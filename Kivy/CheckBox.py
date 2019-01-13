from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

GridLayout:
    cols:2
    CheckBox:
        active:True # 따로 설정 안하면 default는 False
    Label:
        text:"checkbox"
    
    CheckBox:
        group:"Radio Button" # 원형 체크박스
    Label:
        text:'Radio Button'

'''))