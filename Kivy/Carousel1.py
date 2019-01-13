from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel  import Carousel
Builder.load_string("""

<MyWidget>:
    direction:'left' # 방향을 왼쪽으로
    loop:True # 무한회전
    Label:
        text:'Screen 1'
    Label:
        text:'Screen 2'
    Label:
        text:'Screen 3'

""")
class MyWidget(Carousel):
    pass

class TestApp(App):
    def build(self):
        return MyWidget()
    
if __name__=='__main__':
    TestApp().run()