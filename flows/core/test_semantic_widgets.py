import sys as _sys, pathlib as _pathlib
_sys.path.insert(0, str(_pathlib.Path(__file__).resolve().parents[1]))  # flows/, for `core`
import json
import unittest

from core import semantic_widgets as semantic


def fixture(node):
    owners={}
    for _,n in semantic.walk(node):
        owners[n['id']]={'native_widget_id':n['id'],'object_id':n['id'],
            'name':n.pop('source_name',n['id'])}
    return owners


class SemanticWidgetTests(unittest.TestCase):
    def test_track_row_has_distinct_native_activation_and_icon_action(self):
        tree={'t':'stack','id':'track','source_name':'UI Elements/Music/List',
            'x':24,'y':200,'w':327,'h':64,'c':[
                {'t':'text','id':'title','text':'Stay','size':18},
                {'t':'text','id':'artist','text':'The Kid LAROI','size':12},
                {'t':'stack','id':'more','source_name':'Icons/More','x':327,'y':220,'w':24,'h':24,
                 'c':[{'t':'svg','id':'icon','src':'more.svg'}]}]}
        owners=fixture(tree);boundaries,added=semantic.annotate(tree,owners,'camo')
        self.assertEqual(set(added),{'track_kit_button','more_kit_button'})
        config=boundaries['track']['config']
        for path,expected in [(config['bindings']['control'],'track_kit_button'),
                              (config['action_bindings']['more'],'more_kit_button')]:
            n=tree
            for i in path:n=n['c'][i]
            self.assertEqual(n['id'],expected)
            self.assertEqual(n['t'],'button')
        props=semantic.parameters(tree,config)
        self.assertEqual(props[('title','text')],'title')
        self.assertEqual(props[('artist','text')],'artist')

    def test_background_remnant_is_not_misrepresented_as_a_complete_card(self):
        tree={'t':'stack','id':'card','source_name':'Project Card','c':[
            {'t':'image','id':'paint','src':'background.png'}]}
        boundaries,_=semantic.annotate(tree,fixture(tree),'taskplan')
        self.assertFalse(boundaries)

    def test_nested_tab_symbols_get_one_native_control_per_item(self):
        def tab(i):
            return {'t':'stack','id':f'outer{i}','x':i*70,'y':700,'w':70,'h':50,
                'source_name':'Bar/Bottom/navTab-item','c':[
                    {'t':'stack','id':f'inner{i}','source_name':'Bar/Bottom/navTab-item','c':[]}]}
        nav={'t':'stack','id':'nav','c':[tab(0),tab(1),tab(2)]}
        tree={'t':'stack','id':'screen','c':[{'t':'stack','id':'body','c':[]},nav]}
        owners=fixture(tree);boundaries,added=semantic.annotate(tree,owners,'atro')
        self.assertEqual(set(boundaries),{'nav'})
        self.assertEqual(set(added),{f'outer{i}_kit_radio' for i in range(3)})
        config=json.loads(nav['kit'])
        self.assertEqual(config['widget'],'KitTabBar')
        self.assertEqual(len(config['items']),3)
        for item in config['items']:
            node=nav
            for i in item['control']:node=node['c'][i]
            self.assertEqual(node['t'],'radio')
            self.assertEqual(node['variant'],'silent')
        self.assertEqual(semantic.parameters(nav,config)[('nav','kit_index')],'selected_index')

    def test_complete_field_owns_label_and_input_with_one_public_identity(self):
        tree={'t':'stack','id':'field','source_name':'input=Default','c':[
            {'t':'text','id':'label','text':'Email'},
            {'t':'stack','id':'inner','source_name':'Input with label','c':[
                {'t':'input','id':'value','text':'a@example.test','placeholder':'Email','enabled':1}]}]}
        boundaries,added=semantic.annotate(tree,fixture(tree),'taskplan')
        self.assertEqual(set(boundaries),{'field'})
        self.assertFalse(added)
        config=json.loads(tree['kit'])
        self.assertEqual(config['bindings']['input'],[1,0])
        props=semantic.parameters(tree,config)
        self.assertEqual(props[('label','text')],'label')
        self.assertEqual(props[('value','text')],'value')

    def test_separate_bars_do_not_turn_entire_page_into_navigation(self):
        def bar(name,y):
            return {'t':'stack','id':name,'c':[
                {'t':'stack','id':f'{name}{i}','source_name':'Navigation/Tab/Pill',
                 'x':i*50,'y':y,'w':50,'h':40,'c':[]} for i in range(2)]}
        tree={'t':'stack','id':'screen','c':[bar('top',50),bar('bottom',700)]}
        boundaries,_=semantic.annotate(tree,fixture(tree),'atro')
        self.assertEqual(set(boundaries),{'top','bottom'})

    def test_disabled_tab_does_not_define_normal_inactive_paint(self):
        def tab(i,enabled,selected,color,bg):
            return {'t':'stack','id':f'tab{i}','source_name':'Tab Field',
                'x':i*70,'y':100,'w':60,'h':35,'selected':selected,'c':[
                    {'t':'stack','id':f'paint{i}','variant':'surface','w':60,'h':35,'bg':bg},
                    {'t':'text','id':f'text{i}','text':str(i),'color':color},
                    {'t':'radio','id':f'control{i}','enabled':enabled,'on':selected}]}
        tree={'t':'stack','id':'bar','c':[
            tab(0,0,0,0xff9da3ae,0xfff3f4f6),
            tab(1,1,1,0xffffffff,0xff1f2a37),
            tab(2,1,0,0xff4d5761,0xffeeeff2)]}
        boundaries,_=semantic.annotate(tree,fixture(tree),'taskplan')
        config=boundaries['bar']['config']
        self.assertEqual(config['inactive_color'],0xff4d5761)
        self.assertEqual(config['inactive_surface'],0xffeeeff2)
        self.assertFalse(config['items'][0]['source_enabled'])

    def test_added_native_radios_start_with_the_inferred_source_selection(self):
        tree={'t':'stack','id':'bar','c':[
            {'t':'stack','id':f'tab{i}','source_name':'Bar/Bottom/navTab-item',
             'x':i*70,'y':100,'w':60,'h':35,'c':[
                 {'t':'text','id':f'label{i}','text':'Item','color':color}]}
            for i,color in enumerate((0xff999999,0xffffffff,0xff999999))]}
        boundaries,added=semantic.annotate(tree,fixture(tree),'atro')
        config=boundaries['bar']['config']
        self.assertEqual(config['selected_index'],1)
        self.assertEqual([tab['c'][-1]['on'] for tab in tree['c']],[0,1,0])

    def test_underlines_are_state_parts_and_elevation_is_not_background(self):
        tree={'t':'stack','id':'bar','c':[]}
        for i in range(3):
            tree['c'].append({'t':'stack','id':f'tab{i}','source_name':'Navigation/Tab/Sharp',
                'x':i*70,'y':100,'w':70,'h':50,'c':[
                    {'t':'stack','id':f'elevation{i}','source_name':'Elevation','variant':'surface','bg':0,'w':70,'h':50},
                    {'t':'stack','id':f'background{i}','source_name':'background','variant':'surface','bg':0,'w':70,'h':50},
                    {'t':'stack','id':f'line{i}','source_name':'underline','variant':'surface','bg':0xff121212 if i==1 else 0xffeeeeee,'w':70,'h':1.5},
                    {'t':'text','id':f'label{i}','text':'Tab','color':0xff121212 if i==1 else 0xff999999}]})
        boundaries,_=semantic.annotate(tree,fixture(tree),'atro');config=boundaries['bar']['config']
        self.assertEqual(config['active_indicator'],0xff121212)
        self.assertEqual(config['inactive_indicator'],0xffeeeeee)
        self.assertEqual([i['indicators'] for i in config['items']],[[[0,2]],[[1,2]],[[2,2]]])
        self.assertEqual([i['surfaces'] for i in config['items']],[[[0,1]],[[1,1]],[[2,1]]])


if __name__=='__main__':unittest.main()
