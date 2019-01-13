# Kivy Basics
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

회전의 상태에 따라 다음과 같이 값이 사용된다. 가로 방향에서 왼쪽을 나타낼 때는 `x`, 오른쪽을 나타낼 땐 `right`이다. 세로 방향에서는 위를 나타낼 때는 `top`, 아래를 나타낼 때는 `y`이다.

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

*super, padding, __ init __, add_widget.py*

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


# Layout
## 07. BoxLayout

`BoxLayout`은 버튼과 같은 위젯의 수직 또는 수평을 설정해주는 것이다.

*BoxLayout.py*

```python
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

BoxLayout:
	orientation:'vertical'
	spacing: 10
	padding: 100
	Button:
		text:'F1'
	Button:
		text:'F2'


'''))
```

*결과*

<img src = 'images/image 015.png'>



## 08. FloatLayout

`FloatLayout`은 child widgets의 위치, 크기 등을 설정해주는 것이다.

*FloatLayout.py*

```python
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

<Button>:
    color:.8,.2,0,1
    font_size: 50
    size_hint:.3,.2
FloatLayout:
    Button:
        text: 'Hello'
        pos_hint:{'x':0,'top':1}
    Button:
        text: 'world'
        pos_hint:{'right':1,'y':0}


'''))
```

*결과*

<img src = "images/image 017.png">



## 09. GridLayout

`GridLayout`은 위젯을 매트릭스 형식으로 배치시켜준다. 변수 `cols`와 `rows`로 조절한다. 두 변수 중 하나에 값을 초기화 시켜야 작동한다. 그렇지 않으면 한곳에만 몰리는 것을 볼 수 있다.

*GridLayout.py*

```python
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

GridLayout:
    cols:2
    size_hint_x:None #size_hint_x를 적용하지 않음 (deault값이 1이였음)
    size_hint_y:None

    Button:
        text:'hello'
        width:100
    Button:
        text:'world'
        width:100
'''))
```

*결과*

<img src = "images/image 016.png">

`GridLayout` 밑과 버튼 안에 `size_hint_x:None` 이 있으면 `width` 대로 크기가 조절이 된다. 여기서는 두 버튼 모두 `size_hint_x:None`을 갖고 있어야 제대로 조절이 가능하다.

## 10. RelativeLayout

`RelativeLayout`는 child widgets에 상대좌표를 사용할 수 있게끔 해준다. 절대좌표를 사용하는 `FloatLayout`과는 반대이다.

*RelativeLayout.py*

```python
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

RelativeLayout:
    Button:
        text:'R1'
        size_hint:.3,.3
        pos: 250,100
    Button:
        text:'R2'
        size_hint:.2,.2
        pos_hint:{'x':0.3,'y':0}
        
'''))
```

## 11. StackLayout

`StackLayout`에서 `orientation`값을 조정하여 위젯의 배치를 '왼쪽에서 오른쪽, 위에서 밑으로'와 같이 설정할 수 있다.

*StackLayout.py*

```python
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

StackLayout:
    orientation: 'lr-tb' # left to right, top to bottom
    padding : 20
    spacing : 10
    Button:
        text:'B1'
        size_hint:.2,.1
    Button:
        text:'B2'
        size_hint:.2,.1
    Button:
        text:'B3'
        size_hint:.2,.1
    Button:
        text:'B4'
        size_hint:.2,.1
    Button:
        text:'B5'
        size_hint:.2,.1
    Button:
        text:'B6'
        size_hint:.2,.1
'''))
```

*결과*

<img src = "images/image 018.png">



## 12.PageLayout

`PageLayout`은 `size_hint`, `size_hint_min`, `size_hint_max`, `pos_hint`를 지원하지 않는다. 윈도우 상에서 종이 넘기는 것처럼 한 페이지에서 다른 페이지로 넘어갈 수 있게끔 해준다.

*PageLayout.py*

