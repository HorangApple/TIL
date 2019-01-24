##  flask
python이 설치되었다는 전제하에 다음 커멘드라인을 입력하여 설치한다.
```bash
sudo pip3 install flask
```
port를 열어놔야 다른 사람들이 들어와서 접속 할 수 있다. `host = 0.0.0.0`은 로컬 호스트이고 c9의 포트인 `port=8080`을 입력하여 flask를 작동시킨다.
```bash
flask run --host=0.0.0.0 --port=8080
```
사실 굳이 `--host`와 `--port`는 적지않아도 http://127.0.0.1:5000/ 로 자동으로 접속이 된다.
호스트가 0.0.0.0, 127.0.0.1은 내 컴퓨터를 가리키는 로컬호스트이기 때문에 외부에서 접근할 수 없다.

### 실습1

가변라우팅를 사용할 때 다음과 같이 함수의 파라메터에도 같은 이름으로 입력해야한다.

```python
@app.route("/hello/<name>")
def hello(name):
    return "hello, john"
```
`return`할 값은 무조건 string 형이여야 하므로 `str`형변환을 활용해야한다.

cf. `app.run(debug=True)`를 입력하여 디버그 모드에서 작업해도 되지만 습관이 들면 안되므로 안쓰고 하는 것이 좋다.

문자열은 비가변형 변수이기 때문에 중간의 문자를 변경시킬 수 없다. 그렇기때문에 `.replace`라는 메소드를 통해 변경한다. 

*app.py*

```python
from flask import Flask
app = Flask(__name__)

from datetime import datetime as dt

@app.route("/") # 주문 받는 방법 (요청을 받는 방법)
def index():
    return "<h1>Hello World!</h1>" # 서비스 주는 방법 (응답을 보내는 방법)

@app.route("/hello/<name>")
def hello(name):
    return "hello, "+name

@app.route("/cube/<int:num>") # int:num은 num이 int형으로 받아질 것을 알려줌
def cube(num):
    return "{} 입니다.".format(num ** 3)

@app.route("/reverse/<text>")
def reverse(text):
    return text[::-1] # reversed는 튜플, 리스트 등을 받기에 문자열을 받기엔 부적합함

@app.route("/ispal/<word>")
def ispal(word):
    return str(True) if (word==word[::-1]) else str(False)

@app.route("/isitnewyear")
def newyear():
    return '예' if (dt.now().month == 1 and dt.now().day == 1) else '아니요'
```



### 실습2

html이 복잡할 수록 python 코드 안에 다 수록하기엔 힘들기 때문에 flask의 render_template을 사용한다. 이를 사용하기 위해서는 별도로 'templates' 폴더를 만들어 `@app`의 하위 메소드의 이름과 같은 이름으로 html 파일을 만들어 보자. (사실 이름은 달라도 상관 없다.)

html을 자동완성 시켜주는 플러그인을 'emmet'이라 한다. html 문서 처음에 !를 입력하고 Tab을 누르면 자동완성 된다.

flask의 `send_file`을 이용해 `render_template`대신 html파일을 보여줄 수 있다. 이때 html 파일은 'app.py'와 같은 위치에 있어야한다. 그러나 동적인 파일을 만드는데에 부적합하기에 `render_template`을 사용해야한다.

{{}}는 'Jinja'라고 flask에 속해있는 기능인데 이를 이용하면 html에서도 파이썬 언어를 사용할 수 있다.

*app.py*

```python
from flask import Flask, render_template, send_file
app = Flask(__name__)

from datetime import datetime as dt

@app.route("/") # 주문 받는 방법 (요청을 받는 방법)
def index():
#   return send_file('home.html')
    return render_template('index.html') # 서비스 주는 방법 (응답을 보내는 방법)

@app.route("/hello/<name>")
def hello(name):
    return "hello, "+name

@app.route("/cube/<int:num>") # int:num은 num이 int형으로 받아질 것을 알려줌
def cube(num):
    return "{} 입니다.".format(num ** 3)

@app.route("/reverse/<text>")
def reverse(text):
    return text[::-1] # reversed는 튜플, 리스트 등을 받기에 문자열을 받기엔 부적합함

@app.route("/ispal/<word>")
def ispal(word):
    return str(True) if (word==word[::-1]) else str(False)

@app.route("/isitnewyear")
def newyear():
    return '예' if (dt.now().month == 1 and dt.now().day == 1) else '아니요'
```

