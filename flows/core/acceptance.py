"""State exactly what saved beauty evidence establishes, and what remains open."""
import json


def write(kit, screens, run):
    current = bool(screens) and all(not r['needs_repair'] for r in screens)
    # These are explicit next-round requirements, never inferred from the
    # quantity of Views, screenshots, or matching source coordinates.
    next_round = [
        {'id': 'reusable_l0_l3', 'status': 'not_established',
         'required_evidence': 'Named component definitions and page instances linked to Sketch elements; '
                              'shared properties, slots and state; reuse verified across screens.',
         'repair': 'Extract repeated bars, fields, buttons, cards and lists into shared components; '
                   'compose pages from those components and revalidate every consumer.'},
        {'id': 'responsive_layout', 'status': 'not_established',
         'required_evidence': 'Studio captures and structural checks at the reference size and at least '
                              'two additional configured viewport widths, with long-text and overflow cases.',
         'repair': 'Replace page-wide absolute coordinates with flow, Fill/Fit, spacing, alignment and '
                   'scroll containers; retain absolute positions only for intentional overlays or artwork.'},
        {'id': 'application_workflows', 'status': 'not_established',
         'required_evidence': 'Recorded actions and expected state transitions for navigation, submission, '
                              'selection and scrolling, including disabled, focus and error states.',
         'repair': 'Connect native controls to page state and application actions; exercise the full flows. '
                   'A Button hit target or an editable field alone does not prove an application workflow.'},
    ]
    promoted=kit.get('input_format')=='l0-kit'
    if promoted:
        next_round[0]['status']='passed' if current and all(r.get('kit',{}).get('pass') for r in screens) else 'failed'
        next_round[0]['evidence']='kit-gate.json; per-screen .kit.json and .l0map.json'
    report = {'kit': kit['name'], 'schema_version': 1,
              'scope': 'fixed_artboard_parity',
              'status': 'passed' if current else 'failed', 'pass': current,
              'application_complete': False,
              'screen_count': len(screens),
              'passed_screens': sum(not r['needs_repair'] for r in screens),
              'required_gates': ['current_structural_inspection', 'current_visual_review'] +
                  (['native_widget_policy'] if kit.get('input_format') in ('design','l0-kit') else []) +
                  (['registered_tokens_and_reusable_l0_components'] if promoted else []),
              'pipeline_errors': run.get('errors', []),
              'next_composition_round': next_round,
              'note': 'A fixed-artboard pass does not promote any untested capability to passed. '
                      'Responsive layouts and application workflows require their own validation.'}
    path = kit['splash_makepad_dir']/'acceptance.json'
    path.write_text(json.dumps(report, indent=2)+'\n')
    return report
