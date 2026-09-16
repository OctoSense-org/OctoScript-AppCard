"""Prepare the shared Octoscript-Makepad release used by every AppCard."""
import argparse
import json
from common import NATIVE_ROOT
from core.native_runtime import prepare


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--update', action='store_true', help='Update clean dependency checkouts to the locked release')
    args = parser.parse_args()
    print(json.dumps(prepare(NATIVE_ROOT, update=args.update), indent=2))


if __name__ == '__main__':
    main()
