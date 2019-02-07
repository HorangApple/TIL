# Web Service*

세상의 서비스는 요청과 응답으로 이루어져 있다. 어떻게 요청할지 어떻게 응답을 받을지가 중요하다.

인터넷을 최초로 만든사람은 '팀 버너스리'이다.

클라이언트의 요청과 서버의 응답을 주고 받는 방식으로 돌아가며 우리는 플라스크와 장고를 이용해 서버를 만들어 서비스를 제공할 것이다. 그래서 서버 컴퓨터를 만들 것이다.

서버 컴퓨터에서 요청과 응답을 처리하는 프로그램을 만들고 html문서로 정보를 보내주는 기능을 구현한다.

'web developer'라는 extension을 크롬에서 깔아서 front end 개발할 때 사용한다.

웹 페이지는 탐색기와 비슷하게 주소들을 통해 접속할 수 있다.  실제 주소는 ip 형식으로 되어 있지만 사람들이 외우기 쉽게 Domain name을 사용한다. 그러나 DNS 서버가 해킹을 당하면 ip로 직접 접속하지않는 한 접속 할 수 없다.

우리는 aws route 53 서비스를 통해 Domain name을 구매한다.

IP (internet Protocol)

- 172.217.161.78

Domain

- google.com

똑같은 정보를 주는 사이트는 `static web`이고 요청에 맞는 정보를 주는 사이트를 `dynamic web`로 분류할 수 있다.

mozila mdn에 들어가서 웹 기술을 배우자

기존의 페이지는 책처럼 넘겨서 보았지만 하이퍼 텍스트는 거미줄 처럼 페이지들이 서로 연결되어 있다. 그런 링크를 Marking 시킨다. 그것을 작성시키는 언어가 HTML이다.

CSS를 추가시키면 심미적으로 꾸밀 수 있고 JavaScript를 통해 보다 동적인 사이트를 만들 수 있다.

html은 크게 head와  body로 구분되어 있으며 head 부분에 메타 태그를, body 부분에는 브라우저에 나타나는 실질적인 내용을 작성한다.

# HTML

요소

태그는 '여는 태그', '닫는 태그'로 구성되어 있으며, 대소문자를 구분하지 않으나 소문자를 입력한다.  

self close tag가 있는데 image src가 해당된다. 

속성은 속성명과 속성값으로 구성되어 있다. 

DOM 트리는 html의 계층구조를 나타낸다.

<img src = "images/image 001.jpg">

시멘틱 태그

<img src="images/image 002.jpg">

웹을 의미상으로 구분해놓게 해주는 태그를 의미한다.

Web Developer에서 Document outline을 사용하면 구조적으로 얼마나 잘 짰는지 확인할 수 있다. 



SEO : 검색엔진최적화

구글에는 크롤러라는 봇을 이용해 페이지를 수집하는데 잘 짜여진 시멘틱 태그이면 구글에서 검색 될 때 이쁘게 보일 수 있게 된다. 그렇기 때문에 구조적으로 잘 짜는 것이 중요하다. 



*python.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>프로그래밍 교육</h1>
    <hr>
    <h2>파이썬</h2>
    <h3>Number type</h3>
    <p>파이썬에서 숫자형은 아래와 같이 있다.</p>
    <ol>
        <li>int</li>
        <li>float</li>
        <li>complex</li>
        <li><s>str</s></li> <!--취소선은 <s> 태그-->
    </ol>
    <h3>Sequence</h3>
    <p>파이썬에서 시퀀스는 아래와 같이 있다.</p>
    <h3>시퀀스는 for문을 돌릴 수 있다!!</h3>
    <ol>
        <li>str</li>
        <li>list</li>
        <li>tuple</li>
        <li>range</li>
    </ol>
    <hr>
    <h2>웹</h2>
    <h3>기초</h3>
    <ul>
        <!-- css를 이용해 모양을 바꿀 수 있다.-->
        <li style="list-style-type:square">HTML</li> 
        <li style="list-style-type:square">CSS</li>
    </ul>