*templates/index.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Welcome</title>
</head>
<body>
    <h1>Welcome</h1>
</body>
</html>
```

<img src = "images/image 002.png">

구글 검색 구조는 검색어를 `q`로 받아  `https://www.google.com/search`의 뒤에 `?q=검색어`가 붙여서 검색결과를 알려준다. 이를 이용하면 다음과 같이 바꿔 구글 검색을 이용할 수 있게 만들 수 있다.

*templates/index.html*
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Google</title>
</head>
<body>
    <h1>Google</h1>
    <form action="https://www.google.com/search"> <!--반응이 오면 지정된 곳으로 보내버린다-->
        <input name="q" type="text"></input> <!--q라는 파라미터 값을 action으로 보냄-->
    </form>
</body>
</html>
```

<img src="images/image 003.png">

위와 같이 만들어진다.



### 실습3

flask의 `request`는 요청받은 것을 분석하는 모듈이며 이전에 사용했던 `get, post`의 `requests`와는 전혀 다른 기능을 가지고 있다.

가짜 궁합사이트를 만드는 것을 실습해보자.

*app.py*

```python
from flask import Flask, render_template, send_file, request
app = Flask(__name__)

from datetime import datetime as dt
import random

hogu = []

@app.route("/") # 주문 받는 방법 (요청을 받는 방법)
def index():
#    lotto = random.sample(range(1,46),6)
#    return send_file('home.html')
    return render_template('index.html') # 서비스 주는 방법 (응답을 보내는 방법)

@app.route("/hello/<name>")
def hello(name):
    return "hello, "+name

@app.route("/cube/<int:num>") # int:num은 num이 int형으로 받아질 것을 알려줌
def cube(num):
    return "{} 입니다.".format(num ** 3)

@app.route("/reverse/<text>")
def reverse(text):
    return text[::-1] # reversed는 튜플, 리스트 등을 받기에 문자열을 받기엔 부적합함

@app.route("/ispal/<word>")
def ispal(word):
    return str(True) if (word==word[::-1]) else str(False)

@app.route("/isitnewyear")
def newyear():
    return '예' if (dt.now().month == 1 and dt.now().day == 1) else '아니요'

# /goonghap => 나와 상대방의 이름 + 페이크 궁합값(60-99)
@app.route("/goonghap")
def goonghap():

    # request : 사용자의 요청정보
    me=request.args.get('me') # args는 주소의 ? 뒤에 있는 값들을 딕셔너리 형으로 받아온다.
    you=request.args.get('you')
    hogu.append([me,you])
    rating = random.randint(60,99) # 60이상, 100이하
    return render_template('goonghap.html', me=me, you=you, rating=rating)

@app.route("/god")
def god():
    return str(hogu)
```



*templates/index.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>궁합</title>
</head>
<body>
    <h1>궁합</h1>
    <p>궁합을 알려드립니다 !</p>
    <form action="/goonghap"> <!--반응이 오면 지정된 곳으로 보내버린다-->
        <P>당신의 이름</P>
        <input name="me" type="text"></input> <!--q라는 파라미터 값을 action으로 보냄-->
        <P>그분의 이름</P>
        <input name="you" type="text"></input>
        <input type="submit"></input>
    </form>
</body>
</html>
```



*templates/goonghap.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>궁합</title>
</head>
<body>
    <h1>{{ me }}님과 {{ you }}님의 궁합은 {{ rating }}%입니다.</h1>
</body>
</html>
```



그런데 서버를 껐다 키면 `hogu`에 있는 데이터가 다 날아가므로 텍스트 파일로 남기도록 하거나 DB에 저장하도록 조치를 취해야한다.