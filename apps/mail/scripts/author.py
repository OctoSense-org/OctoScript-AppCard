"""Author contracts, then preserve and review automated image observations."""
from pathlib import Path
from copy import deepcopy
import argparse
import json
import shutil
from common import ROOT
from model import initial, reduce
from render import render


def states():
    base=initial()
    base['drafts']=[{'to':'','subject':'Coffee next week?','body':'Hi Jamie,\n\nWould you like to grab coffee next week?\n\nBest,'}]
    result=[base,reduce(base,'navigate',{'screen':'mailboxes'}),reduce(base,'open',{'id':'demo-0'}),
        reduce(reduce(base,'navigate',{'screen':'search'}),'search',{'value':'design'}),
        reduce(base,'open_draft',{'index':0}),reduce(base,'folder',{'folder':'unread'}),
        reduce(base,'navigate',{'screen':'settings'}),reduce(base,'navigate',{'screen':'card'})]
    return result


def main():
    p=argparse.ArgumentParser();p.add_argument('stage',choices=['contracts','review']);args=p.parse_args()
    for i,state in enumerate(states(),1):
        d=ROOT/'cards'/f'ios-mail-{i:02d}'
        if args.stage=='review' and (d/'mapped.json').exists() and not (d/'mapped-proposal.json').exists():
            shutil.copy2(d/'mapped.json',d/'mapped-proposal.json')
        render(state,d,f'ios-mail-{i:02d}',compile_native=args.stage=='review')
        if args.stage=='contracts':
            for name in ['mapped.json','semantic-map.json','service-actions.json']:(d/name).unlink(missing_ok=True)
        else:
            # The bundle resolves hashed artwork inside the project, independently
            # of the native compiler's loopback preview gallery.
            shutil.copytree(d/'assets',ROOT/'assets'/d.name/'assets',dirs_exist_ok=True)
            (d/'AUTHORING.md').write_text('# Reviewed native mapping\n\nThe atlas was inspected as eight app/service states. Apple Vision observations and contour measurements are retained separately. The generated atlas did not follow the requested screen aspect ratios, so the implementation deliberately reflows its shared hierarchy onto a 406 × 776 point mobile surface. Native Inter text, KitButton controls, KitFormField inputs, and SVG line icons implement the design. This is an explicit layout adaptation; strict pixel parity has not been asserted. Runtime messages and local state replace fixture copy without altering service actions.\n')
        print(f'{args.stage}: ios-mail-{i:02d}',flush=True)

if __name__=='__main__':main()
