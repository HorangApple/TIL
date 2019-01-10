from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

RelativeLayout:
    Button:
        text:'R1'
        size_hint:.3,.3
        pos: 250,100
    Button:
        text:'R2'
        size_hint:.2,.2
        pos_hint:{'x':0.3,'y':0}


'''))