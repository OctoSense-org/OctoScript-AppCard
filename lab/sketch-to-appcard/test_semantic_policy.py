import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # lab/, for `core`
import json,tempfile,unittest
from pathlib import Path
from core.semantic_policy import compare,evaluate,POLICY,source_tree_hash
from semantic_lowering import lower
from core.policy import sha


class SemanticPolicyTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.spec={'native_widget_id':'region','object_id':'source','name':'chart','reference_sha256':'reference',
                   'children':[{'native_widget_id':'curve','name':'path','object_id':'curve-source'}]}
        self.portable={'elements':[{'id':'native','original_id':'region','kind':'Svg'}]}
        p=self.root/'data.json';p.write_text('[{"x":0,"y":2},{"x":1,"y":3}]')
        self.entry={'id':'region','role':'chart.line','decision':'reviewed','basis':'reviewed source trend',
            'data':{'path':'data.json','sha256':sha(p),'origin':'fixture','x_key':'x','y_keys':['y'],
                    'units':{'x':'index','y':'value'},'domain':{'x':[0,1],'y':[0,4]}}}
        self.manifest={'policy_version':POLICY['version'],'reference_sha256':'reference','elements':[self.entry]}
        self.manifest['source_review']={'verdict':'complete','reviewer':'test','basis':'reviewed all source regions',
            'method':'source_image_and_hierarchy','source_tree_sha256':source_tree_hash(self.spec)}
    def tearDown(self):self.temp.cleanup()
    def test_svg_chart_cannot_pass(self):
        r=compare(self.spec,self.portable,self.root,self.manifest)
        self.assertFalse(r['pass']);self.assertTrue(any('numerical widget' in e for e in r['errors']))
    def test_anonymous_source_requires_review_even_without_name_candidates(self):
        self.spec['name']='Group 42'
        r=compare(self.spec,self.portable,self.root)
        self.assertFalse(r['pass']);self.assertTrue(any('whole-source' in e for e in r['errors']))
    def test_review_reuse_keeps_exact_spans_when_blank_row_count_changes(self):
        import copy
        self.spec['name']='Terms'
        self.spec['text']={'string':'One\n\nTwo','runs':[{'location':0,'length':8}],
            'source_rows':2,'native_spans':[{'text':'One','y':0},{'text':'Two','y':40}]}
        self.manifest['elements']=[]
        self.manifest['source_review']['source_tree_sha256']=source_tree_hash(self.spec)
        baseline=copy.deepcopy(self.spec)
        self.spec['text']['source_rows']=3
        self.assertTrue(compare(self.spec,self.portable,self.root,self.manifest,
            source_baseline=baseline)['pass'])
        for key,value in [('text','Changed'),('y',41)]:
            changed=copy.deepcopy(self.spec);changed['text']['native_spans'][1][key]=value
            self.assertFalse(compare(changed,self.portable,self.root,self.manifest,
                source_baseline=baseline)['pass'])
        # Without exact span evidence, a changed count cannot reuse the review.
        del baseline['text']['native_spans'];del self.spec['text']['native_spans']
        self.manifest['source_review']['source_tree_sha256']=source_tree_hash(baseline)
        self.assertFalse(compare(self.spec,self.portable,self.root,self.manifest,
            source_baseline=baseline)['pass'])
    def test_reference_pixel_change_invalidates_whole_source_review(self):
        for name in ('specs','targets','semantics','captures'):(self.root/name).mkdir()
        target=self.root/'targets/A.png';target.write_bytes(b'reference pixels')
        self.spec['name']='decorative group';self.spec['reference_sha256']=sha(target)
        self.manifest.update(reference_sha256=sha(target),elements=[])
        self.manifest['source_review']['source_tree_sha256']=source_tree_hash(self.spec)
        (self.root/'specs/A.json').write_text(json.dumps(self.spec))
        (self.root/'semantics/A.json').write_text(json.dumps(self.manifest))
        kit={'specs_dir':self.root/'specs','targets_dir':self.root/'targets','splash_makepad_dir':self.root/'captures'}
        self.assertTrue(evaluate(kit,'A',self.portable)['pass'])
        target.write_bytes(b'changed pixels')
        report=evaluate(kit,'A',self.portable)
        self.assertFalse(report['pass']);self.assertTrue(any('reference pixels changed' in e for e in report['errors']))
    def test_unclassified_chart_cannot_pass_as_generic_graphics(self):
        self.assertFalse(compare(self.spec,self.portable,self.root)['pass'])
    def test_reviewed_card_does_not_hide_an_unreviewed_nested_chart(self):
        self.entry['role']='card'
        self.spec['children'][0]['name']='chart'
        r=compare(self.spec,self.portable,self.root,self.manifest)
        self.assertTrue(any('curve: source region needs' in e for e in r['errors']))
    def test_declared_chart_cannot_be_relabelled_as_artwork(self):
        self.spec['semantic_role']='chart.line';self.entry['role']='illustration'
        self.assertFalse(compare(self.spec,self.portable,self.root,self.manifest)['pass'])
    def test_values_are_checked_even_if_data_hash_matches(self):
        self.portable['elements'][0]['kind']='StockPlot'
        snap={'build_id':[3],'widgets':[{'id':'native','widget_type':'LinePlot'}]}
        state={'build_id':[3],'nonce':'current','elements':{'region':{'native_id':'native','data_sha256':self.entry['data']['sha256'],
               'series':[{'x':[0,1],'y':[2,99]}]}}}
        r=compare(self.spec,self.portable,self.root,self.manifest,snap,state,{'nonce':'current'})
        self.assertTrue(any('actual native series' in e for e in r['errors']))
    def test_lowering_preserves_text_and_binds_real_numeric_widget(self):
        self.entry['replacement']={'paint_sources':['curve']}
        tree={'t':'stack','id':'region','c':[{'t':'svg','id':'curve','x':1,'y':2,'w':100,'h':40},
                                          {'t':'text','id':'title','text':'Trend'}]}
        bindings=lower(self.spec,tree,self.manifest,self.root)
        self.assertEqual(tree['c'][0]['t'],'stockplot');self.assertEqual(tree['c'][1]['text'],'Trend')
        self.assertEqual(bindings[0]['id'],'region_data')
        self.assertEqual(self.spec['children'][0]['graphic_part_of'],'region')
    def test_lowering_cannot_consume_source_text(self):
        self.entry['replacement']={'paint_sources':['curve']};self.spec['children'][0]['text']={'string':'$120'}
        tree={'t':'stack','id':'region','c':[{'t':'text','id':'curve','x':0,'y':0,'w':10,'h':10}]}
        with self.assertRaisesRegex(ValueError,'text or controls'):lower(self.spec,tree,self.manifest,self.root)

    def test_data_mask_clips_only_plot_and_requires_source_evidence(self):
        import copy
        self.spec.update(x=0,y=0,w=200,h=80)
        self.spec['children'][0]['graphic_masks']=[dict(x=2,y=4,w=200,h=80)]
        self.entry['replacement']={'paint_sources':['curve'],'clip_to_bounds':True}
        tree={'t':'stack','id':'region','x':0,'y':0,'w':100,'h':40,'c':[
            {'t':'svg','id':'curve','x':1,'y':2,'w':100,'h':40},
            {'t':'text','id':'title','text':'Outside marker','x':1,'y':-10,'w':100,'h':10}]}
        bad=copy.deepcopy(self.spec);bad['children'][0]['graphic_masks']=[]
        with self.assertRaisesRegex(ValueError,'source-mask evidence'):
            lower(bad,copy.deepcopy(tree),self.manifest,self.root)
        lower(self.spec,tree,self.manifest,self.root)
        self.assertEqual(tree['c'][0]['variant'],'clip')
        self.assertEqual(tree['c'][0]['c'][0]['t'],'stockplot')
        self.assertEqual(tree['c'][1]['id'],'title')

    def test_native_chart_keeps_source_paint_order_above_card_background(self):
        self.entry['replacement']={'paint_sources':['curve']}
        tree={'t':'stack','id':'region','c':[
            {'t':'stack','id':'background','bg':0xffffffff},
            {'t':'svg','id':'curve','x':1,'y':2,'w':100,'h':40},
            {'t':'text','id':'title','text':'Trend'}]}
        lower(self.spec,tree,self.manifest,self.root)
        self.assertEqual([n['id'] for n in tree['c']],['background','region_data','title'])


if __name__=='__main__':unittest.main()
