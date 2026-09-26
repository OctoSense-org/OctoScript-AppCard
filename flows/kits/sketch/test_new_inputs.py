"""Bugs exposed by the held-out component artboards, independent of their files."""
import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # lab/, for `core`
import unittest
from sketch_native import taskplan_tab_variant,validate_text_fonts
from core.gate_structure import compare


class NewSourceTests(unittest.TestCase):
    def test_tab_catalogue_is_not_itself_a_tab(self):
        self.assertIsNone(taskplan_tab_variant({'name':'Tab Field','children':[
            {'name':'State=Default, Type=Filled'},{'name':'State=Hover, Type=Outline'}]}))
    def test_individual_component_prototype_keeps_its_state(self):
        n={'name':'State=Disable, Type=Outline','cls':'group','children':[{'text':{'string':'Label'}}]}
        self.assertEqual(taskplan_tab_variant(n),'State=Disable, Type=Outline')
    def test_unknown_tab_state_fails(self):
        with self.assertRaisesRegex(ValueError,'unsupported'):taskplan_tab_variant({'name':'Tab Field','symbol_name':'State=New'})
    def test_second_rich_text_face_cannot_silently_substitute(self):
        text={'run':{'font':'Inter-Regular'},'runs':[{'attributes':{
            'MSAttributedStringFontAttribute':{'attributes':{'name':'Missing-Bold'}}}}]}
        with self.assertRaisesRegex(ValueError,'Missing-Bold'):validate_text_fonts(text,{})
    def test_canvas_named_search_is_not_an_input_instance(self):
        spec={'name':'Search','cls':'artboard','object_id':'canvas','w':345,'h':52}
        r=compare(spec,{'elements':[]},{'dump':''},{'widgets':[]},{})
        self.assertFalse(any('text_input' in e for e in r['inspection_errors']))


if __name__=='__main__':unittest.main()
