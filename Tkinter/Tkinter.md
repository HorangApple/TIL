# Tkinter

Tkinter는 python 내장 GUI 라이브러리로 간단한 GUI 작업을 할 때 유용하다.

*widget.py*

```python
from tkinter import *
# Tk = tkinter.Tk처럼 모든 메서드에 대해 변수화 작업을 하기 때문에 import *를 사용하면 경고창이 뜬다.
import webbrowser

def browser():
    url = "https://www.google.com/search?q={}".format("미세먼지")
    webbrowser.open(url)

# root라는 윈도우 제작
root = Tk()

# Label(어떤 tkinter 윈도우 프로그램에 넣을지, text="")
label = Label(root,text="Hello",fg="red",bg="blue")
label2 = Label(root,text="My widget")

# Button 생성
btn = Button(root, text="This is a button", command=browser())

# Label, Button 등의 좌표값 지정
label.pack()
label2.pack()
btn.pack()

# 프로그램 구동
root.mainloop()

```

*실행 결과*

<img src = "images/image 001.png">

추가적인 사용법은 인터넷에 찾아서 해보자



### 