```python
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

PageLayout:
    Button:
        text:'B1'
    Button:
        text:'B2'
    Button:
        text:'B3'
'''))
```

*결과*

<img src = "images/image 019.png"> <img src = "images/image 020.png">
'B1'의 오른쪽 경계를 드래그하면 책넘기는 효과와 함께 'B2'로 화면이 전환된다.

# UX widgets
## 13. Button
`Button`에서 텍스트, 글자 크기, 색상, 위치를 조정할 수 있다.

*Button1.py*

```python
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
```

*결과*

<img src = "images/image 021.png">

## 14.Button with root

`root`는 `x`, `right`, `top`, `y` 각 방향의 최대 지점을 나타낸다. 움직일 때는 왼쪽 하단 모서리를 기준으로 움직이므로 윈도우에서 벗어나지 않겠끔 버튼의 크기를 고려하여 위치를 설정해야한다.

*Button2.py*

```python
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

Label:
    Button:
        text:'Hello'
        pos:root.x,root.top - self.height
    Button:
        text:'World!'
        pos:root.right-self.width*1/2,root.y
'''))
```

*결과*

<img src = "images/image 022.png">



## 15. Button with super

`super`를 이용하여 버튼을 생성할 수 있다.

*Buttonsuper.py*

```python
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button


class Controller2(FloatLayout):
    def __init__(self, **kwargs):
        super(Controller2, self).__init__(**kwargs)
        button = Button(text = 'Hello World', color = (.9,.8,0,1), font_size = 10, \
        pos_hint = {'x': .7,'y':.8}, size_hint = (.1,.1))
        self.add_widget(button)
        button = Button(text = 'Hello World', color = (.9,.3,0,1), font_size = 20, \
        pos_hint = {'x': .5,'y':.6}, size_hint = (.2,.2))
        self.add_widget(button)
        button = Button(text = 'Hello World', color = (.9,.5,0,1), font_size = 30, \
        pos_hint = {'x': .2,'y':.3}, size_hint = (.3,.3))
        self.add_widget(button)

class Controller2App(App):
    def build(self):
        return Controller2()

if __name__== '__main__':
    Controller2App().run()
```

*결과*

<img src = "images/image 023.png">



## 16. Label

```
[b][/b] 볼드체
[i][/i] 이탤릭체
[u][/u] 밑줄
[s][/s] 취소선
[font=<str>][/font] 폰트 변경
[size=<integer>][/size] 글씨 크기 변경
[color=#<color>][/color] 글씨 색상 변경
[sub][/sub] 밑첨자
[sup][/sup] 윗첨자
```

*Buttonsuper.py*

```python
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label


class Controller2App(App):
    def build(self):
        return Label(text='[color=3333ff][sup]Hello[/sup][/color] [color=ff3333][b][s][sub]World[/sub][/s][/b][/color]', markup = True, font_size = '60sp')

if __name__== '__main__':
    Controller2App().run()
```

*결과*

<img src = "images/image 024.png">

## 17. Label And Button

*Label And Button.py*

```python
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    size_hint_y:None
    height:sp(300) # Label과 Button이 차지하는 절대적인 높이 설정
    Label:
        text:'Hello'
    Button:
        text:'World'
'''))
```

*결과*

<img src = "images/image 025.png">



## 18. ActionBar

`ActionBar`는 안드로이드 시스템에 존재하는 UI를 말한다. 

*ActionBar.py*

```python
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
ActionBar:
    pos_hint:{'top':1}

    ActionView:
        ActionPrevious: # 이전 버튼
            title:'Action Bar'
            with_previous:False # 이전 버튼 사용 안함
        
        ActionButton:
            text:'Bt1'
            icon:'atlas://data/images/defaulttheme/audio-volume-high'
        ActionButton:
            text:'Bt2'
        ActionButton:
            text:'Bt3'
        ActionButton:
            text:'Bt4'
        ActionGroup: # 화면이 작아지면 자식 버튼들을 한 곳으로 묶어줌
            text:'Group'
            color:.3,.9,0,1
            font_size:20
            ActionButton:
                text:'Bt1'
            ActionButton:
                text:'Bt2'
            ActionButton:
                text:'Bt3'
'''))
```

