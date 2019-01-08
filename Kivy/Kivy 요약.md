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

*실행화면*

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

## 04. size hint, pos_hint

