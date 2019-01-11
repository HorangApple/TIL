from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

PageLayout:
    Button:
        text:'B1'
    Button:
        text:'B2'
    Button:
        text:'B3'
'''))