*결과*

<img src = "images/image 026.png">



## 19. CheckBox

*CheckBox.py*

```python
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
```

*결과*

<img src = "images/image 027.png">



버튼을 누르면 CheckBox에 영향이 가게끔 CheckBox에 id를 설정하여 만들 수 있다.

*CheckBox project.py*

```python
from kivy.lang import Builder
from kivy.app import App

kv = """
BoxLayout:
    orientation:'vertical' # default는 'horizontal'
    CheckBox:
        group:'a'
        active: True
    CheckBox:
        id:Ch
        group:'a'

    Button:
        text:'Yes'
        on_press:Ch.active=True
    Button:
        text:'No'
        on_press:Ch.active=False       
"""

class TestApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    TestApp().run()
```

*결과*

<img src = "images/image 036.png">



## 20. Progressbar

`Progressbar`는 진행의 척도를 나타내는 UI이며 오직 horizontal로만 사용이 가능하다.

*Progressbar.py*

```python
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
BoxLayout:
    padding:30
    ProgressBar:
        id:bar
        max:100
        value:50
'''))
```

*결과*

<img src = "images/image 028.png">



## 21. Scatter

화면상의 사용자의 조작(터치)를 통하여 위젯 등을 최대화하거나 최소화하거나 위치를 변경하거나 회전방향을 변경할 때 사용한다. PC 상에서는 우클릭으로 빨간원을 설정하고 좌클릭으로 드래그하면 된다.

*Scatter.py*

```python
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
FloatLayout:
    Scatter:
        size:100, 100
        pos:100, 100
        do_rotation:False # default는 True
        Label:
            text:"something"
'''))
```

*결과*

<img src = "images/image 029.png"> <img src = "images/image 030.png">

*좌측은 `do_rotation:True`, 우측은 `do_rotation:False`



## 22. Canvas



*Canvas.py*

```python
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
```

*결과*

<img src = "images/image 031.png">



## 23. AsyncImage

이미지를 삽입할 때 사용한다. `anim_delay`는 이미지 로딩 애니메이션의 속도를 조절하며 숫자가 낮을 수록 빨리 움직인다.

*AsyncImage.py*

```python
from kivy.app import App
from kivy.lang import Builder

kv = """
AnchorLayout:
    canvas:
        Color:
            rgba:1,3,1,1
        Rectangle:
            pos:self.pos
            size:self.size
    AsyncImage:
        size_hint:None,None
        size:dp(560),dp(560)
        source:'https://raw.githubusercontent.com/kivy/kivy/master/kivy/data/logo/kivy-icon-256.png'
        anim_delay:0.03
"""

class TestApp(App):
    def build(self):
        return Builder.load_string(kv)
    
if __name__=='__main__':
    TestApp().run()
```

*결과*

<img src = "images/image 032.png">



# Complex UX widegts

## 24. Spinner

옵션을 선택하듯 열거한 후에 선택하여 값을 설정하는 UI를 만들 수 있다.

*Spinner.py*

```python
from kivy.uix.spinner import Spinner
from kivy.base import runTouchApp

s = Spinner(
    text='Home',
    values=('Home','Work','Custom','Other'),
    size_hint=(None,None),
    size=(100,44),
    pos_hint={'center_x':.5,'center_y':.5}

)
def Show_value(spinner, text):
    print('the spinner have text : ', text)

s.bind(text=Show_value)

runTouchApp(s)
```

*결과*

<img src = "images/image 033.png">

<img src = "images/image 034.png">

`Home`, `Work`, `Custom`, `Other`를 클릭할 때마다 맨 첫 번째 칸에 그 이름으로 변경되고 터미널에 출력이 된다.



