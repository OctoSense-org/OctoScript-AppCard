#!/usr/bin/env python3
"""Fault-injection tests for Studio structural inspection and design rejection."""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # flows/, for `core`
import copy
import unittest
from core import gate_structure as gate


def fixture():
    spec={'object_id':'artboard','cls':'artboard','x':0,'y':0,'w':393,'h':852,'children':[
        {'object_id':'a','cls':'text','x':24,'y':40,'w':120,'h':20,'text':{'string':'Alpha'}},
        {'object_id':'b','cls':'text','x':24,'y':70,'w':120,'h':20,'text':{'string':'Beta'}}]}
    nodes=[{'id':'beauty_0','parent':None,'kind':'Column'},
           {'id':'beauty_0_0','parent':'beauty_0','kind':'Text','text':'Alpha'},
           {'id':'beauty_0_1','parent':'beauty_0','kind':'Checkbox','text':'Beta','on':1}]
    bounds=[[0,0,393,852],[24,40,120,20],[24,70,120,20]]
    dump={'dump':'W3 4\n0 -1 main_window Window 0 0 393 852\n'+''.join(
        f'{i+1} {0 if i==0 else 1} {n["id"]} {"View" if i==0 else "Label"} '+
        ' '.join(map(str,b))+'\n' for i,(n,b) in enumerate(zip(nodes,bounds)))}
    snap={'widgets':[{'id':'main_window','widget_type':'Window','x':80,'y':100,'width':393,'height':852}]}
    query={}
    layout={'elements':[]}
    for n,b in zip(nodes,bounds):
        snap['widgets'].append({'id':n['id'],'widget_type':'View' if n['kind']=='Column' else n['kind'],
            'window_id':'main_window','x':b[0]+80,'y':b[1]+100,'width':b[2],'height':b[3],
            'visible':True,'enabled':True,'text':n.get('text'),'value':None,
            'checked':True if n.get('on') else None,'selected':None})
        query[n['id']]={'rects':[f'0 {n["id"]} View '+ ' '.join(map(str,b))]}
        layout['elements'].append({'id':n['id'],'bounds':b.copy(),'clipped_bounds':b.copy()})
    return dict(spec=spec,portable={'elements':nodes},dump=dump,snapshot=snap,queries=query,layout=layout)


