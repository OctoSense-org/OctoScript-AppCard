"""Regressions discovered by importing Camo's light/dark source document."""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[2]))  # flows/, for `core`
import json
import pathlib
import tempfile
import unittest
from unittest.mock import patch

from sketch2spec import Extractor
import sketch_native
from core import gate_structure
from core.test_structure import fixture


class CamoNativeTests(unittest.TestCase):
    def test_short_line_box_does_not_apply_svg_compression_twice(self):
        text={'run':{'font':'DMSans-Bold','size':60},
              'font_metrics':{'ascender':.992,'descender':-.31,'line_gap':0},
              'runs':[{'attributes':{'paragraphStyle':{'minimumLineHeight':64,'maximumLineHeight':64}}}]}
        node={'text':text,'h':64}
        self.assertEqual(sketch_native.text_baseline(node,[{'y':53.5}]),53.5)

    def test_optically_sized_emoji_keeps_source_baseline_and_line_box(self):
        node={'text':'🤧','size':16,'line_height':24}
        with patch('sketch_native.emoji_metrics',return_value={'size':20,'ascender':1,'descender':-.3125,'baseline_shift':4}):
            sketch_native.apply_emoji_metrics(node,19)
        self.assertEqual(node['size'],20)
        self.assertAlmostEqual((1+node['font_asc'])*node['size']-4,19)
        self.assertAlmostEqual((-.3125+node['font_desc'])*node['size']-4,19-24)
        self.assertIn('Apple Color Emoji.ttc',sketch_native.font_properties('AppleColorEmoji')['font_src'])

    def test_ancestor_blend_requires_context_and_cannot_flatten_text(self):
        root={'object_id':'group','children':[{'object_id':'shape'}]}
        raw={'group':{'_class':'group','style':{'contextSettings':{'blendMode':2}}},'shape':{}}
        sketch_native.annotate_group_blends(root,raw)
        self.assertIn('ancestor group blend modes 2',root['children'][0]['backdrop_fallback'])
        root['children'][0]['text']={'string':'native text'}
        with self.assertRaises(ValueError):sketch_native.annotate_group_blends(root,raw)

    def test_code_input_owns_its_reused_button_styling(self):
        f=fixture();source=f['spec']['children'][0]
        source.update(name='Code',symbol_name='Inputs/Code/Filled',control={'kind':'text_input'},
                      children=[{'object_id':'style','name':'Buttons/Large/Normal/Rest','w':20,'h':20}])
        missing=lambda:[e for e in gate_structure.compare(**f)['inspection_errors']
                        if 'lacks native control mapping' in e]
        self.assertEqual(missing(),[])
        source['children'][0]['name']='Inputs/Dropdown/Large'
        self.assertEqual(missing(),[])
        del source['control']
        self.assertEqual(len(missing()),2)

    def test_dropdown_owns_its_sized_prototype(self):
        f=fixture();source=f['spec']['children'][0]
        source.update(name='Season',symbol_name='Inputs/Dropdown',control={'kind':'button'},
                      children=[{'object_id':'style','name':'Inputs/Dropdown/Large','w':20,'h':20}])
        errors=gate_structure.compare(**f)['inspection_errors']
        self.assertFalse(any('lacks native control mapping' in e for e in errors))

    def test_navigation_item_requires_native_button_mapping(self):
        f=fixture();source=f['spec']['children'][0]
        source.update(name='Item 1',symbol_name='Navigation/Appbar/Item')
        missing=lambda:[e for e in gate_structure.compare(**f)['inspection_errors']
                        if 'lacks native control mapping' in e]
        self.assertEqual(len(missing()),1)
        source['control']={'kind':'button'}
        self.assertEqual(missing(),[])

    def test_empty_compound_retains_operand_bounds_and_cannot_suppress_text(self):
        source={'native_widget_id':'source','children':[
            {'object_id':'operand','x':1,'y':2,'w':3,'h':4,'graphic_part_of':'source'}]}
        children=sketch_native.empty_graphic_children(source)
        self.assertEqual([children[0][k] for k in ('x','y','w','h')],[1,2,3,4])
        self.assertEqual(children[0]['t'],'stack')
        self.assertNotIn('graphic_part_of',source['children'][0])
        self.assertEqual(children[0]['id'],source['children'][0]['native_widget_id'])
        source['children'][0]['text']={'string':'must remain text'}
        with self.assertRaises(ValueError):sketch_native.empty_graphic_children(source)

    def test_import_resume_rejects_changed_source_code_or_output(self):
        with tempfile.TemporaryDirectory() as td:
            root=pathlib.Path(td);asset=root/'asset.svg';asset.write_text('source paint')
            receipt=root/'receipt.json';receipt.write_text(json.dumps({
                'inputs':'source-code-key','outputs':{str(asset):sketch_native.digest(asset)}}))
            self.assertTrue(sketch_native.import_current(receipt,'source-code-key'))
            self.assertFalse(sketch_native.import_current(receipt,'changed-code'))
            asset.write_text('changed paint')
            self.assertFalse(sketch_native.import_current(receipt,'source-code-key'))
            asset.unlink()
            self.assertFalse(sketch_native.import_current(receipt,'source-code-key'))

    def test_group_shadow_reaches_background_through_transparent_wrapper(self):
        shadow={'blur':32,'dy':16,'dx':0}
        bg={'object_id':'bg','cls':'rectangle','x':0,'y':0,'w':140,'h':64,'fill':{'a':1}}
        root={'object_id':'outer','cls':'group','x':0,'y':0,'w':140,'h':64,'shadow':shadow,
              'children':[{'object_id':'inner','cls':'group','x':0,'y':0,'w':140,'h':64,'children':[bg]}]}
        raw={'outer':{'style':{'shadows':[{'isEnabled':True,'blurRadius':32}]}},'inner':{},'bg':{}}
        sketch_native.apply_group_shadows(root,raw)
        self.assertEqual(bg['shadow'],shadow)
        self.assertEqual(raw['bg']['style']['shadows'][0]['blurRadius'],32)

    def test_password_circles_become_editable_mask_and_need_explicit_ownership(self):
        value={'object_id':'value','name':'Value','x':24,'y':40,'w':120,'h':20,
               'text':{'string':' '},'cls':'text'}
        mask={'object_id':'mask','name':'Password / Hide','x':24,'y':46,'w':18,'h':6,
              'children':[{'object_id':str(i),'cls':'oval','x':24+12*i,'y':46,'w':6,'h':6,
                           'fill':{'hex':'#000000','a':1}} for i in range(2)]}
        source={'object_id':'artboard','children':[
            {'object_id':'field','symbol_name':'Inputs/Text-Field/Rest','children':[value]},mask]}
        # A repeated Sketch detachment changes UUIDs while reviewed native IDs
        # stay stable. Cross-group mask ownership must use that same retained ID.
        sketch_native.annotate_inputs(source, {id(value): 'reviewed_password_field'})
        self.assertEqual(mask['control_part_of'], 'reviewed_password_field')
        self.assertTrue(all(dot['control_part_of']=='reviewed_password_field' for dot in mask['children']))
        self.assertEqual(value['control']['value'],'••')
        self.assertTrue(value['control']['password'])
        self.assertEqual(value['text']['string'],' ')
        f=fixture();field=f['spec']['children'][0]
        field.update(control=value['control'],native_widget_id=mask['control_part_of'])
        f['portable']['elements'][1]['original_id']=mask['control_part_of']
        f['spec']['children'].append(mask)
        invalid=lambda:[e for e in gate_structure.compare(**f)['inspection_errors']
                        if 'invalid compound graphic coverage' in e]
        self.assertEqual(invalid(),[])
        field['control']['graphic_mask_source_id']='unrelated'
        self.assertEqual(len(invalid()),3)

    def test_text_fill_opacity_inherits_once_and_can_be_overridden(self):
        with tempfile.TemporaryDirectory() as td:
            path=pathlib.Path(td)/'text.svg'
            path.write_text('''<svg xmlns="http://www.w3.org/2000/svg">
              <g opacity="0.5" fill-opacity="0.4" font-family="DMSans-Regular" font-size="12">
                <g><text><tspan x="0" y="12">Muted</tspan>
                  <tspan x="0" y="24" fill-opacity="0.8" opacity="0.5">Override</tspan>
                </text></g>
              </g></svg>''')
            spans=sketch_native.text_spans(path)
            self.assertAlmostEqual(spans[0]['opacity'],.2)
            self.assertAlmostEqual(spans[1]['opacity'],.2)

    def test_symbol_styling_group_shares_only_its_own_native_control(self):
        f=fixture()
        source=f['spec']['children'][0]
        variant='Buttons/Large/Icon+Label/Rest'
        source.update(name='Deposit',symbol_name=variant,control={'kind':'button'},children=[
            {'object_id':'inner','name':variant,'cls':'group','w':20,'h':20}])
        missing=lambda: [e for e in gate_structure.compare(**f)['inspection_errors']
                         if 'lacks native control mapping' in e]
        self.assertEqual(missing(),[])
        source['symbol_name']='Buttons/Large/Other/Rest'
        self.assertEqual(len(missing()),1)
        source['symbol_name']=variant
        del source['control']
        self.assertEqual(len(missing()),2)

    def test_duplicate_page_names_retain_both_artboards(self):
        with tempfile.TemporaryDirectory() as td:
            root=pathlib.Path(td);(root/'pages').mkdir()
            (root/'document.json').write_text('{}')
            (root/'meta.json').write_text(json.dumps({'pagesAndArtboards':{
                'light':{'name':'Finance'}, 'dark':{'name':'Finance'}}}))
            for pid in ('light','dark'):
                (root/'pages'/f'{pid}.json').write_text(json.dumps({'name':'Finance','layers':[
                    {'_class':'artboard','do_objectID':pid,'name':'Home','frame':{'width':375,'height':812}}]}))
            boards=list(Extractor(root).artboards('Finance'))
            self.assertEqual({n['object_id'] for n in boards},{'light','dark'})
            names=sketch_native.artboard_names(boards,{'light':'Light_Home','dark':'Dark_Home'})
            self.assertEqual(set(names.values()),{'Light_Home','Dark_Home'})
            with self.assertRaises(ValueError):
                sketch_native.artboard_names(boards,{'light':'Home','dark':'Home'})

    def test_archive_fonts_use_their_own_metrics_without_changing_atro_weights(self):
        fonts={'DMSans-Bold':{'weight':700,'resource':'self:resources/camo/DMSans-Bold.ttf'},
               'Montserrat-Medium':{'resource':'self:resources/atro/Montserrat-Medium.ttf'}}
        self.assertEqual(sketch_native.font_properties('DMSans-Bold',fonts)['weight'],700)
        self.assertEqual(sketch_native.font_properties('Montserrat-Medium',fonts)['weight'],500)
        source={'text':{'run':{'size':16,'font':'DMSans-Bold'},
            'font_metrics':{'ascender':.992,'descender':-.31,'line_gap':0},
            'runs':[{'attributes':{'paragraphStyle':{'minimumLineHeight':24,'maximumLineHeight':24}}}]}}
        self.assertEqual(sketch_native.text_baseline(source,[{'y':16}]),17.5)

    def test_floating_input_title_remains_text_and_is_not_a_second_input(self):
        title={'name':'Full name','text':{'string':'Full name'}}
        value={'name':'Value','text':{'string':'Alex Smith'}}
        source={'name':'Field','symbol_name':'Inputs/Text-Field/Selected','children':[
            {'name':'Title','children':[title]}, {'name':'Content','children':[value]}]}
        sketch_native.annotate_inputs(source)
        self.assertNotIn('control',title)
        self.assertEqual(value['control']['value'],'Alex Smith')
        self.assertFalse(value['control']['focused'])

    def test_native_binary_controls_keep_source_state_and_reject_text_flattening(self):
        for variant,kind,checked in [('Inputs/Selector/Checkbox/Checked','checkbox',True),
                                     ('Inputs/Selector/Radio-Button/Rest','radio',False),
                                     ('Inputs/Switch-Toggle/Large/On','toggle',True)]:
            with self.subTest(variant=variant):
                source={'name':variant,'w':18,'h':18,'children':[
                    {'name':'Base','w':18,'h':18,'fill':{'hex':'#0077ff','a':1},'radius':3}]}
                node={'id':'control'}
                self.assertTrue(sketch_native.camo_binary_control(source,node))
                self.assertEqual(node['t'],kind)
                self.assertEqual(source['control']['checked'],checked)
                self.assertEqual(source['children'][0]['control_part_of'],'control')
                source['children'].append({'text':{'string':'Keep native'}})
                with self.assertRaises(ValueError):sketch_native.camo_binary_control(source,node)


if __name__=='__main__':unittest.main()
