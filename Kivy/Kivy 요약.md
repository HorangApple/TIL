# Kivy 정리

## 01. import kivy

```python
from kivy.app import App #대소문자 주의
from kivy.uix.label import Label
```
uix 모듈은 위젯과 레이아웃 같은 GUI의 모든 요소들을 담고 있다.

위젯은 체크박스나 왼쪽 버튼, 오른쪽 버튼 등을 가리킨다.

```python
class MyApp(App): # MyApp 이름은 원하는대로 변경할 수 있음
	def build(self):
		return Label(text='Hello world')
```
import 한 `App`을 `MyApp`상속시켜 그 클래스 안에 정의한 함수가 레이블  등을 윈도우 창에 그리게 만든다.

```python
if __name__ == '__main__':
	MyApp().run()
```
이것은 Kivy를 사용하게 되면 항상 입력해야하는 함수이다.



*Label.py*

```python
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__' :
    MyApp().run()
```

*결과*

<img src = 'images/image 004.png'>



## 02. runTouchApp

```python
from kivy.base import runTouchApp
from kivy.lang import Builder
```
`runTouchApp`은 만들어 놓은 것들을 화면 상의 터치를 통해 작동시켜주는 것을 도와준다. 그리고 `Builder`는 텍스트를 작성하는 것을 도와준다.

```python
runTouchApp(Builder.load_string('''
StackLayout:
	Label: # Label을 Button으로 바꾸면 누를 때 반응하는 버튼이 생성된다.
		text:'S1'
'''))
```
`Builder.load_string`은 텍스트를 작성해서 표현하는 기본적인 역할을 수행해준다.

*runTouchApp.py*

```python
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''

StackLayout:
    Button:
        text:'S1'

'''))
```

`from kivy.app import App`의 `.run()`에 의한 실행 대신에 사용할 수 있으며 터치반응이 가능하다는 점이 차이점이다.


*결과*
<img src = 'images/image 005.png'> <img src = 'images/image 006.png'>
`Button`으로 작성하여 레이아웃 전체가 버튼이 되었고  위와 같이 누르면 반응한다.



## 03. Orientation, BoxLayout

```python
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
```

uix를 사용하기위해 위와 같이 import하는데 버튼은 위젯의 일부분으로써 자주 쓰인다.

```python
<BoxLayout>:
    orientation: 'Horizontal'
    Button:
        text:'B1'
    Button:
        text:'B2'
    Button:
        text:'B3'
```

`BoxLayout`을 생성하고 거기에 버튼 3개를 추가로 생성한다. `orientation`을 통해 버튼의 배치를 수평으로 할지 수직으로 할지 설정한다.

```python
class MyListView(BoxLayout):
    pass
```



*Orientation.py*

```python
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Builder.load_string('''

<BoxLayout>
    orientation : 'horizontal' # 'vertical'로 바꿀 수 있음. default는 'horizontal'
    Button:
        text:'B1'
    Button:
        text:'B1'
    Button:
        text:'B1'
''')

class MyList(BoxLayout):
    pass

if __name__ =='__main__' :
    runTouchApp(MyList())
```
*`orientation`을 `'vertical'`로 했을 때*
<img src = 'images/image 008.png'>



*`orientation`을 `'horizontal'`로 했을 때*
<img src = 'images/image 007.png'>

이렇게 각각의 버튼에 자신이 원하는 기능을 달아서 실행하도록 만들면 된다.

## 04. size_hint, pos_hint

### 1) size_hint

`size_hint`에 두 값을 입력하여 가로, 세로를 조정할 수 있다. 같은 방법으로  `size_hint_x`와 `size_hint_y`가 있어 각각 값을 입력하면 된다. 레이아웃과 윈도우의 x, y 사이즈 설정을 맡고 있으므로 레이아웃과 윈도우 클래스에서만 사용이 가능하다. 수치의 범위는 `0.0`부터 `1.0`까지이며 0.5는 곧 50%를 이야기한다. default 값은 `1.0`으로 설정되어 있다.

*size_hint.py*

