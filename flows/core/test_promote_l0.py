import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # lab/, for `core`
import unittest

from core import promote_l0 as promote


class PromotionTests(unittest.TestCase):
    def test_literal_reader_preserves_quotes_newlines_unicode_and_scientific_numbers(self):
        tree=promote.parse_design(r'{t: "text" id: "caption" x: -1e-9 text: "line\n\"two\" ☃"}')
        self.assertEqual(tree['text'],'line\n"two" ☃')
        self.assertEqual(tree['x'],-1e-9)
        for source in ('fn bad() {}', '{t: "text"} run()', '{t: "text" t: "image"}'):
            with self.assertRaises(ValueError):promote.parse_design(source)

    def test_body_tokens_keep_regular_font_and_weight_together(self):
        pack={'theme':'light','tokens':{'regular':{'value':'Regular.ttf'},'bold':{'value':'Bold.ttf'},
              'w400':{'value':400},'w700':{'value':700},'s14':{'value':14}},
              'components':{name:{'role':'TextBody','style':{'font_src':{'$token':font},
                  'weight':{'$token':weight},'size':{'$token':'s14'}},'uses':uses,'props':{'text':'text'},'slot':False}
                  for name,font,weight,uses in [('normal','regular','w400',4),('emphasis','bold','w700',20)]}}
        promote.semantic_tokens(pack,[])
        self.assertEqual(pack['tokens']['typography.body.font_src']['value'],'Regular.ttf')
        self.assertEqual(pack['tokens']['typography.body.weight']['value'],400)


if __name__=='__main__':unittest.main()
