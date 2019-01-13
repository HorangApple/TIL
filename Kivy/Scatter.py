from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
FloatLayout:
    Scatter:
        size:100, 100
        pos:100, 100
        do_rotation:False # default는 True
        Label:
            text:"something"
'''))