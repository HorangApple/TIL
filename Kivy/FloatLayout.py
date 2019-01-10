from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

<Button>:
    color:.8,.2,0,1
    font_size: 50
    size_hint:.3,.2
FloatLayout:
    Button:
        text: 'Hello'
        pos_hint:{'x':0,'top':0.5}
    Button:
        text: 'world'
        pos_hint:{'right':0.5,'y':0}


'''))