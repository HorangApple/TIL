# Kivy - Udemy

## 01. import kivy

```python
from kivy.app import App #lowercase
from kivy.uix.label import Label #Uppercase
```
uix 모듈은 위젯과 레이아웃 같은 GUI의 모든 요소들을 담고 있다.

```python
class MyApp(App): # MyApp 이름은 원하는대로 변경할 수 있음
	def build(self):
		return Label(text='Hello world')
```
import 한 `App`을 `MyApp`상속시켜 그 클래스 안에 정의한 함수가 레이블  등을 그리게 만든다.

```python
if __name__ == '__main__':
	MyApp().run()
```
이것은 Kivy를 사용하게 되면 항상 입력해야하는 함수이다.