</body>
</html>
```



# CSS

html을 꾸밀 수 있는 방법은 인라인, 스타일, 파일이다. 이 중 CSS 파일로 따로 빼서 하는 것을 할 것이다.

html과 다른 css만의 언어를 사용한다.

html에서 `style=값`으로 정의할 수 있지만 수많은 정보를 일일히 작성하기엔 비효율적이다. 그렇기 때문에 CSS를 통해 간편하게 꾸민다.

다음과 같이 적용하며 속성마다 세미콜론(;)으로 구분한다.

```css
Selector{Property1:Value1;Property2:Value2;...}
```

Value로는 1. 키워드, 2. 색깔, 3. 크기단위(px: 픽셀화소, %, em, rem)

픽셀단위는 디바이스별로 크기가 제각각이다.

CSS의 Cascading 말대로 가장 아래쪽 규칙을 우선으로 따른다.

명시도가 높은, 즉 상세하게 정의된 것을 우선으로 규칙이 적용된다.

https://poiemaweb.com/ 에서 공부하자 

*python.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!--클래스 정의는 . 찍고 작성하면 된다.-->
    <style>
        .salmon{
            color:darksalmon;
            font-size: 20px;
            font-style: italic;
            font-family: 'Times New Roman', Times, serif;
            font-weight: bold
        }
        p{
            color: deeppink;
        }
        body{
            background-color:gray;
        }
        h1{
            color:blue
        }
        h2{
            color: yellow
        }
        h3{
            color: purple
        }
        hr{
            height:1px; background-color: seagreen
        }

    </style>
</head>
<body>
    <h1>프로그래밍 교육</h1> <!--파란색-->
    <hr> <!--초록색-->
    <div id=python>
        <h2>파이썬</h2>
        <h3>Number type</h3> <!--보라색-->
        <p class="salmon">파이썬에서 숫자형은 아래와 같이 있다.</p>
        <!--리스트의 모든 요소들은 orange로 색을 바꾸세요-->
        <ol class="salmon">
            <li style="color: red">int</li> 
            <!--Cascading 적용, 대상을 명확하게 특정할수록 명시도가 높아지고 우선순위가 높아진다.-->
            <li>float</li>
            <li>complex</li>
            <li><s>str</s></li> <!--취소선은 <s> 태그-->
        </ol>
        <h3>Sequence</h3>
        <p>파이썬에서 시퀀스는 아래와 같이 있다.</p>
        <h3>시퀀스는 for문을 돌릴 수 있다!!</h3>
        <ol class="salmon">
            <li>str</li>
            <li>list</li>
            <li>tuple</li>
            <li>range</li>
        </ol>
    </div> 
    <hr>
    <div>
        <h2>웹</h2>
        <h3>기초</h3>
        <ul>
            <!-- css를 이용해 모양을 바꿀 수 있다.-->
            <li style="list-style-type:square">HTML</li>
            <li style="list-style-type:square">CSS</li>
        </ul>
    </div>
</body>
</html>
```

만약 style만 따로 css 파일로 빼고 싶다면 `<link rel="stylesheet" href="style.css">` 를 이용하자

*python.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="style.css"> <!--css연결-->
</head>
<body>
    <h1>프로그래밍 교육</h1> <!--파란색-->
    <hr> <!--초록색-->
    <div id=python>
        <h2>파이썬</h2>
        <h3>Number type</h3> <!--보라색-->
        <p class="salmon">파이썬에서 숫자형은 아래와 같이 있다.</p>
        <!--리스트의 모든 요소들은 orange로 색을 바꾸세요-->
        <ol class="salmon">
            <li>int</li> 
            <!--Cascading 적용, 대상을 명확하게 특정할수록 명시도가 높아지고 우선순위가 높아진다.-->
            <li>float</li>
            <li>complex</li>
            <li><s>str</s></li> <!--취소선은 <s> 태그-->
        </ol>
        <h3>Sequence</h3>
        <p>파이썬에서 시퀀스는 아래와 같이 있다.</p>
        <h3>시퀀스는 for문을 돌릴 수 있다!!</h3>
        <ol class="salmon">
            <li>str</li>
            <li>list</li>
            <li>tuple</li>
            <li>range</li>
        </ol>
    </div> 
    <hr>
    <div>
        <h2>웹</h2>
        <h3>기초</h3>
        <ul>
            <!-- css를 이용해 모양을 바꿀 수 있다.-->
            <li>HTML</li>
            <li>CSS</li>
        </ul>
    </div>
