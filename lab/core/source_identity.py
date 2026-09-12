"""Keep reviewed identities stable when Sketch re-detaches symbol instances.

Detached object UUIDs are ephemeral. Original source paths and ordered source
hierarchies establish correspondence; reference pixels and source content still
have to match before an existing review can be reused.
"""
import hashlib
import json


def indexed(spec):
    result = {}
    def visit(node, parent='', index=0):
        key = node.get('source_path') or f'{parent}/child:{index}:{node.get("cls")}:{node.get("name")}'
        if key in result:
            raise ValueError('ambiguous original Sketch source identity: '+key)
        result[key] = node
        for i, child in enumerate(node.get('children', [])):
            visit(child, key, i)
    visit(spec)
    return result


def stable_tree_hash(spec):
    fields = ('cls', 'name', 'symbol_name', 'x', 'y', 'w', 'h', 'text')
    rows = [(key, {k: node.get(k) for k in fields}) for key, node in indexed(spec).items()]
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def retained_widget_ids(spec, baseline):
    previous = indexed(baseline)
    return {id(node): previous[key]['native_widget_id']
            for key, node in indexed(spec).items()
            if key in previous and previous[key].get('native_widget_id')}
