from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

StackLayout:
    orientation: 'lr-tb' # left to right, top to bottom
    padding : 20
    spacing : 10
    Button:
        text:'B1'
        size_hint:.2,.1
    Button:
        text:'B2'
        size_hint:.2,.1
    Button:
        text:'B3'
        size_hint:.2,.1
    Button:
        text:'B4'
        size_hint:.2,.1
    Button:
        text:'B5'
        size_hint:.2,.1
    Button:
        text:'B6'
        size_hint:.2,.1
'''))