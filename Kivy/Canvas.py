from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

GridLayout:
    canvas: 
    # canvas를 소문자로 적어야한다. canvas 뒤에 주석을 적으면 오류가 발생한다.
        Color:
            rgb:1,2,0
        Rectangle:
            pos: 100,100 # self.pos는 (0,0) 위치
            size:100,100 # self.size는 화면 전체
'''))