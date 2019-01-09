from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""

BoxLayout:
    Button:
        text: 'B1'
        size_hint_x : 0.5
    Button:
        text: 'B1'
        size_hint_x : 1
    Button:
        text: 'B1'
        size_hint_x : 0.5

"""))