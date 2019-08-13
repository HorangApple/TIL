# CSS

- [CSS](#css)
  - [1. 코드 중복 최소화](#1-코드-중복-최소화)
  - [2. 선택자](#2-선택자)
    - [Type, className, Sibling](#type-classname-sibling)
    - [Pseudo](#pseudo)
    - [Attribute](#attribute)
  - [3. 조화](#3-조화)
    - [1) 상속](#1-상속)
    - [2) Cascading](#2-cascading)
  - [4. 레이아웃](#4-레이아웃)
    - [1) box-sizing](#1-box-sizing)
    - [2) 마진겹침 현상](#2-마진겹침-현상)
    - [3) position](#3-position)

## 1. 코드 중복 최소화

**편집이 필요한 부분을 최소화**하는 것이 중요하다. 

```css
button {
  padding: 6px 16px;
  border: 1px solid #446d88;
  background: #58a linear-gradient(#77a0bb, #58a);
  border-radius: 4px;
  box-shadow: 0 1px 5px gray;
  color: white;
  text-shadow: 0 -1px 1px #335166;
  font-size: 20px;
  line-height: 30px;
}
```

위 코드에서 유지보수성을 갖추기 위해 수정할 부분은 다음과 같다.

1) 글꼴과 관련된 절댓값(line-height 등)도 같이 변경되어야한다.
- 글꼴의 크기에 따라 줄 간격도 수정되어야 하는데 이 의존하는 두 값을 여러 번 변형할 가능성이 있다. 그래서 모든 효과의 사이즈를 단위 `em`, `%`와 같은 상대적인 크기로 만들어야 글꼴 크기에 따라 변형이 가능하다.

```css
button {
  padding: .3em .8em;
  border: 1px solid #446d88;
  background: #58a linear-gradient(#77a0bb, #58a);
  border-radius: .2em;
  box-shadow: 0 .05em .25em gray;
  color: white;
  text-shadow: 0 -.05em .05em #335166;
  font-size: 125%;
  line-height: 1.5;
}
```

어떤 효과는 비례하여 확대하고 어떤 효과는 그대로 남겨둘지는 선택에 달렸다.

2) 색상 변경은 override를 이용한다.

```css
button {
  padding: .3em .8em;
  border: 1px solid rgba(0,0,0,.1);
  background: #58a linear-gradient(hsla(0,0%,100%,.2),transparent);
  border-radius: .2em;
  box-shadow: 0 .05em .25em rgba(0,0,0,.5);
  color: white;
  text-shadow: 0 -.05em .05em rgba(0,0,0,.5);
  font-size: 125%;
  line-height: 1.5;
}

button.cancel {
  background-color: #c00;
}

button.ok {
  background-color: #6b0;
}
```

밝기/어둡기 변수에 반투명 흰색과 검은색을 사용하여 각각 주 색상에 덮어씌운다.

3) 유지보수성 vs. 간결성
가끔은 유지보수성과 간결성이 상호배타적일 수 있다.

```css
border-width: 10px 10px 10px 0;
```
보다는

```css
border-width: 10px;
border-left-width: 0;
```
로 변경하면 수정하기도 쉽고 읽기도 쉽다.

4) 현재 색상(currentColor)
```css
hr {
  height: .5em;
  background: currentColor;
}
```

SVG에서 차용한 currentColor와 같은 고정된 색상 값이 아닌 css 최초의 변수이다. 요소의 `color` 속성값을 나타낸다. 이 외에도 border-color, the text-shadow, box-shadow, outline-color 등 많은 CSS의 색상 속성의 기본 값이기도 하다.

5) 상속(inherit)
키워드 `inherit`는 어떤 CSS 속성에서도 사용할 수 있고 계산된 부모 요소의 값을 따른다. 특히 `margin`과 같이 상속이 되지 않는 속성을 강제로 상속 시키고 싶을 때 사용한다.

6) 숫자가 아닌 눈을 믿어라!
정확한 측정을 바탕으로 한 결과가 부정확하게 보일 때가 있는데 이는 **착시** 때문이다. 둥근 모양은 실제보다 약간 작게 인식하는 경향과 상자의 각 측면에 일정하게 패딩한 것보다 글자의 길이에 따라 위와 아랫면의 패딩을 적게 두는 것이 더 균일하게 받아들이는 것이 대표적인 예다.

7) 반응형 웹 디자인 (Responsible Web Design, RWD)
일반적인 방법은 다양한 해상도에서 웹 사이트를 테스트하고 문제를 해결하기 위해 점점 더 많은 미디어 쿼리를 추가한다. 그러나 앞으로의 CSS 변화는 **모든 추가된 미디어 쿼리에 대응**해야 하므로 섣불리 추가해서는 안된다. 미디어 쿼리가 늘어날 수록 CSS 코드는 점점 더 깨지기 쉽다.

미디어 쿼리의 한계는 특정 장치에서 동작하지 않아서가 아닌 디자인 그 자체이다. 스마트폰부터 컴퓨터까지 모든 크기의 윈도우에서 잘 보여야한다. 모든 뷰포트 크기에서 잘 동작하는 디자인이면 걱정할 필요는 없지만 현실은 그렇지 않다.

미디어 쿼리를 줄이기 위한 방법은 다음과 같다.

- 폭의 단위는 백분율 또는 뷰포트 관련 단위(vm, wh, wmin, wmax)를 사용하여 뷰포트를 가로 또는 세로로 분할하여 보이도록 한다.

- 큰 해상도에서 고정된 폭을 지정할 때는 `max-width`를 사용하여 작은 해상도에서 미디어 쿼리 없이 적용되도록 한다.

- <img>, <object>, <video>, <iframe>과 같은 대체 요소를 위해 max-width를 100%로 설정한다.

- 배경 이미지가 전체 내용을 커버해야 할 경우 `background-size: cover`를 사용하면 되지만 CSS로 모바일 설계를 할 경우 대역폭(bandwidth)의 한계가 있으므로 큰 크기의 이미지를 포함하는 것은 부적절하다.

- 레이아웃 이미지(또는 다른 요소)가 가로와 세로 그리드가 있을 때 세로 번호가 뷰포트의 너비이다. 유동형 상자 레이아웃(Flexible Box Layout, Flexbox) 또는 `display: inline-block`과 일반적인 줄 바꿈(wrapping)이 도움이 될 수 있다.

- 다단의 텍스트를 사용할 때는 `column-count` 대신에 `column-width`를 지정하여 작은 해상도에서는 한 단만 나타나게 한다.

디자인의 유동성이 충분하다면 여기에는 아주 짧은 미디어 쿼리만 있으면 된다. 만약 원하는 크기의 스크린에 맞출 수 있는 디자인의 미디어 쿼리를 찾았다면 코드 구조를 다시 한 번 재검증하는 것이 좋다.

cf. px 대신 em을 미디어 쿼리에 사용하면 텍스트를 확대했을 때 필요에 따라 레이아웃이 변하게 된다.

8) 단축 속성을 현명하게 사용하라
예를 들어 `background`와 `background-color`는 서로 다르고 전자는 단축 속성(shorthand), 후자는 일반 속성이다. 일반 속성은 단축 속성과 조합하여 사용하는 경우 매우 유용하다.

