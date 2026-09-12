import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # lab/, for `core`
import io
import queue
import unittest
from types import SimpleNamespace
from core.studio_bridge import query_batch


class QueryBatchTests(unittest.TestCase):
    def run_batch(self, replies, queries=('id:a', 'id:b')):
        messages = queue.Queue()
        for row in replies:
            messages.put({'WidgetQuery': row})
        process = SimpleNamespace(stdin=io.StringIO())
        requests = [{'WidgetQuery': {'build_id': [7], 'query': q}} for q in queries]
        return query_batch(requests, process, messages, timeout=.01), process.stdin.getvalue()

    def test_out_of_order_exact_replies_are_preserved(self):
        replies = [{'build_id': [7], 'query': q, 'widgets': [{'id': q}]} for q in ('id:b', 'id:a')]
        result, sent = self.run_batch(replies)
        self.assertEqual(result['responses'], replies)
        self.assertEqual(len(sent.splitlines()), 2)

    def test_other_build_cannot_satisfy_batch(self):
        with self.assertRaisesRegex(RuntimeError, 'unexpected'):
            self.run_batch([{'build_id': [8], 'query': 'id:a'}])

    def test_duplicate_reply_fails(self):
        with self.assertRaisesRegex(RuntimeError, 'duplicate'):
            self.run_batch([{'build_id': [7], 'query': 'id:a'}]*2)

    def test_missing_reply_fails(self):
        with self.assertRaises(queue.Empty):
            self.run_batch([{'build_id': [7], 'query': 'id:a'}])

    def test_wildcards_and_duplicate_requests_fail(self):
        for queries in (('*',), ('id:a','id:a')):
            with self.assertRaises(ValueError):
                self.run_batch([], queries)


if __name__ == '__main__':
    unittest.main()