</body>
</html>
```



*style.css*

```css
.salmon{
    color:darksalmon;
    font-size: 20px;
    font-style: italic;
    font-family: 'Times New Roman', Times, serif;
    font-weight: bold
}
p{
    color: deeppink;
}
body{
    background-color:gray;
}
h1{
    color:blue
}
h2{
    color: yellow
}
h3{
    color: purple
}
hr{
    height:1px; background-color: seagreen
}
li{
    list-style-type:square
}
```

모던 폰트에서는 세리프를 잘 안 쓴다. 왜냐하면 렌더링 하는데에도 자원 소모가 크기 때문에 얇은 부분과 곡선이 별로 없는 산세리프를 많이 쓴다.

<img src = "images/image 001.png">

크롬의 폰트 설정에 들어가면 Serif나 San-serif로 정의되어 있는 글꼴을 내 브라우저에서 임의의 글꼴로 바꿔주는 기능을 제공하고 있다.

<img src = "images/image 002.png">

구글 폰트에 들어가서 원하는 폰트를 받아 사용할 수 있다. 

```html
<head>
	...
    <link href="https://fonts.googleapis.com/css?family=Nanum+Gothic" rel="stylesheet">
    <link rel="stylesheet" href="style.css"> <!--css연결-->
</head>
```



만약 내가 폰트를 추가하고 싶다고 하면 글꼴을 SELECT 하여 하단 팝업에 뜨는 `link` 주소를 복사하여 html의 CSS 파일을 불러오는 파일보다 먼저 선언하게 끔 작성한다.

*style.css*

```css
...
    font-family: Nanum Gothic,sans-serif;
...
```

이후 CSS파일에서 `font-family` 어트리뷰트에 사용하려는 폰트 이름을 추가 시키면 된다.

em 단위는 배수 단위로 상대 단위다. 그러나 상속의 영향으로 바뀔 수 있다.

rem 단위는 최상위 요소 사이즈를 기준으로 삼는다.

Viewport 단위 디바이스마다 다른 크기의 화면을 가지고 있기 때문에 디바이스 기준으로 상대적인 단위인 viewport를 기준으로 만든 단위이다. 이것은 반응형 웹 페이지를 제작할 때 필수적으로 사용해야한다.



Box model

항상 네모로 생각해야한다. 둥근 모양도 사실 네모를 깎아서 표현했다고 해도 무방하다.

<img src="images/image 003.png">

margin은 박스 밖의 여백을 지칭한다. 여러 박스와 margin이 겹치게 될텐데 이는 합산하지 않고 margin 값이 큰 것을 기준으로 겹쳐진다.

margin 어트리뷰트는 4개 값을 입력하면 top을 시작으로 시계방향으로 설정되고 2개 값을 입력하면 세로, 가로를 기준으로 적용이되고 값이 하나만 입력되면 4방향으로 같은 값이 적용된다.

```css
margin : 16px 16px 16px 16px /*(top을 시작으로 시계방향으로 설정)*/
margin : 16px 16px /*(세로축, 가로축)*/
margin : 16px /*(한번에 네 군데)*/
```

border는 box의 경계선을 가리킨다. 어트리뷰트의 필수 값은 `dotted`와 같은 style이다. default로 1px로 잡혀있기에 style만큼은 꼭 정해줘야한다. border는 다음과 같이 한 줄로 정의할 수도 있다.

```css
border:2px dotted pink;
```
```css
border-width: 1px 2px 2px 1px;
border-color:pink;
border-style: dashed;
```

padding은 box 내부의 여백을 가리킨다.

```css
padding:20px
```

block level, inline level 로 크게 두 분류로 나눌 수 있다. 

전자는 p 태그 처럼 한 box 당 한 라인으로로 구분지어서 나뉘지만 후자는 a 태그 처럼 한 라인 안에 차지한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="box.css">
</head>
<body>
    <a href="http://daum.net">daum</a>
    <p>박스1<p>박스1 안의 박스</p><a href="http://naver.com">naver</a></p>
    <p>박스2</p>
    <p>박스3</p>
</body>
</html>
```