```css
div {
  background: url(tr.png) no-repeat top right / 2em 2em,
              url(br.png) no-repeat bottom right / 2em 2em,
              url(bl.png) no-repeat bottom left / 2em 2em;
}
```

cf. `/`는 단축 속성에서 사용되는 규칙이며 CSS 파서가 잘 인지할 수 있도록 어떤 속성인지 나눈다.

위 코드처럼 중복되는 부분이 있는데 CSS의 리스트 확장 규칙을 활용하면 아래와 같이 변경할 수 있다.

```css
div {
  background: url(tr.png) top right,
              url(br.png) bottom right,
              url(bl.png) bottom left;
  background-size: 2em 2em;
  background-repeat: no-repeat;
}
```

9) 전처리기를 사용해야하나?
LESS, Sass, Stylus과 같은 CSS 전처리기(Preprocessor)는 적절히 사용하면 CSS 자체만 사용하는 것 보다 대규모 프로젝트에서 코드를 좀 더 유연하게 관리할 수 있다. 그러나 다음과 같은 단점이 있다.

- 복잡하고 파일크기가 커질 수 있다.
- 디버깅이 힘들어진다.
- 개발 프로세스에 지연시간이 추가된다.
- 모든 것을 추상화 시킴으로써 전처리기의 언어를 알지 못하면 협업이 어려울 수 있다.
- 작은 것까지 모두 추상화한다면 빈틈이 생기기 마련이고 전처리기 자체에 버그가 존재할 수 있다.

순수한 CSS로 모든 프로젝트를 시작하였으나 코드를 DRY하게 유지하는 것이 힘들다면 그때 전처리기를 사용하는 것을 권한다. 

## 2. 선택자

http://flukeout.github.io/

### Type, className, Sibling

**A**

해당 html 태그 선택

**#id**

해당 id를 갖고 있는 태그 선택

**A B**

해당 A 이하에 있는 B 태그 선택

**#id A**

해당 id를 갖고 있는 태그 이하에 있는 A 태그 선택

**.className**

해당 class를 갖고 있는 태그 선택

**A.className**

해당 class를 갖고 있는 A 태그 선택