```python
from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""

FloatLayout:
    Button:
        text: 'B1'
        size_hint_x: 0.5 # size_hint: 0.5, 0.8을 입력한거
        size_hint_y: 0.8

"""))
```

*결과*
<img src = 'images/image 009.png'>

위와 같이 왼쪽 아래쪽 모퉁이를 기준으로 영역이 조절된다.

```python
size_hint_max_x: None
size_hint_max_y: None
```
무조건 최대 크기로 사용하고 싶다하면 `size_hint_max_x`와 `size_hint_max_y`를 이용하면 된다. 

*size_hint.py*

```python
from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""

BoxLayout:
    Button:
        text: 'B1'
        size_hint_x : 0.5
    Button:
        text: 'B1'
        size_hint_x : 1
    Button:
        text: 'B1'
        size_hint_x : 0.5

"""))
```
위와 같이 작성하면 어떻게 될까? 프로그램이 자동으로 조정하여 `0.5->0.25`,`1->0.5`,`0.5->0.25`로 상대적인 비율을 맞춰준다.

*결과*
<img src = 'images/image 010.png'>

### 2) pos_hint
`pos_hint`는 위젯의 위치를 지정해주는 요소이다. `x`와 `y`값을 입력하여 조절하고 입력 방식은 `size_hint`와 다르니 아래 예제를 통해 확인하자.

*pos_hint.py*

```python
from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""

FloatLayout:
    Button:
        text: 'B1'
        size_hint: 0.2, 0.2
        pos_hint: {'x': .5, 'y': .8}
"""))

```

*결과*
<img src = 'images/image 011.png'>

버튼의 왼쪽 하단 모퉁이를 기준으로 위치가 정해진다. 현재 `y`가 80%로 되었음에도 이미 상단 끝에 닿은 것을 확인할 수 있는데 이는 `size_hint`의 `y`값, 즉 버튼의 높이까지 고려되어 위와 같이 나왔다. 만약에 `size_hint`의 y값+`pos_hint`의 y값이 100%가 넘어가면 윈도우에 짤려서 나오게 되니 주의하자.

*pos_hint.py*

```python
from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""

FloatLayout:
    Button:
        text: 'B1'
        size_hint: 0.2, 0.2
        pos_hint: {'top': 0.5, 'right': 0.5}
"""))

```

*결과*
<img src = 'images/image 012.png'>
`x`와 `y`뿐만 아니라 `x`는 `lift`, `right`로, `y`는 `top`, `down`로 대체해 설정할 수 있다.  다만 'top'과 'right'를 함께 사용하면 오른쪽 상단 모서리가 기준인 것처럼 위치의 기준이 변경된다.

## 05. horizontal, vertical
<img src = 'images/image 013.png'>

회전의 상태에 따라 다음과 같이 값이 사용된다.

```
vertical : x, right, center_x
horizontal : y, top, center_y
```

## 06. super, padding, __init__, add_widget
```python
class Class1(BoxLayout):

    def __init__(self, **kwargs):
        super(Class1,self).__init__(**kwargs)

        self.padding = 200 # 바깥 여백 길이

        button = Button(text = 'Banana')
        self.add_widget(button)
```
위의 함수 `__init__`은 위젯을 추가시키기 위해 'override'를 했다. `super`는 원래의 클래스를 실행시키기 위해 사용된다. 또한 패스워드 확인란을 만들 때 사용되기도 한다.
`__init__`을 'override'하는 부분은 고정적으로 항상 사용되기 때문에 잊지말자. 이후에는 `padding`과 같이 BoxLayout을 설정하는 내용을 작성하면 된다.
*super, padding, __init__, add_widget.py*

```python
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button

class Class1(BoxLayout):

    def __init__(self, **kwargs):
        super(Class1,self).__init__(**kwargs)

        self.padding = 200 # 바깥 여백 길이

        button = Button(text = 'Banana')
        self.add_widget(button)

class Class2(App):
    def build(self):
        return Class1()

if __name__ == '__main__':
    Class2().run()

```

*결과*
<img src = 'images/image 014.png'>