class StructureTests(unittest.TestCase):
    def test_native_data_clip_requires_exact_identity_ancestry_and_bounds(self):
        source={'native_data_widget_id':'series','native_data_bounds_logical':[5,10,100,40]}
        plot={'parent':'clip'}
        wrapper={'id':'clip','parent':'owner','kind':'Stack'}
        imported={'series_clip':[wrapper]}
        actual={'clip':{'type':'View','bounds':[5,10,100,40]}}
        check=lambda:gate.numerical_paint_is_owned(source,'owner',plot,imported,actual,1)
        self.assertTrue(check())
        wrapper['parent']='unrelated';self.assertFalse(check());wrapper['parent']='owner'
        actual['clip']['bounds'][2]=90;self.assertFalse(check());actual['clip']['bounds'][2]=100
        actual['clip']['type']='Image';self.assertFalse(check());actual['clip']['type']='View'
        imported['series_clip'].append(wrapper.copy());self.assertFalse(check())

    def test_tab_adapter_requires_explicit_role_and_inspected_native_radio(self):
        f=fixture();f['spec']['native_widgets_first']=True
        source=f['spec']['children'][0]
        source.pop('text')
        source.update(name='Tab Field',cls='group',native_widget_id='source_tab',
            control=dict(kind='radio',semantic_role='tab',adapter='native RadioButton selection',
                         checked=True,enabled=True))
        node=f['portable']['elements'][1]
        node.update(kind='Radio',original_id='source_tab',on=1)
        node.pop('text')
        snapshot=f['snapshot']['widgets'][2]
        snapshot.update(widget_type='RadioButton',checked=True,text=None)
        self.assertTrue(gate.compare(**f)['pass'])
        source['control'].pop('semantic_role')
        self.assertTrue(any('lacks native control mapping' in e
                            for e in gate.compare(**f)['inspection_errors']))
        source['control']['semantic_role']='tab'
        snapshot['widget_type']='View'
        self.assertTrue(any('native RadioButton' in e
                            for e in gate.compare(**f)['inspection_errors']))

    def test_graphic_overlay_requires_explicit_source_route_and_owner(self):
        spec={'glass_foreground_routes':['source_paint']}
        source={'native_paint_id':'source_paint'}
        owner={'id':'owner','image':'graphic.svg'}
        paint={'parent':'overlay','image':'graphic.svg'}
        wrapper={'id':'overlay','parent':'owner','kind':'Stack'}
        imported={'source_paint_foreground':[wrapper]}
        actual={'overlay':{'type':'DesignOverlay'}}
        self.assertTrue(gate.graphic_paint_is_owned(spec,source,owner,paint,imported,actual))
        self.assertFalse(gate.graphic_paint_is_owned({},source,owner,paint,imported,actual))
        wrapper['parent']='unrelated'
        self.assertFalse(gate.graphic_paint_is_owned(spec,source,owner,paint,imported,actual))
        wrapper['parent']='owner';paint['image']='different.svg'
        self.assertFalse(gate.graphic_paint_is_owned(spec,source,owner,paint,imported,actual))

    def test_rotated_source_intersection_uses_painted_extent(self):
        spec={'object_id':'root','w':375,'h':812,'children':[
            {'object_id':'outside','x':181.525,'y':-121.475,'w':8,'h':177.3,
             'rot':90,'fill':{'a':1}},
            {'object_id':'inside','x':-30,'y':100,'w':8,'h':100,
             'rot':90,'fill':{'a':1}}]}
        rows=gate.source_elements(spec,1)
        self.assertFalse(rows[1]['required'])
        self.assertTrue(rows[2]['required'])
        self.assertEqual(rows[2]['bounds'],[-30,100,8,100])

    def test_masked_out_source_descendants_are_not_required_visible_elements(self):
        spec={'object_id':'root','cls':'artboard','x':0,'y':0,'w':100,'h':100,'children':[
            {'object_id':'hidden','cls':'group','fully_clipped':True,'graphic_masks':[{'x':60,'y':60,'w':10,'h':10}],'x':0,'y':0,'w':50,'h':50,'children':[
                {'object_id':'text','cls':'text','x':0,'y':0,'w':40,'h':20,'text':{'string':'masked'}}]}]}
        rows=gate.source_elements(spec,1)
        self.assertFalse(rows[-1]['visible'])
        self.assertFalse(rows[-1]['required'])

    def test_visibility_cannot_hide_stroked_rules_without_a_source_mask(self):
        f=fixture()
        f['spec']['children'][0].update(fully_clipped=True,w=0,stroke={'w':1})
        result=gate.compare(**f)
        self.assertFalse(result['inspection_pass'])
        self.assertTrue(any('without a source mask' in e for e in result['inspection_errors']))

    def test_source_baseline_overflow_requires_unclipped_native_ink(self):
        f=fixture()
        f['spec']['children'][0]['text']['native_baseline']=25
        f['layout']['elements'][1]['text_clip']=[True,True]
        result=gate.compare(**f)
        self.assertTrue(any('source_glyph_overflow_clipped' in e['issues'] for e in result['elements']))
        f['layout']['elements'][1]['text_clip']=[False,False]
        self.assertTrue(gate.compare(**f)['pass'])

    def test_subpixel_widget_still_requires_query_and_retains_precise_bounds(self):
        f=fixture()
        source=f['spec']['children'][0]
        source['w']=.4
        f['dump']['dump']=f['dump']['dump'].replace('24 40 120 20','24 40 0 20')
        f['snapshot']['widgets'][2]['width']=0
        f['queries']['beauty_0_0']['rects']=['0 beauty_0_0 Label 24 40 0 20']
        for key in ('bounds','clipped_bounds'):f['layout']['elements'][1][key][2]=.4
        result=gate.compare(**f)
        self.assertTrue(result['pass'],result)
        f['queries']['beauty_0_0']['rects']=[]
        self.assertFalse(gate.compare(**f)['inspection_pass'])

    def test_text_wrapping_outside_label_frame_fails_structural_gate(self):
        f=fixture()
        f['layout']['elements'][1]['text_layout']=[24,40,120,40]
        r=gate.compare(**f)
        self.assertTrue(r['inspection_pass'])
        self.assertFalse(r['pass'])
        self.assertTrue(any('native_text_layout_overflow' in e['issues'] for e in r['elements']))
        # An independently exported two-row source can intentionally crop its
        # second row. Preserve that source overflow, rather than invent a fix.
        f['spec']['children'][0]['text'].update(source_rows=2,line_height=20)
        self.assertTrue(gate.compare(**f)['pass'])

    def test_extra_text_rows_fail_even_inside_an_oversized_source_frame(self):
        f=fixture()
        f['spec']['children'][0]['h']=80
        f['spec']['children'][0]['text'].update(source_rows=1,line_height=20)
        for key in ('bounds','clipped_bounds'):f['layout']['elements'][1][key][3]=80
        f['dump']['dump']=f['dump']['dump'].replace('24 40 120 20','24 40 120 80')
        f['snapshot']['widgets'][2]['height']=80
        f['queries']['beauty_0_0']['rects']=['0 beauty_0_0 Label 24 40 120 80']
        f['layout']['elements'][1]['text_layout']=[24,40,80,40]
        r=gate.compare(**f)
        self.assertTrue(any('native_text_layout_overflow' in e['issues'] for e in r['elements']))
        f['layout']['elements'][1]['text_layout'][3]=20
        self.assertTrue(gate.compare(**f)['pass'])

    def test_input_requires_native_value_placeholder_and_measured_focus(self):
        f=fixture()
        source=f['spec']['children'][0]
        source['text']['string']='Alpha|'
        source['native_widget_id']='source_input'
        source['control']={'kind':'text_input','value':'Alpha','display_text':'Alpha',
                           'focused':True,'enabled':True}
        f['portable']['elements'][1].update(kind='Input',original_id='source_input',focused=1)
        s=f['snapshot']['widgets'][2]
        s.update(widget_type='TextInput',text='Alpha',value='Alpha')
        f['layout']['elements'][1]['focused']=True
        f['layout']['elements'][1]['password']=False
        self.assertTrue(gate.compare(**f)['pass'])
        s['widget_type']='Label'
        self.assertFalse(gate.compare(**f)['pass'])
        s['widget_type']='TextInput'
        f['layout']['elements'][1]['focused']=False
        self.assertFalse(gate.compare(**f)['pass'])
        f['layout']['elements'][1]['focused']=True
        s['value']='different'
        self.assertFalse(gate.compare(**f)['pass'])

    def test_zero_height_stroked_rule_is_required_visible_content(self):
        f=fixture()
        f['spec']['children'].append({'object_id':'divider','cls':'shapePath',
            'x':24,'y':110,'w':345,'h':0,'stroke':{'w':1,'c':{'hex':'#eeeff2','a':1}}})
        r=gate.compare(**f)
        self.assertFalse(r['pass'])
        divider=next(e for e in r['sketch_hierarchy'] if e['object_id']=='divider')
        self.assertTrue(divider['visible'])
        self.assertTrue(divider['required'])

    def test_imported_identity_does_not_hide_wrong_text_or_geometry(self):
        f=fixture()
        f['spec']['children'][0]['native_widget_id']='sketch_alpha'
        f['portable']['elements'][1]['original_id']='sketch_alpha'
        self.assertTrue(gate.compare(**f)['pass'])
        f['spec']['children'][0]['x']+=10
        self.assertFalse(gate.compare(**f)['pass'])
        f['spec']['children'][0]['x']-=10
        f['spec']['children'][0]['text']['string']='Different source text'
        self.assertFalse(gate.compare(**f)['inspection_pass'])

    def test_missing_imported_identity_cannot_fall_back_to_same_text(self):
        f=fixture()
        f['spec']['children'][0]['native_widget_id']='missing_source_identity'
        self.assertFalse(gate.compare(**f)['pass'])

    def test_matching_structure_and_global_snapshot_origin_pass(self):
        r=gate.compare(**fixture())
        self.assertTrue(r['pass'],r)
        self.assertEqual(r['mapped_elements'],3)

    def test_host_only_dump_fails_even_with_good_screenshot_metadata(self):
        f=fixture()
        f['dump']={'dump':'W3 3\n0 -1 main_window Window 0 0 393 852\n1 0 body KeyboardView 0 0 393 852\n2 1 host Splash 0 0 393 852\n'}
        f['snapshot']['widgets']=f['snapshot']['widgets'][:1]
        r=gate.compare(**f)
        self.assertFalse(r['pass'])
        self.assertTrue(any('host-only' in e for e in r['inspection_errors']))

    def test_missing_exact_query_fails_inspection(self):
        f=fixture(); f['queries']['beauty_0_0']={'rects':[]}
        self.assertFalse(gate.compare(**f)['inspection_pass'])

    def test_missing_native_text_and_checked_state_fail(self):
        for field,value in [('text','Wrong'),('checked',None)]:
            f=fixture(); f['snapshot']['widgets'][-1][field]=value
            self.assertFalse(gate.compare(**f)['inspection_pass'])

    def test_composed_control_selected_state_must_be_observable(self):
        f=fixture(); f['portable']['elements'][0]['selected']=1
        self.assertFalse(gate.compare(**f)['inspection_pass'])
        f['snapshot']['widgets'][1]['selected']='true'
        self.assertTrue(gate.compare(**f)['inspection_pass'])

    def test_native_hierarchy_change_fails(self):
        f=fixture(); f['dump']['dump']=f['dump']['dump'].replace('3 1 beauty_0_1','3 0 beauty_0_1')
        self.assertFalse(gate.compare(**f)['inspection_pass'])

    def test_dimensions_position_and_spacing_are_measured(self):
        f=fixture(); f['spec']['children'][1].update(x=34,y=84,w=145)
        r=gate.compare(**f)
        self.assertTrue(r['inspection_pass'])
        self.assertFalse(r['pass'])
        self.assertTrue(any('dimensions' in e['issues'] and 'position' in e['issues'] for e in r['elements']))
        f=fixture(); f['spec']['children'][1]['y']=84
        self.assertTrue(any('spacing' in e['issues'] for e in gate.compare(**f)['relations']))

    def test_ancestor_clipping_and_invisibility_fail(self):
        f=fixture(); f['layout']['elements'][-1]['clipped_bounds'][2]=20
        self.assertTrue(any('native_ancestor_clipping' in e['issues'] for e in gate.compare(**f)['elements']))
        f=fixture(); f['snapshot']['widgets'][-1]['visible']=False
        self.assertTrue(any('invisible' in e['issues'] for e in gate.compare(**f)['elements']))

    def test_unmapped_design_element_is_not_silently_excluded(self):
        f=fixture(); f['spec']['children'].append({'object_id':'missing','cls':'text','x':24,'y':130,
            'w':120,'h':20,'text':{'string':'Missing content'}})
        self.assertTrue(any('missing_or_unmapped_element' in e['issues'] for e in gate.compare(**f)['elements']))

    def test_duplicate_label_mismatch_is_ambiguous_not_nearest_match(self):
        f=fixture(); extra=copy.deepcopy(f['spec']['children'][0]);extra.update(object_id='duplicate',y=130)
        f['spec']['children'].append(extra)
        r=gate.compare(**f)
        self.assertFalse(r['pass'])
        self.assertEqual(sum(e.get('text')=='Alpha' and 'missing_or_unmapped_element' in e['issues'] for e in r['elements']),2)

    def test_tolerances_and_sketch_scale_are_explicit(self):
        f=fixture()
        for n in [f['spec'],*f['spec']['children']]:
            for k in ('x','y','w','h'):n[k]*=2
        self.assertTrue(gate.compare(**f,scale=2)['pass'])
        f=fixture();f['spec']['children'][0]['x']+=4
        self.assertTrue(gate.compare(**f)['pass'])
        f['spec']['children'][0]['x']+=1
        self.assertFalse(gate.compare(**f)['pass'])


if __name__=='__main__':unittest.main()
