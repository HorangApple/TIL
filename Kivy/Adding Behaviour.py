from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from random import random
class MyPaintWidget(Widget):
    def on_touch_down(self,touch):
        print(touch) # 터미널에 마우스 위치 출력
        color = (random(), random(), random())
        with self.canvas:
            Color(*color)
            t = 100
            Ellipse(pos=(touch.x - t/2, touch.y -t/2),size=(t,t))
            touch.ud['Line'] = Line(points = (touch.x,touch.y))
    def on_touch_move(self,touch):
        touch.ud['Line'].points += [touch.x, touch.y]


class MyPrintApp(App):
    def build(self):
        return MyPaintWidget()

if __name__ == '__main__':
    MyPrintApp().run()