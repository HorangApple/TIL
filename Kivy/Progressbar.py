from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
BoxLayout:
    padding:30
    ProgressBar:
        id:bar
        max:10000
        value:5000
'''))