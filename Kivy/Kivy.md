# Kivy의 대모험

### 1. 설치

https://kivy.org/#download 에서 원하는 플랫폼을 클릭하여 들어가 설치한다.

윈도우는 다음의 커맨드 라인을 입력하면 설치가 된다. (단, 사전에 python이 설치되어 있어야 한다.)
```bash
python -m pip install --upgrade pip wheel setuptools
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer
python -m pip install kivy
```
예제까지 설치하고 싶다면 다음까지 입력한다.
```bash
python -m pip install kivy_examples
```
<img src = "images/image 002.png">
VS Code를 사용한다면 View-Extensions에 가서 'Kivy'를 설치하자


### 2. first App

Kivy의 공식 튜토리얼로 Pong 게임 제작이 설명되어있다.
https://kivy.org/doc/stable/tutorials/pong.html
차근차근 따라가보자

*main.py*

```python
from kivy.app import App # 앱을 만들기 위한 모듈
from kivy.uix.widget import Widget # 위젯을 만들어 그래픽을 표현


class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()
```

python을 이용해 기본 골격을 짠다. kivy 앱을 만들기 위해선 반드시 `App`을 import 시켜야한다.



*pong.kv*

```
#:kivy 1.0.9
# kv 파일이면 반드시 작성해야할 코드

<PongGame>:    
# 그래픽을 담당하는 Widget 클래스에 맞춰 세부 설정을 한다.
	canvas:
        Rectangle:
            pos: self.center_x - 5, 0
            size: 10, self.height
# 가운데 경계선을 만든다.            
    Label:
        font_size: 70  
        center_x: root.width / 4
        top: root.top - 50
        text: "0"
# 화면 상단의 왼쪽에 텍스트 "0"을 출력한다.        
    Label:
        font_size: 70  
        center_x: root.width * 3 / 4
        top: root.top - 50
        text: "0"
# 화면 상단의 오른쪽에 텍스트 "0"을 출력한다.  
```

HTML과 CSS의 관계처럼 Kivy에서는 확장자`.kv`로 끝나는 파일을 통해 디자인적 요소를 담아내야 한다. 

여기서 사용되는 문법을 'Kv'언어라고 하며 자세한 것은 다음 링크에 들어가서 확인해보자

https://kivy.org/doc/stable/guide/lang.html

당장 사용된 문법을 간단히 이야기해보자면 맨 첫 줄인  `#:set name value`는 전역 변수를 설정하는 것이며 여기서 kv 파일을 사용하기위해 반드시 `#:kivy '요구되는 최소 버전'`을 입력해야한다.

`<PongGame>`처럼 <과 >로 감싸있는 것은 py 파일에 있는 widget에 해당되는 class이며 `canvas`와 같이 아무것도 감싸있지 않은 것은 class 아래에 속하는 root이다. 

kv는 python처럼 들여쓰기의 주의가 반드시 필요하다.

결과적으로 'pong.kv'를 통해 widget인 `PongGame`은 화면에 몇 가지 그래픽들을 그리는 역할을 해주었다.

<img src = "images/image 001.png">

완성된 코드를 돌려보면 위와 같이 나온다.



다음으로 공과 그것을 움직이게 만드는 코드를 추가해본다.

`from kivy.properties` 가 아마 찾을 수 없다고 VS Code에서 Problems로 나올텐데 무시하고 진행하자.

*main.py*

```python
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from random import randint

class PongBall(Widget):
# 공을 나타내는 class
    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
	ball = ObjectProperty(None)
 
    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # bounce off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

class PongApp(App):

    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        # 공을 움직이게끔 game.update를 1초당 60번 실행
        return game
    
if __name__ == '__main__':
    PongApp().run()
```

*pong.kv*

```
#:kivy 1.0.9

<PongBall>:
    size: 50, 50 
    canvas:
        Ellipse:
            pos: self.pos
            size: self.size          

<PongGame>:
    ball: pong_ball
    
    canvas:
        Rectangle:
            pos: self.center_x-5, 0
            size: 10, self.height
    
    Label:
        font_size: 70  
        center_x: root.width / 4
        top: root.top - 50
        text: "0"
        
    Label:
        font_size: 70  
        center_x: root.width * 3 / 4
        top: root.top - 50
        text: "0"
    
    PongBall:
        id: pong_ball
        center: self.parent.center
```

<img src = "images/image 003.png">