**A, B**

A 태그와 B 태그 선택

**\* **

모든 태그 선택

**A * **

A 태그 이하의 모든 태그 선택

**A + B**

A 뒤에 있는 하나의 B 태그 선택

**A ~ B**

A 뒤에 있는 모든 B 태그 선택

**A > B**

A의 직계 자손인 B 태그 선택

### Pseudo

**A B:first-child**

A 태그 이하의 B의 첫 번째를 선택

**A:only-child**

자식으로 하나만 있는 A 태그 선택

**A:last-child**

맨 마지막에 있는 A 태그 선택

**A:nth-child(X)**

X번 째 A 태그 선택, 이 때 A 태그 이외의 태그도 갯수 X에 영향을 미침

**A:nth-last-child(X)**

뒤에서 X번 째 A 태그 선택, 이 때 A 태그 이외의 태그도 갯수 X에 영향을 미침

**A:first-of-type**

자식, 손자 관련 없이 A 태그의 첫 번째 선택

**A:nth-of-type(X)**

X번 째 A 태그 선택, 이 때 A 태그 이외의 태그는 갯수 X에 영향을 미치지 않음, `odd`, `even`, `Xn+Y`(등차수열) 사용 가능

**A:only-of-type**

한 번밖에 사용되지 않은 A를 선택

**A:last-of-type**

A 태그의 마지막을 선택

**A:empty**

자식이 없는 A 태그 선택

**A:not(X)**

X를 제외한 A 태그 선택

### Attribute

**[attribute]**

해당 속성을 가진 태그 선택

**A[attribute]**

해당 속성을 가진 A 태그 선택

**[attribute="value"]**

해당 속성 값을 가진 태그 선택

**[attribute^="value"]**

해당 속성 값이 "value"로 시작하는 태그 선택

**[attribute$="value"]**

해당 속성 값이 "value"로 끝나는 태그 선택

**[attribute*="value"]**

해당 속성 값이 "value"를 포함하는 태그 선택

## 3. 조화

### 1) 상속

