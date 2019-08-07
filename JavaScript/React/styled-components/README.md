# styled-components

*본 문서는 [styled-components의 공식문서](https://www.styled-components.com/docs/)를 바탕으로 정리한 내용이다.*

## 1. 개요
styled-components는 React의 컴포넌트 시스템에 맞는 보다 쉬운 스타일링을 할 수있도록 도와준다.

## 2. 설치
```bash
$ npm install --save styled-components
또는 
$ yarn add styled-components
```

## 3. 기초
### 1) 기본
styled-components를 사용하기 위해 아래와 같이 import를 한다.

```javascript
import styled from 'styled-components'
```

styled-components는 `styled.요소이름`으로 작성 후 javascript의 문법 중 Backtick( \` )을 사용하는  **tagged template**을 사용한다.

```javascript
import React from "react"; // 이하 생략
import styled from "styled-components"; // 이하 생략

const Title = styled.h1`
  /* 주석 */
  font-size: 1.5em;
  text-align: center;
  color: palevioletred;
`;

const Wrapper = styled.section`
  padding: 4em;
  background: papayawhip;
`;

const Example = () => (
  <Wrapper>
    <Title>hi</Title>
  </Wrapper>
);

export default Example; // 이하 생략
```

styled-components를 통해 CSS 파일을 따로 정의할 필요가 없다. tagged template 문법으로 스타일을 정의하고 일종의 컴포넌트로 사용한다. 웹 브라우저의 개발자 모드로 관찰을 하면 스타일 요소는 모두 클래스 형식으로 요소에 부여가 되는데 styled-components가 정한 임의의 이름으로 클래스가 부여되기 때문에 다른 컴포넌트에서 같은 요소를 스타일링 해도 중첩될 일이 없다. 즉, styled-components를 사용하면 A 컴포넌트의 h1의 스타일과 B 컴포넌트의 h1의 스타일은 독립적으로 작동된다는 것이다.

**주의할 점**
스타일을 정의할 때는 컴포넌트 선언 밖에서 선언이 이루어져야 한다. 만약 컴포넌트 선언 안에서 정의하게 되면 성능이 떨어지게 된다.

### 2) props
React에서 props를 통해 자식 컴포넌트에게 상태를 넘기는 것과 같이 styled-components로 정의한 스타일에 props를 전달하여 스타일을 조작할 수 있게 해준다.

```javascript
const Button = styled.button`
  background:${props => props.primary?
  "palevioletred":"white"};
  color:${props=>props.primary?"white":
"palevioletred"};

  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
`;

const Example = () => (
  <div>
    <Button>Normal</Button>
    <Button primary={true}>Primary</Button>
  </div>
);

```
React에서 사용한 것과 마찬가지로 넘겨줄 변수 이름과 스타일 내부의 props의 property 이름과 동일하도록 작성해야한다.


### 3) 상속
이미 정의된 스타일을 재사용 할 수 있는 상속이 가능하다.

```javascript
const Button = styled.button`
  background:${props => props.primary?
  "palevioletred":"white"};
  color:${props=>props.primary?"white":
"palevioletred"};

  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
`;

const TomatoButton = styled(Button)`
    color: tomato;
    border-color: tomato;
`

const Example = () => (
  <div>
    <Button primary>Primary</Button>
    <TomatoButton>Tomato Button</TomatoButton>
  </div>
);

```

소괄호 `(, )`를 이용하여 상속을 통해 재활용하고 오버라이딩으로 커스텀마이징을 할 수 있다.

반면, 같은 스타일이지만 다른 요소로 사용하고 싶을 때는 `as`를 이용하여 요소를 바꿀 수 있다.

```javascript
const Button = styled.button`
  background:${props => props.primary?
  "palevioletred":"white"};
  color:${props=>props.primary?"white":
"palevioletred"};

  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
`;

const TomatoButton = styled(Button)`
    color: tomato;
    border-color: tomato;
`

const Example = () => (
  <div>
    <Button primary>Primary</Button>
    <TomatoButton as="a" href="/">Tomato Button</TomatoButton>
  </div>
);

```

as를 통해 원하는 요소로 바꾸고 그 요소에 해당하는 속성값도 같이 적으면 적용이 된다. 기존의 html 요소뿐만 아니라 직접만든 컴포넌트도 as에 넣을 수 있다. 이때는 중괄호를 통해서 넣어줘야한다.

### 4) 기존 컴포넌트 스타일링하기
지금까지의 과정은 컴포넌트를 만들면서 스타일링을 하는 것이지만 반대로 만들어진 컴포넌트를 꾸미는 것도 가능하다.

```javascript
const Link = ({className, children}) => (
  <a className={className}>{/* className이 props를 받도록 해야한다. */}
    {children}
  </a>
);

const StyledLink = styled(Link)`
  color: palevioletred;
  font-weight: bold;
`;

const Example = () => (
  <div>
    <Link>Unstyled Link</Link>
    <br />
    <StyledLink>Styled Link</StyledLink>
)

```

단, 위와 같이 별도로 props를 통해 className에 적용할 수 있도록 만들어야 가능하다.

### 5) 가상 요소, 가상 선택자, 중첩
styled-components는 [**stylis**](https://github.com/thysultan/stylis.js)라는 전처리기를 사용하고 있다. 따라서 SCSS와 같은 문법을 사용할 수 있는데 가상 요소, 가상 선택자, 중첩이 그것이다.

```javascript
const Thing = styled.div.attrs(() => ({
  tabIndex: 0
}))`
  color: blue;

  &:hover {
    color: red; // <Thing> when hovered
  }

  & ~ & {
    background: tomato; // <Thing> as a sibling of <Thing>, but maybe not directly next to it
  }

  & + & {
    background: lime; // <Thing> next to <Thing>
  }

  &.something {
    background: orange; // <Thing> tagged with an addtional CSS class ".something"
  }

  .something-else & {
    border: 1px solid; // <Thing> inside another element labeled ".something-else"
  }
`;

const Example = () => (
  <React.Fragment>
    <Thing>Hello world!</Thing>
    <Thing>How ya doing?</Thing>
    <Thing className="something">The sun is shining...</Thing>
    <div>Pretty nice day today.</div>
    <Thing>Don't you think?</Thing>
    <div>Pretty nice day today.</div>
    <div>Pretty nice day today.</div>
    <Thing>Don't you think?</Thing>
    <div className="something-else">
      <Thing>Splendid.</Thing>
    </div>
  </React.Fragment>
);
```

또한 


```javascript
import styled, {createGlobalStyle} from 'styled-components';

const Thing = styled.div`
  && {
    color: blue;
  }
`

const Thing2 = styled.div`
`

const GlobalStyle = createGlobalStyle`
  div${Thing2} {
    color: red;
  }
`
const Example = () => (
  <React.Fragment>
    <GlobalStyle />
    <Thing>
      Thing
    </Thing>
    <Thing2>
      Thing2
    </Thing2>
    <div>
      hi
    </div>
  </React.Fragment>
);
```

`createGlobalStyle`는 styled-components에서 제공하는 일종의 helper 함수로 전역으로 스타일을 설정할 수 있고 `${}`를 이용해 특정 요소만 꾸밀 수 있도록 할 수 있다.

### 6) props 조작
`.attr`를 통해 스타일에 적용하기 전에 props를 받아 조작한 후에 스타일에 사용할 수 있도록 할 수 있다.

```javascript
const Input = styled.input.attrs(props => ({
  // static props
  type: "password",

  // dynamic props
  size: props.size || "1em",
}))`
  color: palevioletred;
  font-size: 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;

  /* dynamically computed prop */
  margin: ${props => props.size};
  padding: ${props => props.size};
`;

const Example = () => (
  <div>
    <Input placeholder="A small text input" />
    <br />
    <Input placeholder="A bigger text input" size="2em" />
  </div>
);
```

이를 통해 동적으로 스타일링을 할 수 있다.

### 7) 애니메이션
`@keyframes`를 사용한 CSS 애니메이션은 한 컴포넌트에 스코프가 맞춰있지 않는데 styled-components에서 제공되는 `keyframes`를 활용하면 유일한 인스턴스를 생성하여 사용할 수 있다.

```javascript
import styled, {keyframes} from "styled-components";

// Create the keyframes
const rotate = keyframes`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`;

const Rotate = styled.div`
  display: inline-block;
  animation: ${rotate} 2s linear infinite;
  padding: 2rem 1rem;
  font-size: 1.2rem;
`;

const Example = () => (
  <Rotate>&lt; 💅 &gt;</Rotate> // &lt;, &gt;는 간접 표현식
);
```

## 4. 심화

## 5. 그 외
- styled-components에서 `<input>`을 사용할 때 일반적인 html과 다르게 `value`는 읽기 전용으로 렌더링이 된다. 이 때는 `defaultValue`를 사용하는 것이 좋다.
- `<label>`에서 for는 `htmlFor`로 사용된다.