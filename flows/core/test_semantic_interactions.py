import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # lab/, for `core`
import unittest
from PIL import Image

from core.semantic_interactions import exposed_point, surface_palette


class SurfacePaletteTests(unittest.TestCase):
    def test_click_target_avoids_a_floating_native_button(self):
        elements=[{'id':'radio','kind':'Radio'},{'id':'floating','kind':'Button'}]
        layout={'radio':{'clipped_bounds':[150,737,75,75]},'floating':{'clipped_bounds':[162,730,52,52]}}
        point,blockers=exposed_point('radio',elements,layout)
        self.assertIsNotNone(point)
        x,y=point
        self.assertTrue(150<=x<225 and 737<=y<812)
        self.assertFalse(162<=x<214 and 730<=y<782)
        self.assertEqual(blockers[0]['id'],'floating')

    def test_fully_covered_control_does_not_claim_a_click_target(self):
        elements=[{'id':'radio','kind':'Radio'},{'id':'cover','kind':'Button'}]
        layout={'radio':{'clipped_bounds':[10,10,20,20]},'cover':{'clipped_bounds':[0,0,100,100]}}
        self.assertIsNone(exposed_point('radio',elements,layout)[0])

    def test_clipped_last_control_has_no_click_target(self):
        self.assertIsNone(exposed_point('radio',[{'id':'radio','kind':'Radio'}],
            {'radio':{'clipped_bounds':[10,10,0,0]}})[0])

    def test_palette_accounts_for_composited_modal_scrim(self):
        image=Image.new('RGB',(100,40),(205,207,212))
        for x in range(50):
            for y in range(40):image.putpixel((x,y),(29,39,53))
        config={'items':[
            {'surface_color':0xff1f2a37,'surfaces':[[0]]},
            {'surface_color':0xffeeeff2,'surfaces':[[1]]}]}
        layout={'bar_0':{'bounds':[0,0,50,40]},'bar_1':{'bounds':[50,0,50,40]}}
        palette=surface_palette(config,{'id':'bar'},layout,image,1)
        self.assertEqual(palette[0xff1f2a37],[29,39,53])
        self.assertEqual(palette[0xffeeeff2],[205,207,212])
        self.assertGreater(max(abs(a-b) for a,b in zip(palette[0xff1f2a37],palette[0xffeeeff2])),3)

    def test_nonuniform_occlusion_cannot_supply_a_false_palette(self):
        image=Image.new('RGB',(100,40),(205,207,212))
        image.putpixel((75,4),(255,255,255))
        config={'items':[{'surface_color':0xffeeeff2,'surfaces':[[0],[1]]}]}
        layout={'bar_0':{'bounds':[0,0,50,40]},'bar_1':{'bounds':[50,0,50,40]}}
        with self.assertRaisesRegex(RuntimeError,'varies across sample points'):
            surface_palette(config,{'id':'bar'},layout,image,1)


if __name__=='__main__':unittest.main()