상위 엘리먼트에 `color`를 정하면 하위 엘리먼트에도 적용이 되듯이 상속이 일어난다. 그러나 모든 CSS 속성이 상속이 되는 것은 아니기에 [링크](https://www.w3.org/TR/CSS21/propidx.html)의 표에서 확인해보자.

### 2) Cascading

CSS는 Cascading Style Sheet의 약자로 폭포를 의미하는 Cascading이 있는 만큼 CSS 작성 순서도 영향이 미친다. CSS는 같은 엘리먼트를 꾸미는데 가장 마지막에 선언된 것을 최종으로 반영하거나 `!important`가 붙여있는 속성이 반영된다.

CSS가 적용되는 우선순위가 있는데 **`!important` > style attribute (inline-style) > id selector > class selector > tag selector** 순으로 높다.

## 4. 레이아웃

### 1) box-sizing

박스의 크기를 화면에 표시하는 방식을 변경하는 속성이다. `border-box`로 지정하면 테두리를 포함한 크기를 지정할 수 있어 예측하기가 더 쉽다.

### 2) 마진겹침 현상

상하 마진값이 어떤 상황에서 사라지는 현상을 의미하며 주로 수직(위, 아래)의 마진에서 발생한다. 겹침이 발생하면 마진값이 가장 큰 값을 기준으로 적용된다.

태그가 시각적인 요소(내용, 테두리 등)가 없다면 마진겹침 현상이 발생한다. 이 때 margin-top과 margin-bottom 중 가장 큰 값을 기준으로 한다.

자세한 내용은 [링크](https://www.w3.org/TR/CSS22/box.html#collapsing-margins)를 참고한다.

### 3) position

**static**

left, top, bottom, right와 같은 offset 값을 무시하고 원래 있어야할 곳에 위치한다.

**relative**

자기가 있어야하는 위치에서 상대적으로 이동할 때 사용한다.

**absolute**

부모 엘리먼트의 위치(left, top)를 기준으로 해서 움직인다. 이때 부모로부터 받는 상속은 받지 않게 된다.

**fixed**

부모 엘리먼트의 위치(left, top)를 기준으로 해서 화면상 그 위치에 고정된다. 이때 부모로부터 받는 상속은 받지 않게 된다.

**flex**

엘리먼트들의 크기나 위치를 쉽게 잡아주는 도구이다. 정렬 방향을 나타내는 `flex-direction`를 `column`으로 바꾸면 가로 방향으로 나열할 수 있다.

`flex-basis`는 `flex-direction`의 방향에 따른 크기를 지정해준다. `flex-grow`는 공간을 차지하는 비율을 정할 수 있다. `flex-shrink`는 화면이 작아질 때 공간이 줄어드는 정도를 정할 수 있다.

다른 속성들은 [링크](https://codepen.io/enxaneta/pen/adLPwv)를 참고하자.

### 4) float

편집 디자인에서 이미지를 삽화로 삽입할 때나 레이아웃을 잡을 때 사용하는 기능이다. `float`는 보통 이미지에 적용하여 `left` 또는 `right`로 글자가 흐르게 끔 만들 수 있다. 만약 `float`에 영향을 미치지 않게 하고 싶다면 해당 엘리먼트에 `clear`를 설정하고 `float`와 같은 값을 정의하면 된다. 

### 5) 다단

화면을 분할해서 좀 더 읽기 쉽도록 만든 레이아웃이다. `column-count`를 통해 단의 갯수를 정해 이에 맞게 폭이 가변되고, `column-width`를 이용하여 단의 폭을 정하여 단의 갯수가 가변되도록 만들 수 있다. 만약 두 속성을 같이 사용하게 된다면 `column-count` 이하의 단의 갯수에 `column-width` 이상의 폭을 가진 레이아웃을 구현하게 된다.

각 단의 사이의 폭은 `column-gap`을 통해 정할 수 있으며 `column-rule-style`로 단 사이에 선을 그릴 수 있다. 선과 관련하여 `column-rule-width`, `column-rule-color`로 선 굵기와 색을 정할 수 있다.

어떤 내용이 다단의 영향을 받지 않게 만들고 싶다면 `column-span`을 통해 만들 수 있다.


## 4. 그래픽

### 1) background
- background-color : red
- background-image : url("bg.png")
- background-repeat : repeat, no-repeat, repeat-x, repeat-y
- background-attachment : scroll, fixed
- background-position : left top  or x% y% or x y
- background-size : 100px 100px or cover or contain

### 2) filter
`filter`를 통해 사진, 동영상, 텍스트 등에 다양한 효과를 줄 수 있다. 사용할 수 있는 값은 `blur()`, `grayscale()` 등 있다.

### 3) blend
블랜드는 이미지와 이미지를 혼합해서 새로운 이미지를 만들어내는 기법이다. 

- `background-blend-mode`: `background-color`와 `background-image`를 섞어서 새로운 효과를 만들 수 있다.

- `mix-blend-mode`: 꾸미고자 하는 컨텐트에 `mix-blend-mode` 속성을 입력하면 그 컨텐트의 배경이 되는 `background-image`에 맞춰 효과를 보여준다.

### 4) transform

https://codepen.io/vineethtr/pen/XKKEgM

`display`가 `inline`이면 작동되지 않는다.

```css
.trans{
  /* Keyword values */
  transform: none;
  
  /* Function values */
  transform: matrix(1.0, 2.0, 3.0, 4.0, 5.0, 6.0);
  transform: translate(12px, 50%);
  transform: translateX(2em);
  transform: translateY(3in);
  transform: scale(2, 0.5);
  transform: scaleX(2);
  transform: scaleY(0.5);
  transform: rotate(0.5turn);
  transform: skew(30deg, 20deg);
  transform: skewX(30deg);
  transform: skewY(1.07rad);
  transform: matrix3d(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0);
  transform: translate3d(12px, 50%, 3em);
  transform: translateZ(2px);
  transform: scale3d(2.5, 1.2, 0.3);
  transform: scaleZ(0.3);
  transform: rotate3d(1, 2.0, 3.0, 10deg);
  transform: rotateX(10deg);
  transform: rotateY(10deg);
  transform: rotateZ(10deg);
  transform: perspective(17px);
  
  /* Multiple function values */
  transform: translateX(10px) rotate(10deg) translateY(5px);
  
  /* Global values */
  transform: inherit;
  transform: initial;
  transform: unset;
}
```

이 외에도 `transform-origin`을 사용하여 어느 축을 기준으로 회전할 지도 정할 수 있다.

### 5) transition

- transition-duration: transition 시간을 정함
- transition-property: 어느 속성에 transition 효과를 적용할 지 정함
- transition-delay: transition 후 지연할 시간을 정함
- transition-timing-function: transition의 효과(속도)를 정함 [참고](https://matthewlein.com/tools/ceaser)
- transition

## 5. 유지보수

### 1) link와 import

아래의 두 가지 방법으로 CSS 파일을 불러온다.

1. `<link rel="stylesheet" href="style.css">`

2. `<style>@import url("style.css")</style>`

### 2) 코드 경량화 (minify)

서버와 클라이언트에게 소모되는 자원을 줄이기 위해 경량화시킨다. [참고](http://adam.id.au/clean-css-online/)와 같이 줄바꿈, 띄어쓰기를 없애준다.