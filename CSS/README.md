## CSS 코딩 팁
### 1. 코드 중복 최소화

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