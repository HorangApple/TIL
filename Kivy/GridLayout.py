from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

GridLayout:
    cols:2
#    size_hint_x:None
#    size_hint_y:None

    Button:
        text:'hello'
        size_hint_x:None
        width:200
    Button:
        text:'world'
        size_hint_x:None
        width:100


'''))