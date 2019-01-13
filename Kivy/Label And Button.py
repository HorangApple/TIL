from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    size_hint_y:None
    height:sp(300) #Label과 Button이 차지하는 높이 설정
    Label:
        text:'Hello'
    Button:
        text:'World'
'''))