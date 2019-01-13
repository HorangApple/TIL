from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

Label:
    Button:
        text:'Hello'
        pos:root.x,root.top - self.height
    Button:
        text:'World!'
        pos:root.right-200,root.y
'''))