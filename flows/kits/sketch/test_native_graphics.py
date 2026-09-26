"""Native-first selection must preserve geometry and explain every fallback."""
import pathlib
import tempfile
import unittest
import json
import zipfile
import xml.etree.ElementTree as ET

import native_graphics as graphics
import sketch_native
import sketch_assets


class NativeGraphicsTests(unittest.TestCase):
    def test_blended_shadow_requires_its_source_backdrop(self):
        raw={'style':{'shadows':[dict(isEnabled=True,contextSettings=dict(blendMode=7))]}}
        self.assertIn('shadow blend mode 7',graphics.shadow_backdrop_reason(raw))
        raw['style']['shadows'][0]['isEnabled']=False
        self.assertIsNone(graphics.shadow_backdrop_reason(raw))

    def test_sketch_paragraph_leading_centers_ink_inside_explicit_line_height(self):
        def source(size, height):
            return dict(text={'run':dict(size=size,font='Montserrat-Medium'),
                'runs':[{'attributes':{'paragraphStyle':dict(minimumLineHeight=height,maximumLineHeight=height)}}]})
        # Source PNG has Gallery's ink five pixels above the SVG baseline;
        # 45px body rows place their ink six pixels below the SVG baseline.
        self.assertEqual(sketch_native.text_baseline(source(25,20),[dict(y=24)]),19)
        self.assertEqual(sketch_native.text_baseline(source(27,45),[dict(y=26)]),32)
        self.assertEqual(sketch_native.text_baseline(source(18,0),[dict(y=17)]),17)
        centered=source(18,0);centered['h']=60;centered['text']['vertical_alignment']=1
        self.assertEqual(sketch_native.text_baseline(centered,[dict(y=17,size=18)]),36)

    def test_group_foreground_tint_preserves_native_text_and_ancestor_alpha(self):
        text=dict(object_id='label',text={'string':'Hello'})
        root=dict(object_id='group',children=[text])
        raw={'group':{'_class':'group','style':{'fills':[dict(isEnabled=True,fillType=0,
             layeringType=1,color=dict(red=.9,green=.2,blue=.2,alpha=1))]}},'label':{'_class':'text'}}
        sketch_native.annotate_text_tints(root,raw)
        self.assertEqual(text['text']['group_tint']['source_id'],'group')
        color=sketch_native.native_text_color(text,dict(color='#ffffff',opacity=.6))
        self.assertEqual(color,0x99e63333)
        self.assertEqual(text['text']['string'],'Hello')
        raw['group']['style']['fills'][0]['layeringType']=0
        text['text'].pop('group_tint')
        sketch_native.annotate_text_tints(root,raw)
        self.assertNotIn('group_tint',text['text'])

    def test_sketch_point_preserves_exponents_and_coordinate_order(self):
        from sketch2spec import pt, Extractor
        self.assertEqual(pt('{1.722546424198833e-16, 0}'), (1.722546424198833e-16, 0.0))
        self.assertEqual(pt('{-.25, +2.5E+2}'), (-.25, 250.0))
        self.assertEqual(pt('{0, 1}'), (0.0, 1.0))
        self.assertEqual(pt(None), (0.0, 0.0))
        extractor = Extractor.__new__(Extractor)
        extractor.shared = {}
        gradient = {'from': '{1.722546424198833e-16, 0}', 'to': '{1, 1}',
                    'stops': [{'color': dict(red=1, green=0, blue=0)}]}
        style = extractor.style_of({'style': {'fills': [dict(isEnabled=True, fillType=1, gradient=gradient)]}})
        self.assertAlmostEqual(style['gradient']['from'][0], 0, delta=1e-15)
        self.assertEqual(style['gradient']['from'][1], 0)

    def test_embedded_font_refresh_keeps_every_source_weight(self):
        import sketch_fonts
        for weight,style in sketch_fonts.STYLES.items():
            source=f'weight: {weight} font_src: "self:resources/atro/Montserrat.ttf"'
            family='Montserrat-'+style
            updated=sketch_fonts.refresh_design(source)
            self.assertIn(f'weight: {weight} ',updated)
            self.assertIn(sketch_native.font_properties(family)['font_src'],updated)
            self.assertEqual(sketch_fonts.refresh_design(updated),updated)
        with self.assertRaisesRegex(ValueError,'input padding'):
            sketch_fonts.refresh_design('weight: 400 font_src: "self:resources/atro/Montserrat.ttf" padleft: 15')

    def test_overlay_graphic_preserves_native_text_and_handles_border_blending(self):
        graphic={'_class':'group','style':{'contextSettings':{'blendMode':7}},'layers':[{'_class':'shapePath'}]}
        self.assertTrue(graphics.overlay_graphic(graphic))
        graphic['layers'].append({'_class':'text'})
        self.assertFalse(graphics.overlay_graphic(graphic))
        border={'_class':'rectangle','style':{'borders':[{'isEnabled':True,'contextSettings':{'blendMode':7}}]}}
        self.assertTrue(graphics.overlay_graphic(border))

    def test_overlay_svg_stroke_uses_covering_glass_tint_without_claiming_solid_bounds(self):
        glass=dict(t='stack',id='glass',variant='glass_surface',x=0,y=0,w=100,h=100,bg=0x80140f26,blur=10)
        icon=dict(t='svg',id='icon',variant='glass_svg',value=1,x=20,y=20,w=40,h=40,blur=0)
        following=dict(t='svg',id='following',variant='glass_svg',value=1,x=25,y=25,w=30,h=30,blur=0)
        findings=sketch_native.compose_glass_materials(dict(c=[glass,icon,following]))
        self.assertEqual(icon['color'],0x80140f26)
        self.assertEqual(icon['blur'],10)
        self.assertEqual(findings['following']['covering_widget_id'],'glass')

    def test_foreground_photo_backdrop_has_an_explicit_individual_effect_fallback(self):
        box=dict(x=0,y=0,w=100,h=100)
        blur={'style':{'blurs':[{'isEnabled':True,'type':3}]}}
        bg=dict(object_id='bg',**box)
        photo=dict(object_id='photo',x=10,y=10,w=80,h=80,image='source.jpg')
        toast=dict(object_id='toast',x=20,y=50,w=60,h=20)
        root=dict(object_id='root',children=[bg,photo,toast],**box)
        sketch_native.annotate_overlay_backdrops(root,{'root':{},'bg':blur,'photo':{},'toast':blur})
        self.assertEqual(toast['foreground_backdrop_source_id'],'photo')
        self.assertIn('Gauss scene excludes',toast['backdrop_fallback'])
        self.assertNotIn('backdrop_fallback',bg)
        overlay={'_class':'rectangle','style':{'fills':[{'isEnabled':True,'contextSettings':{'blendMode':7}}]}}
        toast.pop('backdrop_fallback');toast.pop('foreground_backdrop_source_id')
        sketch_native.annotate_overlay_backdrops(root,{'root':{},'bg':blur,'photo':{},'toast':overlay})
        self.assertEqual(toast['foreground_backdrop_source_id'],'photo')

    def test_sketch_wide_card_gradient_matches_source_pixel_projection(self):
        svg='<svg><defs><linearGradient id="g" x1="26.1061276%" y1="42.3499932%" x2="47.7376163%" y2="57.1432966%"><stop stop-color="#B293FF"/><stop stop-color="#7C58D6"/></linearGradient></defs><rect width="580" height="180" fill="url(#g)"/></svg>'
        source=dict(w=580,h=180,gradient={'type':0,'from':[.261061275601882,-.294278487469121],
            'to':[.477376162703044,1.2416682071669],'stops':[{'c':{'hex':'#b293ff'}},{'c':{'hex':'#7c58d6'}}]})
        result,proof=graphics.source_linear_gradient(svg,source)
        self.assertEqual(proof['method'],'Sketch point-space linear gradient')
        g=ET.fromstring(result).find('defs/linearGradient')
        x,y=float(g.get('x1')),float(g.get('y1'));dx,dy=float(g.get('x2'))-x,float(g.get('y2'))-y
        # Least-squares measurement of the authoritative PNG yielded these
        # coefficients; allow 8-bit channel quantization, not a narrow band.
        norm=dx*dx+dy*dy
        self.assertAlmostEqual(dx/(norm*580),.00136792,delta=.00001)
        self.assertAlmostEqual(dy/(norm*180),.00301441,delta=.00002)

    def test_emoji_baseline_offset_does_not_create_a_multiline_input(self):
        spans=[{'size':25,'y':24},{'size':25,'y':25.7}]
        self.assertEqual(sketch_native.text_row_baselines(spans),[24])
        self.assertEqual(sketch_native.measured_line_height(spans,20),20)
        spans.append({'size':25,'y':69})
        self.assertEqual(sketch_native.text_row_baselines(spans),[24,69])
        self.assertEqual(sketch_native.measured_line_height(spans,20),45)

    def test_fill_profile_uses_the_same_white_matte_as_visual_review(self):
        import gate_fill
        import numpy as np
        from PIL import Image,ImageDraw
        with tempfile.TemporaryDirectory() as td:
            source=Image.new('RGBA',(120,300),(0,0,0,0))
            ImageDraw.Draw(source).rectangle((10,100,110,200),fill=(80,100,200,255))
            target=pathlib.Path(td)/'target.png';native=pathlib.Path(td)/'native.png'
            source.save(target)
            Image.alpha_composite(Image.new('RGBA',source.size,'white'),source).save(native)
            np.testing.assert_array_equal(gate_fill._mask(target),gate_fill._mask(native))

    def test_alpha_mask_keeps_coverage_while_outline_mask_drops_its_paint(self):
        style={'fills':[{'gradient':{'stops':[{'alpha':0},{'alpha':1}]}}]}
        alpha={'clippingMaskMode':1,'style':style}
        self.assertEqual(sketch_assets.clipping_style(alpha),style)
        self.assertEqual(sketch_assets.clipping_style({'clippingMaskMode':0,'style':style})['fills'],[])
        sketch_assets.clipping_style(alpha)['fills'].clear()
        self.assertTrue(style['fills'])

    def test_unused_svg_definitions_do_not_become_empty_native_geometry(self):
        with tempfile.TemporaryDirectory() as td:
            path=pathlib.Path(td)/'empty.svg'
            path.write_text('<svg><defs><rect id="unused" width="10" height="10"/></defs><g/></svg>')
            self.assertEqual(graphics.vector_asset(path),('',None))
            path.write_text('<svg><g><path d="" stroke="#000"/></g></svg>')
            self.assertEqual(graphics.vector_asset(path),('',None))
            path.write_text('<svg><g fill="none" stroke="none"><polygon points="0 0 10 0 10 10"/></g></svg>')
            self.assertEqual(graphics.vector_asset(path),('',None))
            path.write_text('<svg><g fill="none" stroke="none"><polygon fill="#fff" points="0 0 10 0 10 10"/></g></svg>')
            self.assertTrue(graphics.vector_asset(path)[0])

    def test_rotated_phone_highlight_intersects_artboard(self):
        x,y,w,h=sketch_native.rotated_bounds(-28.64,904.2,20.4,312,93)
        self.assertGreater(x+w,0)
        self.assertGreater(w,300)

    def test_reflected_group_mirrors_each_leaf_in_rotated_parent_axes(self):
        child=dict(object_id='leaf',x=10,y=20,w=10,h=10)
        root=dict(x=0,y=0,w=100,h=100,rot=90,flip_x=True,children=[child])
        sketch_native.apply_group_rotations(root)
        self.assertAlmostEqual(child['x'],70)
        self.assertAlmostEqual(child['y'],80)
        self.assertEqual(child['rot'],90)
        self.assertTrue(child['flip_x'])
        self.assertTrue(child['ancestor_transform'])

    def test_rotated_reflected_bell_keeps_clapper_on_source_right(self):
        clapper=dict(x=21.8,y=38.5,w=5.4,h=1.5)
        root=dict(x=0,y=0,w=48,h=48,rot=-270,flip_y=True,children=[clapper])
        sketch_native.apply_group_rotations(root)
        self.assertGreater(clapper['x'],35)
        self.assertEqual(clapper['rot'],-90)
        self.assertTrue(clapper['flip_x'])

    def test_rotated_parent_mask_keeps_its_transformed_orientation(self):
        mask=dict(object_id='mask',x=10,y=20,w=60,h=70,mask=True)
        leaf=dict(object_id='leaf',x=20,y=30,w=20,h=20)
        root=dict(object_id='root',x=0,y=0,w=100,h=100,rot=10,children=[mask,leaf])
        sketch_native.apply_group_rotations(root)
        sketch_native.annotate_graphic_masks(root,{'root':{},'mask':{},'leaf':{}})
        self.assertEqual(leaf['graphic_masks'][0]['rot'],10)
        graphics.active_masks(leaf,{'mask':{'_class':'rectangle'}})
        self.assertEqual(leaf['export_graphic_masks'],leaf['graphic_masks'])

    def test_keyboard_keys_compose_the_covering_native_glass_tint(self):
        background=dict(t='stack',id='keyboard',variant='glass_surface',x=0,y=100,w=750,h=490,bg=0x80140f26,blur=10)
        key=dict(t='stack',id='key',variant='glass_surface',x=5,y=120,w=64,h=85,bg=0x80140f26,blur=10)
        outside=dict(key,id='outside',x=800)
        findings=sketch_native.compose_glass_materials(dict(t='stack',c=[background,key,outside]))
        self.assertEqual(key['bg'],0xc0140f26)
        self.assertAlmostEqual(key['blur'],200**.5)
        self.assertEqual(outside['bg'],0x80140f26)
        self.assertEqual(findings['key']['covering_widget_id'],'keyboard')

    def test_fullscreen_glass_preserves_photo_scene_and_foreground_order(self):
        box=dict(x=0,y=0,w=750,h=1624)
        photo=dict(t='image',id='photo',**box)
        glass=dict(t='stack',id='blur',variant='glass_surface',**box)
        background=dict(t='stack',id='background',variant='glass_group',c=[photo,glass],**box)
        title=dict(t='text',id='title',x=20,y=40,w=200,h=30,text='Title')
        root=dict(t='stack',id='root',c=[background,title],**box)
        self.assertEqual(sketch_native.route_fullscreen_glass(root),['title'])
        self.assertNotIn('variant',background)
        self.assertIs(background['c'][0],photo)
        self.assertEqual(root['c'][1]['variant'],'glass_group')
        self.assertIs(root['c'][1]['c'][0],title)

    def test_keyboard_glass_outside_artboard_composes_visible_background(self):
        background=dict(t='stack',id='background',variant='glass_surface',x=0,y=0,w=750,h=1624,bg=0x80140f26,blur=10)
        keyboard=dict(t='stack',id='keyboard',variant='glass_surface',x=0,y=1133,w=750,h=492,bg=0x80140f26,blur=10)
        key=dict(t='stack',id='key',variant='glass_surface',x=5,y=1200,w=65,h=85,bg=0x80140f26,blur=10)
        findings=sketch_native.compose_glass_materials(dict(x=0,y=0,w=750,h=1624,c=[background,keyboard,key]))
        self.assertEqual(keyboard['bg'],0xc0140f26)
        self.assertEqual(key['bg'],0xe0140f26)
        self.assertEqual(findings['keyboard']['covering_widget_id'],'background')

    def test_padded_fullscreen_svg_keeps_preceding_photo_in_scene(self):
        box=dict(x=0,y=0,w=750,h=1624)
        photo=dict(t='image',id='photo',**box)
        paint=dict(t='svg',id='paint',variant='glass_svg',x=-20,y=-20,w=790,h=1664)
        glass=dict(t='stack',id='glass',variant='glass_group',c=[paint],**box)
        title=dict(t='text',id='title',x=20,y=40,w=200,h=30,text='Title')
        viewfinder=dict(t='stack',id='viewfinder',variant='glass_group',c=[photo,glass,title],**box)
        root=dict(t='stack',id='root',c=[viewfinder],**box)
        self.assertEqual(sketch_native.route_fullscreen_glass(root),['title'])
        self.assertNotIn('variant',viewfinder)
        self.assertIs(viewfinder['c'][0],photo)
        self.assertEqual(glass['variant'],'glass_group')

    def test_shadow_deferred_by_glass_also_routes_its_later_foreground(self):
        glass=dict(t='stack',id='glass',variant='glass_surface',x=20,y=100,w=40,h=20)
        shadow=dict(t='image',id='shadow',x=0,y=60,w=100,h=80)
        label=dict(t='text',id='label',text='SIZE',x=20,y=70,w=40,h=15)
        unrelated=dict(t='image',id='photo',x=200,y=20,w=100,h=100)
        root=dict(t='stack',id='root',x=0,y=0,w=375,h=812,c=[glass,shadow,label,unrelated])
        self.assertEqual(sketch_native.route_glass_foreground(root),['shadow','label'])
        self.assertIs(root['c'][2]['c'][0],label)
        self.assertIs(root['c'][3],unrelated)

    def test_vector_glass_material_requires_source_alpha_coverage(self):
        from PIL import Image
        with tempfile.TemporaryDirectory() as tmp:
            path=pathlib.Path(tmp)/'coverage.png'
            im=Image.new('RGBA',(100,100));im.paste((20,15,38,128),(0,0,50,100));im.save(path)
            glass=dict(t='svg',id='glass',variant='glass_svg',x=0,y=0,w=100,h=100,blur=10)
            covered=dict(t='stack',id='covered',variant='glass_overlay',x=10,y=10,w=30,h=30,bg=0x80ffffff,blur=5)
            hole=dict(t='stack',id='hole',variant='glass_overlay',x=60,y=10,w=30,h=30,bg=0x80ffffff,blur=5)
            findings=sketch_native.compose_glass_materials(dict(c=[glass,covered,hole]),
                {'glass':{'color':0x80140f26,'coverage':path}})
            self.assertEqual(covered['color'],0x80140f26)
            self.assertNotIn('color',hole)
            self.assertEqual(findings['covered']['covering_widget_id'],'glass')

    def test_later_home_indicator_stays_above_keyboard_glass(self):
        keyboard=dict(t='stack',id='keyboard',variant='glass_group',x=0,y=600,w=375,h=212,c=[
            dict(t='stack',id='glass',variant='glass_surface',x=0,y=600,w=375,h=212)])
        home=dict(t='stack',id='home',variant='surface',x=130,y=790,w=100,h=4)
        photo=dict(t='image',id='photo',x=0,y=0,w=100,h=100)
        root=dict(t='stack',id='root',x=0,y=0,w=375,h=812,c=[keyboard,home,photo])
        self.assertEqual(sketch_native.route_glass_foreground(root),['home'])
        self.assertIs(root['c'][1]['c'][0],home)
        self.assertIs(root['c'][2],photo)

    def test_overlay_blend_uses_preceding_glass_material_in_native_shader(self):
        box=dict(x=0,y=0,w=100,h=100)
        background=dict(t='stack',id='background',variant='glass_surface',bg=0x80140f26,blur=10,**box)
        button=dict(t='stack',id='button',variant='glass_overlay',bg=0x80ffffff,blur=5,**box)
        result=sketch_native.compose_glass_materials(dict(c=[background,button]))
        self.assertEqual(button['color'],0x80140f26)
        self.assertEqual(button['bg'],0x80ffffff)
        self.assertIn('native Overlay',result['button']['method'])

    def test_nested_tooltip_foreground_stays_in_its_glass_group(self):
        box=dict(x=20,y=30,w=100,h=50)
        glass=dict(t='stack',variant='glass_group',**box)
        inner=dict(t='stack',c=[glass],**box)
        outer=dict(t='stack',c=[inner,dict(t='text',text='Copy',x=30,y=40,w=30,h=20)],**box)
        root=dict(t='stack',x=0,y=0,w=375,h=812,c=[outer])
        sketch_native.promote_glass_groups(root)
        self.assertEqual(outer['variant'],'glass_group')
        self.assertEqual(inner['variant'],'glass_group')
        self.assertNotIn('variant',root)

    def test_keyboard_background_can_extend_one_source_pixel_beyond_symbol(self):
        keyboard=dict(t='stack',x=0,y=1133,w=750,h=490,c=[
            dict(t='stack',variant='glass_surface',x=0,y=1133,w=750,h=491.1),
            dict(t='stack',x=5,y=1153.5,w=740,h=455.8)])
        root=dict(t='stack',c=[keyboard])
        sketch_native.promote_glass_groups(root)
        self.assertEqual(keyboard['variant'],'glass_group')
        self.assertNotIn('variant',root)

    def test_native_button_hit_padding_does_not_put_digits_behind_glass(self):
        button=dict(t='stack',x=90,y=543,w=170,h=170,c=[
            dict(t='stack',variant='glass_surface',x=94.2,y=547.2,w=161.5,h=161.5),
            dict(t='text',text='2',x=150,y=600,w=50,h=50),
            dict(t='button',x=90,y=543,w=170,h=170)])
        root=dict(t='stack',c=[button])
        sketch_native.promote_glass_groups(root)
        self.assertEqual(button['variant'],'glass_group')
        self.assertNotIn('variant',root)

    def test_measured_baselines_replace_font_height_estimate(self):
        self.assertEqual(sketch_native.measured_line_height([
            dict(y=39,size=40),dict(y=88,size=40)],52),49)
        self.assertEqual(sketch_native.measured_line_height([
            dict(y=19,size=22),dict(y=19.7,size=20)],26),26)

    def test_fixed_text_box_clips_hidden_paragraph_without_truncating_content(self):
        spans=[dict(y=19),dict(y=47),dict(y=75)]
        raw=dict(verticalSizing=3,frame=dict(height=60))
        self.assertTrue(sketch_native.fixed_text_overflows(raw,spans))
        self.assertFalse(sketch_native.fixed_text_overflows(raw,spans[:2]))
        self.assertFalse(sketch_native.fixed_text_overflows(dict(raw,verticalSizing=1),spans))
        self.assertTrue(sketch_native.fixed_text_overflows(dict(raw,verticalSizing=0),spans))
        self.assertFalse(sketch_native.fixed_text_overflows(raw,[dict(y=75,size=80)]))

    def test_isolated_export_preserves_referenced_images_and_excludes_other_pages(self):
        with tempfile.TemporaryDirectory() as td:
            source=pathlib.Path(td)/'source.sketch';out=pathlib.Path(td)/'export.sketch'
            with zipfile.ZipFile(source,'w') as z:
                z.writestr('document.json',json.dumps({'pages':[{'_ref':'pages/a'},{'_ref':'pages/b'}]}))
                for name,data in [('pages/a.json','{}'),('pages/b.json','{}'),('images/needed', 'keep'),('images/unused','omit')]:z.writestr(name,data)
            page={'layers':[{'image':{'_ref':'images/needed'}}]}
            sketch_assets.isolated_document(source,out,'pages/a.json',page)
            with zipfile.ZipFile(out) as z:
                self.assertEqual(z.read('images/needed'),b'keep')
                self.assertNotIn('images/unused',z.namelist())
                self.assertNotIn('pages/b.json',z.namelist())
                self.assertEqual(json.loads(z.read('pages/a.json')),page)

    def test_backdrop_prefix_does_not_include_later_content_or_mutate_source(self):
        source={'do_objectID':'root','layers':[{'do_objectID':'photo'},
            {'do_objectID':'group','layers':[{'do_objectID':'blend'},{'do_objectID':'text'}]},
            {'do_objectID':'button'}]}
        prefix,found=sketch_assets.backdrop_prefix(source,'blend')
        self.assertTrue(found)
        self.assertEqual([c['do_objectID'] for c in prefix['layers']],['photo','group'])
        self.assertEqual(prefix['layers'][1]['layers'],[{'do_objectID':'blend'}])
        self.assertEqual(len(source['layers']),3)

    def test_backdrop_blend_is_not_silently_treated_as_normal_svg_fill(self):
        svg,reason=self.vector('<rect width="80" height="60" style="mix-blend-mode: overlay;"/>')
        self.assertIsNone(svg)
        self.assertIn('backdrop blend mode',reason)
    def vector(self, body):
        with tempfile.TemporaryDirectory() as td:
            path=pathlib.Path(td)/'source.svg'
            path.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="80" height="60">'+body+'</svg>')
            return graphics.vector_asset(path)

    def test_vector_uses_preserve_canvas_and_transforms(self):
        svg,reason=self.vector('<defs><path id="shape" d="M0 0L10 0L0 10Z"/></defs>'
            '<g transform="translate(8 12)"><use href="#shape" fill="#123456"/></g>')
        root=ET.fromstring(svg)
        self.assertIsNone(reason)
        self.assertEqual((root.get('width'),root.get('height')),('80','60'))
        self.assertEqual(len(list(root.iter('path'))),1)
        self.assertIn('translate(8 12)',svg)
        self.assertIn('#123456',svg)
        self.assertNotIn('<use',svg)

    def test_empty_graphic_does_not_wait_for_nonexistent_geometry(self):
        self.assertEqual(self.vector('<g transform="translate(8 8)"/>'),('',None))

    def test_single_shape_group_shadow_is_transferred_without_disappearing(self):
        svg,reason=self.vector('<defs><filter id="shadow"><feDropShadow stdDeviation="14.5"/></filter></defs>'
            '<g filter="url(#shadow)"><rect width="100" height="20"/></g>')
        self.assertIsNone(reason)
        root=ET.fromstring(svg)
        self.assertEqual(next(root.iter('rect')).get('filter'),'url(#shadow)')
        self.assertTrue(all(not g.get('filter') for g in root.iter('g')))
        svg,reason=self.vector('<g filter="url(#shadow)"><rect width="100" height="20"/>'
                              '<circle cx="10" cy="10" r="10"/></g>')
        self.assertIsNone(svg)
        self.assertIn('multiple shapes',reason)

    def test_mask_and_unknown_filter_fail_with_reason(self):
        svg,reason=self.vector('<defs><mask id="clip"><rect width="10" height="10"/></mask></defs>'
                              '<rect width="30" height="30" mask="url(#clip)"/>')
        self.assertIsNone(svg)
        self.assertIn('mask',reason)
        svg,reason=self.vector('<filter id="fx"><feTurbulence/></filter><path d="M0 0L10 0L0 10Z"/>')
        self.assertIsNone(svg)
        self.assertIn('feTurbulence',reason)

    def test_redundant_outline_mask_is_proven_before_removal(self):
        mask=dict(object_id='mask',x=0,y=0,w=100,h=100)
        raw={'mask':{'_class':'rectangle','fixedRadius':20}}
        interior=dict(x=30,y=30,w=40,h=40,graphic_masks=[mask])
        graphics.active_masks(interior,raw)
        self.assertEqual(interior['export_graphic_masks'],[])
        self.assertEqual(interior['graphic_masks'],[mask])
        corner=dict(x=1,y=1,w=8,h=8,graphic_masks=[mask])
        graphics.active_masks(corner,raw)
        self.assertEqual(corner['export_graphic_masks'],[mask])

    def test_shape_uses_native_properties_and_outside_stroke_uses_vector(self):
        node=dict(cls='rectangle',fill={'hex':'#123456','a':1},radius=12,opacity=.5)
        raw={'style':{'fills':[{'isEnabled':True}]},'points':[{'cornerRadius':12,'point':p} for p in ('{0,0}','{1,0}','{1,1}','{0,1}') ]}
        surface=graphics.surface(node,raw)
        self.assertEqual(surface['bg'],0x80123456)
        self.assertEqual(surface['radius'],12)
        raw['style']['borders']=[{'isEnabled':True,'position':2}]
        node['stroke']={'w':2,'c':{'hex':'#000000','a':1}}
        self.assertIsNone(graphics.surface(node,raw))

    def test_edited_rectangle_diamond_retains_native_vector_geometry(self):
        node=dict(cls='rectangle',fill={'hex':'#123456','a':1})
        raw={'style':{'fills':[{'isEnabled':True}]},'points':[{'point':p} for p in ('{0.5,0}','{1,0.5}','{0.5,1}','{0,0.5}') ]}
        self.assertIsNone(graphics.surface(node,raw))

    def test_backdrop_overlay_uses_native_glass_instead_of_plain_white_fill(self):
        node=dict(cls='rectangle',w=140,h=64,fill={'hex':'#ffffff','a':.5},radius=32)
        raw={'style':{'blurs':[{'isEnabled':True,'type':3,'radius':22.5}],
             'fills':[{'isEnabled':True,'contextSettings':{'blendMode':7}}]}}
        result=graphics.surface(node,raw)
        self.assertEqual((result['variant'],result['blur'],result['bg']),('glass_overlay',22.5,0x80ffffff))

    def test_paragraph_boundaries_are_retained_without_changing_span_positions(self):
        with tempfile.TemporaryDirectory() as td:
            path=pathlib.Path(td)/'text.svg'
            path.write_text('<svg xmlns="http://www.w3.org/2000/svg"><text '
                'font-family="Montserrat-Regular" font-size="20">'
                '<tspan x="0" y="20">Capital.</tspan><tspan x="0" y="100">Parallax</tspan></text></svg>')
            spans=sketch_native.text_spans(path,source_text='Capital.\n\nParallax')
            self.assertEqual(''.join(s['text'] for s in spans),'Capital. Parallax')
            self.assertEqual(spans[1]['y'],100)
            with self.assertRaisesRegex(ValueError,'changed source content'):
                sketch_native.text_spans(path,source_text='Capital. Different')

    def test_scale_preserves_em_metrics_and_actual_image_pixels(self):
        node=dict(x=20,y=30,w=100,h=60,size=24,tracking=2,font_asc=.1,font_desc=.2,
                  image_width=200,image_height=120,c=[dict(x=20,y=30,w=10,h=10)])
        sketch_native.scale_design(node,2)
        self.assertEqual((node['size'],node['tracking'],node['font_asc']),(12,1,.1))
        self.assertEqual((node['image_width'],node['image_height']),(200,120))
        self.assertEqual(node['c'][0]['w'],5)

    def test_rotated_label_measurement_recovers_unrotated_baseline(self):
        with tempfile.TemporaryDirectory() as td:
            path=pathlib.Path(td)/'text.svg'
            path.write_text('<svg xmlns="http://www.w3.org/2000/svg"><g transform="translate(-489, 0)" '
                'font-family="Montserrat-Medium" font-size="18" opacity="0.6" letter-spacing="3">'
                '<text transform="translate(500.5, 26) rotate(-90) translate(-500.5, -26)">'
                '<tspan x="480.244" y="32">JAN</tspan></text></g></svg>')
            spans=sketch_native.text_spans(path,(51,22))
            self.assertAlmostEqual(spans[0]['x'],5.244)
            self.assertEqual((spans[0]['y'],spans[0]['tracking'],spans[0]['opacity']),(17,3,.6))

    def test_rotated_group_keeps_native_text_baseline_and_transforms_placement(self):
        with tempfile.TemporaryDirectory() as td:
            path=pathlib.Path(td)/'text.svg'
            path.write_text('<svg xmlns="http://www.w3.org/2000/svg"><g '
                'transform="translate(661, 812) rotate(-90) translate(-661, -812)translate(-151, 723)">'
                '<text font-family="Montserrat-Medium" font-size="25">'
                '<tspan x="491" y="126">Places</tspan></text></g></svg>')
            spans=sketch_native.text_spans(path,source_frame={'x':491,'y':102})
            self.assertEqual((spans[0]['x'],spans[0]['y']),(0,24))
        child=dict(x=340,y=825,w=83,h=20)
        root=dict(x=-151,y=723,w=1624,h=178,rot=90,children=[child])
        sketch_native.apply_group_rotations(root)
        self.assertEqual(child['rot'],90)
        self.assertAlmostEqual(child['x'],642.5)
        self.assertAlmostEqual(child['y'],1081.5)


if __name__=='__main__': unittest.main()