위와 같이 치면 박스 안에 박스가 포함될 것이라 기대하지만 실제로 그렇지 않다.

<img src ="images/image 004.png">

block level의 특성 때문에 새로운 라인에 박스 하나로 잡혔고 마지막 `</p>`가 잡히지 못해 브라우저가 자체적으로 빈박스를 만들어 위와 같이 출력되었다.

inline은 한 줄에 많이 들어가야하는 상황, 예를 들면 한 줄에 여러 개 버튼을 넣을 때 사용하는 상황일 때 사용한다.

inline 태그는 글자를 꾸며주는 태그들이 해당된다. 밑으로 내리는 것이 block level, 그렇지 않으면 inline level이라 생각하면되는데 억지로 block을 inline으로 또는 그 반대로 만들 수는 있다. 예를 들면 block level인 리스트를 한 줄로 나열시키게 만드는 것이다.

```html
<ul>
    <li style="display:inline">리스트1</li> <!--block을 inline-->
    <li style="display:inline">리스트2</li>
    <li style="display:inline">리스트3</li>
</ul>
<a style="display: block" href="https://naver.com">naver</a> <!--inline을 block-->
```

inline-block은 block과 inline 요소를 모두 갖는다. 

*html*

```html
<span>스팬1</span>
<span>스팬2</span>
<span>스팬3</span>
```

*css*

```css
span{
    display: inline-block;
    margin-top:10px;
    margin-bottom:10px;
    width: 20px;
    height: 30px;
}
```

<img src ='images/image 005.png'>

span을 위와 같이 css를 정하면 세로로 글씨가 나열되어 출력되는 것을 볼 수 있다. 이는 width가 좁아서 밑으로 글씨가 배치되었기 때문이다.

none은 화면상에 아예 나타나지 않게 한다. `visibility: hidden`같은 경우 태그는 존재해서 드래그하면 공간이 있지만 컨텐츠가 보이지 않으나 `display: none`은 아예 보이지 않는다.

# responsive

*responsive.html*

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!--디바이스 폭이 1배 사이즈로 사용, 반응형을 사용할 때 사용-->
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!--bootstrap file-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
    <title>Document</title>
    <style>
        .item{
            background-color: deepskyblue;
        }
    </style>
</head>
<body>
    <!-- container 생성 -->
    <div class="container-fluid">
        <!-- row 생성 -->
        <div class="row"> <!--display: flex로 인해 inline으로 작동됨-->
            <div class="bg-primary col-lg-2 col-md-4 col-sm-2 px-1"> <!-- sm, md, lg, xl이 있음 -->
                글 1
            </div>
            <div class="bg-warning col-lg-2 col-md-4 col-sm-2 px-1">
                글 2
            </div>
            <div class="bg-danger col-lg-2 col-md-4 col-sm-2 px-1">
                글 3
            </div>
            <div class="bg-warning col-lg-2 col-md-4 col-sm-2 px-1">
                글 4
            </div>
            <div class="bg-success col-lg-2 col-md-4 col-sm-2 px-1">
                글 5
            </div>
            <div class="bg-dark col-lg-2 col-md-4 col-sm-2 px-1">
                글 6
            </div>

        </div>
    </div>
</div>
</body>
</html>
```

https://getbootstrap.com/docs/4.2/layout/grid/#grid-options

미디어 쿼리는 디바이스에서 특정 크기에 도달하게 되면 css에 변화를 주어 디자인을 다르게 만들게 한다.

sm, md, lg, xl는  breakpoint를 정하는 위치로 디바이스따라 달라지게 만들 수 있다. 위의 예시처럼 `col` 클래스를 여러 개 쓰면 다양한 디바이스에서 변경되도록 만들 수 있다.

`class="row"`에서 사용하는 `justify-content-center` , `justify-content-end` 등은 중앙정렬, 오른쪽 끝 정렬을 의미한다.