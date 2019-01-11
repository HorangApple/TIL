from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

Label:
    Button:
        text:'B1'
        font_size:32
        color:.8,.9,0,1
        size:100,200 # layout을 사용하게 된다면 size_hint 사용
        pos:50,100
    Button:
        text:'B2'
        font_size:32
        color:.8,.1,0,1
        size:100,200
        pos:150,150
'''))