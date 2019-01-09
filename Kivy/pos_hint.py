from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""

FloatLayout:
    Button:
        text: 'B1'
        size_hint: 0.2, 0.2
        pos_hint: {'top': 0.5, 'right': 0.5}
"""))