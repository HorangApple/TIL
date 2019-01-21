# Web Service

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