## 25. Accordion

악기 아코디언처럼 내용을 열 수 있는 세로로 긴 버튼을 만들 수 있게 한다.

*Accordion.py*

```python
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.app import App
from kivy.uix.label import Label

class AccordionApp(App):
    def build(self):
        root = Accordion()
        for x in range(5):
            item = AccordionItem(title='Title %d' %x, min_space=35) 
            # min_space의 default는 40
            item.add_widget(Label(text='Hello World\n'*5))
            root.add_widget(item)
        return root


if __name__ == '__main__':
    AccordionApp().run()
```

*결과*

<img src = "images/image 035.png">



## 26. Slider, ProgressBar

`Slider`는 `ProgressBar`와 다르게 수직으로 회전시킬 수 있다. `id`를 설정해 `Slider`가 움직이면 같이 `ProgressBar`도 움직이게 만드는 코드는 아래와 같다.

*Slider, Progressbar.py*

```python
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

BoxLayout:
    orientation:'vertical'
    padding:50

    ProgressBar:
        value:slider.value
        max:300
    Slider:
        id:slider
        max:300
        value:140
    Slider:
        orientation:'vertical'
        on_value:slider.value=self.value
        max:400

'''))
```

*결과*

<img src = "images/image 037.png">



## 27. Text on window

*Text on window.py*

```python
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

BoxLayout:
    orientation :'vertical'
    Label:
        canvas.before:
            Color:
                rgba:1,0,0,0.22
            Rectangle:
                pos:self.pos
                size:self.size
        text:'Top'
        size_hint_y:None
        height:sp(65)
        font_size:sp(50)
    Label:
        canvas.before:
            Color:
                rgb:1,0,0
            Rectangle:
                pos:self.pos
                size:self.size
        text:'Center'
        size_hint_y:None
        height:sp(65)
        size_hint_x:None
        width:sp(65)
    Label:
        canvas.before:
            Color:
                rgba:2,1,1,0.35
            Rectangle:
                pos:self.pos
                size:self.size
        text:'Botton'
        size_hint_y:None
        height:sp(65)
'''))
```

*결과*

<img src = "images/image 038.png"><img src = "images/image 039.png">

*좌측은 `orientation :'horizontal'`일 때, 우측은 `orientation :'vertical'`일 때



## 28. TextInput

텍스트를 입력할 수 있는 창을 만든다. `use_bubble:True`는 복사, 잘라내기, 붙여놓기 버튼을 팝업하는 기능을 켜게 한다. `use_handles:True`는 커서를 가리키는 아이콘이 생성된다. `password:True`는 모든 텍스트를 `*`로 처리하여 가려준다. `readonly:True`는 읽기전용으로 바뀌며 bubble에서 사용할 수 있는 기능은 복사로 제한된다.

*TextInput.py*

```python
from kivy.app import App
from kivy.lang import Builder

kv = """
AnchorLayout:
    TextInput:
        size_hint:None,None
        size: 400, 100
        text: 'Select this text'
        use_bubble:True
        use_handles:True
        password:False
        readonly:False
"""

class TestApp(App):
    def build(self):
        return Builder.load_string(kv)
    
if __name__=='__main__':
    TestApp().run()
```

*결과*

<img src = "images/image 040.png">



## 29. Carousel

옆으로 드래그하여 페이지를 넘기게 해준다.

*Carousel1.py*

```python 
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
```

*결과*

<img src = "images/image 041.png"><img src = "images/image 042.png">



*Carousel2.py*

```python
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
class CarouselApp(App):
    def build(self):
        c = Carousel(direction='right', loop = True)
        for i in range(10):
            src = "http://placehold.it/480x270.png& text=Silde- %d" %i
            image = AsyncImage(source=src, allow_stretch=False)
            c.add_widget(image)
        return c

CarouselApp().run()
```

*결과*

<img src = "images/image 043.png">