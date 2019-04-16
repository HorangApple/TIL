# Chapter 1. 리액트를 만나다

## 1.1 리액트 시작하기

리액트는 강력한 멘탈 모델과 더불어 선언적이면서도 컴포넌트 주도적인 방법으로 사용자 인터페이스를 개발하기 위한 다양한 기능을 제공한다. 

리액트의 멘탈 모델은 함수적(functional) 개념과 객체지향(object-oriented)을 결합하고 있으며, 컴포넌트를 UI 개발의 주요 단위로 보고 있다. 

리액트의 렌더링(rendering) 시스템은 이 컴포넌트들을 관리하여 애플리케이션의 뷰(view)와 동기화한다. 컴포넌트는 날짜 선택, 머리글 영역, 탐색 메뉴 영역 등의 사용자 인터페이스를 구현하는 데 사용하기도 하지만, 클라이언트 측 라우팅(routing), 데이터 형식화(data formatting), 스타일과 같은 클라이언트 측 애플리케이션의 다른 부분들을 관장하기도 한다.

주로 사용되는 재료들은 다음과 같다.

- 컴포넌트 : 리액트에서 구현하고자 하는 기능을 캡슐화하는 기본 단위, 데이터(속성 및 상태)를 다루며, 그 결과로 UI를 렌더링한다.
- 리액트 라이브러리 : React-dom 라이브러리는 브라우저환경 및 서버 측 렌더링 기능의 구현을 목적으로 하고 있고 React-native 라이브러리는 네이티브 플랫폼에서의 UI 렌더링을 위한 라이브러리로 다른 플랫폼을 위한 리액트 애플리케이션을 개발할 때 활용한다.
- 서드파티 라이브러리 : 리액트는 데이터 모델링(data modeling), HTTP 호출, 스타일 조정 및 기타 프런트엔드 애플리케이션이 필요하는 기능들을 지원하지 않는다. 대신에 리액트를 지원하는 다양하고 유용한 라이브러리가 존재한다.
- 리액트 애플리케이션의 실행 : 리액트 네이티브와 리액트 VR 같은 다른 프로젝트들을 이용할 수 있다.

```bash
# 설치
npm install -g create-react-app
# 프로젝트 생성
create-react-app 프로젝트이름

# 로컬 서버 구동
npm start
```

위와 같이 bash에서 입력하여 설치하고 프로젝트를 생성한다.

## 1.2 리액트가 적합하지 않은 경우

리액트는 사용자 인터페이스를 구현하기 위한 컴포넌트 기반의 선언적(declarative) 라이브러리로, 웹, 네이티브 모바일, 서버, 데스크톱 및 나아가 가상현실 플랫폼 등 다양한 플랫폼에서 동작한다. 그러나 다음과 같은 트레이드 오프가 존재한다.

- 리액트는 UI 관점에서의 뷰를 가장 우선시한다. 즉, 다른 포괄적인 프레임워크나 라이브러리보다 기본적으로 제공되는 기능이 적다. 그러나 그만큼 유연하여 필요한 작업을 수행하기 위한 최선의 도구를 선택할 수 있다.
- 유연한 만큼 특정 영역의 문제를 독자적으로 해결해야한다.
- 프레임워크에 대한 결속이 약해 낮은 비용으로 마이그레이션(migration)이 가능하다.
- 페이스북이 주도한 개발 도구이기 때문에 페이스북 앱의 UI 요구사항과 상당히 다른 앱을 개발한다면 리액트를 활용하는 데 어려움을 겪을 수 있다.
- 컴포넌트 내의 데이터가 변경되었을 때 이를 처리하여 UI를 갱신하는 시스템으로 개발자가 생명주기 메서드(lifecycle method)라고 부르는 특정한 메서드를 이용해 감지한 변경 사항들을 실행하는 방식이다.  이러한 시스템이 모듈화되어 대부분의 작업을 추상화한다. 즉, 리액트가 정해 준 방식대로 UI를 개발해야 한다는 뜻이다. 리액트와 호환되는 방식으로 도구를 사용해야한다.
- 기반 시스템의 일부를 확인할 수 없고 리액트가 동작하는 방식으로 앱을 개발해야 한다.  이러한 점이 애플리케이션 스택의 이부분에 영향을 미친다.

## 1.3 가상 DOM

리액트는 선언적(declarative) 방법을 사용하도록 유도한다. 개발자는 컴포넌트가 어떻게 동작하는지, 그리고 여러 상태를 어떻게 보여줄 것인지를 선언하며, 리액트의 내부 메커니즘은 컴포넌트의 상태 변경과 이를 UI에 반영하는 작업 등에 필요한 복잡한 과정을 처리한다.

이 과정을 처리하는 주요 기법이 가상 DOM이다. 리액트의 가상 DOM은 브라우저에 존재하는 문서 객체 모델(Document Object Model)을 흉내 내거나 반영하는 데이터 구조 또는 데이터 구조의 모음(collection)이다.

일반적으로 가상 DOM은 변경의 탐지 및 관리에 필요한 복잡한 작업을 최대한 숨기고, 개발자가 특별한 추상화 계층에 집중하는 데  도움을 준다.

### 1.3.1 DOM

DOM 또는 문서 객체 모델은 JS 프로그램이 다양한 종류의 문서(HTML, XML 또는 SVG 등)를 다루기 위한 프로그래밍 인터페이스다. 이 인터페이스는 표준 명세를 바탕으로 구현된다. 즉, 이 인터페이스가 제공해야 할 표준 기능과 그 동작은 공개 작업 그룹(public working group)이 정의한다는 뜻이다.

DOM은 XML 문서의 계층 구조를 반영한 트리 구조(tree structure)다.

HTML 문서 내의 무언가와 관련된 정보에 접근하고 갱신하거나 저장하는 JS 메서드를 사용한다면 거의 확실히 DOM 또는 그와 관련된 API들을 사용하는 것이다.

리액트를 이용해 애플리케이션을 개발하면 DOM을 직접 조작할 경우가 별로 없다. 리액트가 웬만한 작업을 대신 해주기 때문이다.

### 1.3.2 가상 DOM

대형 웹 애플리케이션을 개발하다 보면 직접 DOM을 조작하기가 매우 어려운 경우가 있다. 이런 어려움은 변경 사항을 탐지하려 할 때 드러난다. 일반적으로 데이터가 변경되면 이 변경 사항을 반영하기 위해 UI를 갱신해야 한다.

브라우저가 DOM 요소(element)에 액세스하고 이를 갱신하거나 새로 생성하기 위해서는 지정된 요소를 구조화된 트리 구조로부터 조회해야 한다. 이후 레이아웃, 크기 및 변경을 위한 기타 여러 동작을 수행해야 하며, 이러한 작업은 복잡한 계산이 요구된다.

가상 DOM은 이런 제약을 처리하기 위해 DOM의 갱신을 최적으로 수행한다. 리액트의 가상 DOM은 단지 '충분히 빠르게' 하기 위한 것이다. 성능도 장점이지만 간결함이 그보다 더 우선하는 요소이기에 가상 DOM은 복잡한 상태 관리 로직에서 벗어나 애플리케이션에서 더 중요한 부분에 집중하도록 도와주는 요소의 일부일 뿐이다.

### 1.3.3 갱신과 변경 비교

그래픽 카드가 필요한 최소한의 변경만 처리하듯이 가상 DOM이 그 역할을 한다. 리액트는 메모리에 가상 DOM을 생성하고 관리하여 가상 DOM의 변경 사항을 브라우저 DOM에 반영한다. 이 동작은 메모리의 DOM에서 발생한 변경 사항이 실제 DOM의 변경을 유발한다고 판단되는 경우에만 수행된다. 이러한 방식은 개발자들의 상태 추적이 훨씬 간편해진다는 장점을 가져다준다.

## 1.4 컴포넌트: 리액트의 기본 단위

컴포넌트는 리액트의 가장 기본적인 단위다.

### 1.4.1 컴포넌트의 정의

컴포넌트를 멘탈 및 시각화 도구로 사용하는 것은 훨씬 더 나은 방법인 동시에 더욱 직관적인 애플리케이션의 디자인과 사용법을 정의할 수 있다.

컴포넌트는 우리가 정의하는 어떤 형태로든 구현할 수 있다. 설령, 그것이 컴포넌트로서 적합한 형태가 아닐지라도 말이다. 

### 1.4.2 리액트의 컴포넌트: 캡술화와 재사용

리액트의 컴포넌트는 캡슐화되어 있으며, 재사용 및 재구성을 할 수 있다. 덕분에 간결한 컴포넌트를 조합해서 애플리케이션을 개발할 수 있다. 컴포넌트를 만들 때는 반드시 한 번은 재사용할 컴포넌트를 만들도록 해야한다.

리액트 기반의 컴포넌트를 정의할 때는 컴포넌트 디자인에서 그 구조와 일관성에 대해 고려하는 것이 중요하다.

다른 라이브러리에 의존하는 컴포넌트라 하더라도 잘 디자인된 리액트 컴포넌트는 애플리케이션의 다른 영역과 충분히 잘 어울릴 수 있다.  컴포넌트 간의 경계는 기능의 분할과 잘 정의된 애플리케이션 구조를 확보할 수 있다는 것을 의미하지만, 독립적인 컴포넌트는 재사용성과 이동성을 의미한다.

컴포넌트는 상호작용, 즉 여러 컴포넌트를 '조합(compose)'해서 새로운 형태의 '합성(composite)' 컴포넌트를 만들 수도 있다. 컴포넌트의 조합은 리액트의 가장 강력한 장점 중 하나다.

컴포넌트 안에 있는 '생명주기 메서드'는 예측이 가능하며, 컴포넌트가 다른 생명주기 시점(마운팅, 갱신, 언마운팅 등)으로 이동할 때 활용할 수 있도록 잘 정의되어 있다.

# Chapter 2 첫 번째 컴포넌트

## 2.1 리액트의 컴포넌트에 대해 알아보기

컴포넌트는 리액트로 작성된 클라이언트 측 애플리케이션을 구성하는 기본 단위이다. 컴퓨넌트를 기반으로 사용자 인터페이스를 구성하고 이를 바탕으로 구조를 잡아야한다. 

이후 애플리케이션이 필요로 하는 데이터에 대해 이해한 후 이 데이터를 어떻게 컴포넌트로 만들 수 있는지 생각해본다.

### 2.1.1 애플리케이션 데이터를 살펴보자

디자인 시안 외에 API가 애플리케이션에 어떤 데이터를 제공해 주는지 알아야한다. 디자인 시안을 보면 API로부터 어떤 데이터가 전달될 것인지 어렴풋이 짐작할 수 있다. 이처럼 애플리케이션 데이터의 형태를 아는 것은 UI 개발 시작에 앞서 계획을 수립하는 데 있어 매우 중요한 부분이다.

참고로 **API**(Application Programming Interface)는 프로그램이나 플랫폼과 상호작용을 하기 위해 정해진 것을 외부에 노출하는 방법이며, 쉬운 사용을 위해 대부분 인터넷을 통해 제공된다. 서버로부터 제공되는 데이터는 **REST 형식의 JSON API**가 많이 사용된다. JSON을 통해 데이터가 어디에 어떻게 사용될 것인지 살펴볼 수 있다.

### 2.1.2 다중 컴포넌트: 컴포넌트의 조합과 부모-자식 관계

DOM 요소들과 마찬가지로, 리액트의 컴포넌트들은 중첩(nested)할 수 있으며, 다른 컴포넌트를 포함할 수 있다. 물론 다른 컴포넌트와 같은 계층에 컴포넌트를 배치할 수 있다. 컴포넌트들은 여러 가지 '짐스러운' 것을 가지고 있지 않기 때문에 매우 유연하게 조합이 가능(composible)하다.

컴포넌트가 컴포넌트를 포함하고 있다면 이 컴포넌트는 **부모 컴포넌트**가 되며, 반대로 다른 컴포넌트 내에 포함된 컴포넌트는 **자식 컴포넌트**가 된다. 컴포넌트에 있어서는 오로지 부모와 자식 관계만이 중요하다.

### 2.1.3 컴포넌트 간의 관계 확립

컴포넌트의 계층 구조를 정의하면 다음과 같다. 

- 인터페이스의 어느 부분이 컴포넌트가 될 것이며, 어디에 배치할 것인지에 대해 계획을 세워야 한다.
- 컴포넌트의 관계는 시간이 지나면서 달라질 수 있으므로 처음부터 너무 완벽해지려는 욕심을 부리지 않는다.
- 컴포넌트를 적절하게 그룹화시킨다. 서로 관련된 기능을 제공하는 것들로 구성해야 한다. 컴포넌트를 애플리케이션 내에 자유롭게 배치하기 어렵다면 계층 구조를 너무 견고하게 정의했기 때문일 수도 있다.
- 인터페이스의 어떤 요소가 여러 번 반복되어 나타난다면 이런 요소들은 컴포넌트로 정의한다.

## 2.2 리액트 컴포넌트 개발하기

```javascript
// index.js
const node = document.getElementById("root");

// index.html
<div id="root"></div>
```

우선, ID 값이 root인 DOM 요소를 추가하고 React-dom 라이브러리를 사용하는 약간의 기본 코드를 작성한다.

컴포넌트는 요소를 그룹화하는 방법이며 기능, 마크업, 스타일 그리고 기타 UI에 필요한 다른 요소들을 하나로 묶어 그룹화한다.

### 2.2.1 리액트 요소 생성하기

***React.createElement***

**리액트 요소**란 경량이고 상태가 없으며 내부 상태의 변경이 불가능한 요소이다. 두 가지 타입이 있는데 **ReactDOMElement**는 DOM 요소를 가상으로 표현한 객체이고 **ReactComponentElement**는 리액트 컴포넌트를 표현하는 함수나 클래스에 대한 참조를 의미한다.

요소(element)란 우리가 화면에서 보고자 하는 것들에 대해 리액트에게 설명해 주는 서술자(descriptor)며, 리액트의 중심에 있는 개념이다. 대부분의 컴포넌트는 리액트 요소의 컬렉션이 될 것이다.

UI를 구성하는 가장 기본적인 요소이기 때문에 UI의 각 영역에 '경계(boundary)'를 생성하기 때문에 기능과 마크업, 스타일 등을 함께 그룹화할 수 있다.

DOM 요소와 리액트 요소 사이의 유사성은 멘탈 모델을 지원하기 위한 것이며, 일반적인 DOM 요소들과 마찬가지로 트리 구조의 요소들로 구성된 익숙한 멘탈 모델을 다루게 된다.

다른 한편으로, 리액트 요소는 DOM 요소의 청사진(blueprint)처럼 리액트가 사용하는 기본적인 지시문의 집합으로 이해할 수 있다.  즉, 리액트가 요소를 생성하고 관리할 때 사용하는 간소화된 버전의 청사진이라고 할 수 있다.

```javascript
React.createElement(
  String/ReactClass type,
  [object props],
  [children...]
) -> ReactElement
```

React.createElement 함수는 문자열이나 (React.Component 타입을 상속한) 컴포넌트, prop 객체, 그리고 자식 컴포넌트들을 인수로 전달받아 리액트 요소를 리턴한다.

- type : 생성할 HTML 요소의 태그 이름을 문자열로 전달하거나 리액트 클래스를 전달한다. '리액트가 생성할 타입'을 지정한다.

- props : 속성(properties)의 줄임말이며 ReactDOMElement인 경우 HTML 요소에 지정될 특성(attributes)을 지정하거나 컴포넌트 클래스 인스턴스에 사용할 속성들을 지정한다.
- childern : 컴포넌트들을 전달하면 순서대로 해당 컴포넌트를 중첩하거나 다른 리액트 요소를 중첩할 수 있게 해준다.

### 2.2.2 컴포넌트의 렌더링

리액트는 개발자가 만든 리액트 요소를 이용해 가상 DOM을 만들고, React-dom 라이브러리는 이 가상 DOM을 활용해 실제 브라우저 DOM을 관리한다. 리액트는 실제로 어떤 동작을 수행하기 위해 리액트 요소들로부터 가상 DOM을 위한 트리 구조를 만들어 내야 한다.

React.createElement 함수 호출에 전달된 `children...` 매개변수들을 재귀적으로 평가해서 그 결과를 부모 요소에 전달한다.

***ReactDOM.render***

실제로 브라우저에서 뭔가를 보기 위해서는 react-dom을 이용해야 한다. 즉, 컴포넌트를 생성하고 관리하기 위해서는 리액트의 render 메서드를 호출해서 컴포넌트와 컴포넌트 요소(앞서 선언한 변수에 저장해 둔 DOM 요소)를 렌더링해야 한다.

```javascript
ReactDOM.render(
  ReactElement element,
  DOMElement container,
  [function callback]
) -> ReactComponent
```

React DOM은 ReactElement 타입의 요소와 DOM 요소를 필요로 한다. DOM 요소(div)는 이미 만들었지만, 리액트 요소는 아직 만들지 않았다.

### 2.2.4 리액트 클래스 생성하기

함수를 기반으로 생성한 컴포넌트는 리액트 요소와 유사하지만, 더 많은 기능을 제공한다. 컴포넌트는 React.Component 기반 클래스를 확장하거나 함수를 이용해서 생성한다.

리액트 클래스를 생성하는 방법은 다음과 같다.

```javascript
class MyReactClassComponent extends Component {
    render() {}
}
```

React.Component 추상 기반 클래스를 상속하는 JS 클래스를 선언하면 된다. 이 기반 클래스를 상속하는 클래스는 대부분 하나의 리액트 요소 또는 리액트 요소의 배열을 리턴하는 render 메서드를 정의한다.

리액트 클래스를 이용해서 컴포넌트를 생성하면 props 객체에 접근할 수 있다. 이 객체는 컴포넌트에 전달할 수 있는 데이터이며, 해당 컴포넌트의 자식 컴포넌테에도 전달할 수 있다. props는 컴포넌트 내부에서 수정해서는 안 되지만, 데이터를 갱신하는 방법이 있다.

props 객체가 사용되는 형태는 Jedi처럼 임의의 HTML 요소에 'name'이라는 특성을 정의해서 `<Jedi name="Obi Wan"/>`같은 태그를 만들어 내는 것과 비슷하다.

this는 컴포넌트의 인스턴스를 가리킨다.

메서드를 개발자가 .bind 함수를 이용해 직접 바인딩해 주어야 한다.

### 2.2.5 render 메서드

화면에 뭔가를 출력하는 컴포넌트라면 반드시 render 메서드를 정의한다. render 메서드는 반드시 단 하나의 리액트 요소를 리턴해야 한다. (버전 16부터는 여러 개도 가능)

리액트 요소들은 중첩할 수 있지만, 최상위에는 단 하나의 노드만이 존재하는 것과 같다. 하지만 리액트 클래스의 render 메서드는 내부 데이터(컴포넌트 내부에 저장된 상태)뿐만 아니라 컴포넌트 메서드와 React.Component 추상 기반 클래스로부터 상속된 추가 메서드에도 접근이 가능하다.

이것이 가능한 이유는 컴포넌트에 대한 '보조 인스턴스(backing instance)'를 생성하기 때문이고 이런 컴포넌트를 **상태가 있는** 컴포넌트라고 부른다.

리액트는 (청사진이 아닌) 리액트 클래스의 인스턴스에 대한 특별한 데이터 객체인 보조 인스턴스를 생성하고 변경사항을 계속 추적한다. 인스턴스에 저장된 데이터는 특정 API 메서드를 통해 컴포넌트의 render 메서드에서 접근이 가능하다. 즉, 사용자가 애플리케이션을 이용하면서 변경되는 부분을 데이터에 반영하고 저장할 수 있다는 뜻이다.

### 2.2.6 PropTypes를 이용한 속성의 유효성 검사

사용하고자 하는 속성에 대한 유효성 검사를 수행할 방법을 제공해서 버그를 예방하고, 컴포넌트가 사용할 데이터의 종류에 대한 계획을 세워야한다. 이러한 유효성 검사는 React 네임스페이스 내에 정의된 유효성 검사 도구(validators)인 PropTypes 객체를 이용하면 된다. 버전 15.5 이후로 prop-types 패키지를 별도로 설치해야한다.

PropTypes는 다른 개발자가 올바른 값을 제공하지 않으면 제대로 동작하지 않기 때문에 반드시 만족하는 조건(contract)을 지정하는 방법이다.

PropTypes를 사용하려면 React.Component 클래스에 propTypes 속성을 추가해야 한다.

PropTypes는 개발 모드에서만 타입을 평가하기 때문에 실제 운영 환경에서 실행중인 PropTypes를 동작하는 추가적인 오버헤드가 발생하지 않는다.

*예제 2.5*

``` javascript
// React, React DOM, 그리고 prop-types 라이브러리를 불러온다.
import React, { Component } from "react";
import { render } from "react-dom";
import PropTypes from "prop-types";

const node = document.getElementById("root");

// Post 컴포넌트로 사용할 리액트 클래스를 생성, propTypes 속성과 render 메서드를 정의한다.
class Post extends Component {
  render() {
    return React.createElement(
      "div",
      {
        className: "post"
      },
      React.createElement(
        "h2",
        {
          className: "postAuthor",
          id: this.props.id
        },
        // this는 리액트 클래스가 아닌 현재 컴포넌트 인스턴스를 참조
        this.props.user,
        React.createElement(
          "span",
          {
            // DOM 요소에 CSS클래스 이름을 지정할 때 className을 이용
            className: "postBody"
          },
          this.props.content
        ),
        // 자식 컴포넌트를 렌더링할 수 있도록 추가, 중첩된 데이터의 배출구 같은 역할
        this.props.children
      )
    );
  }
}

// 속성은 반드시 필요한 값일수도, 선택적인 값일 수도 있으며, 
// 타입을 명시해야 하고 특정한 '형태'여야 할 수도 있다.
Post.propTypes = {
  user: PropTypes.string.isRequired,
  content: PropTypes.string.isRequired,
  id: PropTypes.number.isRequired
};

// Comment 컴포넌트 생성
class Comment extends Component {
  render() {
    console.log("yo");
    return React.createElement(
      "div",
      {
        className: "comment"
      },
      React.createElement(
        "h2",
        {
          className: "commentAuthor"
        },
        this.props.user,
        React.createElement(
          "span",
          {
            className: "commentContent"
          },
          this.props.content
        )
      )
    );
  }
}
// propTypes 속성 선언
Comment.propTypes = {
  id: PropTypes.number.isRequired,
  content: PropTypes.string.isRequired,
  user: PropTypes.string.isRequired
};

// Post 리액트 클래스와 필요한 속성들을 전달하면 React-dom 라이브러리가 이 컴포넌트를 렌더링한다.
const App = React.createElement(
  Post,
  {
    id: 1,
    content: " said: This is a post!",
    user: "mark"
  },
  // Post 컴포넌트에 Comment 컴포넌트를 중첩한다.
  React.createElement(Comment, {
    id: 2,
    user: "bob",
    content: " commented: wow! how cool!"
  }) // Comment에 this.props.children가 추가되어있지 않아 중첩이 불가능하다.
);

render(App, node);
```

## 2.3 컴포넌트의 수명과 시간

리액트 클래스는 React.Component 클래스의 서브 클래스이며, React.createdElement 메서드에 전달할 수 있다. 리액트 클래스로 생성한 컴포넌트는 데이터를 저장하기 위한 지원 인스턴스를 가지고 있으며, 단 하나의 리액트 요소를 리턴하는 render 메서드를 정의해야한다.

리액트는 리액트 요소를 이용해 메모리상에 가상 DOM을 생성한 후 실제 DOM을 관리하고 갱신한다.

리액트는 컴포넌트에 어떤 기능이든 추가할 수 있는 자유도와 유연성을 제공한다. 개발자가 필요에 따라 직접 메서드를 추가할 수도 있다.

### 2.3.1 리액트의 상태

컴포넌트에 저장할 수 있는 상태(데이터, state)를 제공한다. 이 상태는 지원 인스턴스를 통해 관리한다. 상태는 어느 특정 시점의 어떤 것에 대한 정보라고 생각한다.

상태의 종류는 크게 **변경 가능한(mutable) 상태**와 **변경 불가능한(immutable) 상태**로 구분할 수 있다. 어떤 상태가 처음 생성된 이후에 변경할 수 있다면 가변 상태이고, 그렇지 않다면 불변 상태이다.

React.Component 클래스를 확장한 컴포넌트는 가변(state) 또는 불변 상태(props)를 모두 관리 할 수 있지만, 함수를 이용해 생성한 컴포넌트(상태가 없는 함수 컴포넌트)는 불변 상태만을 관리할 수 있다.

this.props 속성은 컴포넌트 내에서 변경할 수 없지만 전달하는 방법은 있다. 두 속성을 이용하는 방법은 함수에 전달되거나 함수 내에서 사용되는 데이터를 이용하는 방법과 거의 같다. 사실 state, props는 동적 혹은 정적 데이터를 UI에서 활용하는(사용자 정보의 표시, 이벤트 핸들러, 데이터 전달하기 등) 가장 기본적인 방법이다.

### 2.3.2 기본 상태 설정하기

사용자의 폼 요소와 상호작용을 계속 추적하려면 기본 상태를 제공하고 이후 시간의 흐름에 따라 상태를 변경해야 한다. 컴포넌트의 기본 상태는 컴포넌트의 생성자를 이용해 지정할 수 있다.

*this.setState*

```javascript
setState(
  function(prevState,props) -> nextState,
  callback
) -> void
```

this.state 속성의 값은 직접 덮어쓸 수 없기에 this.setState 메서드를 호출한다. 상태의 갱신을 수행하는 함수를 매개변수로 전달 받으며 리턴 값은 없다.

this.setState 메서드는 최신의 상태로 병합될 객체를 리턴하는 갱신 함수를 매개변수로 전달 받는다. 효율성을 극대화하기 위해 리액트가 상태를 일괄적으로 변경한다. 즉, 상태를 갱신하기 위해 setState 메서드를 호출하면 그 결과가 곧바로 적용되지는 않는다.

클릭이나 키 입력 등 브라우저가 지원하는 이벤트들에 의해 갱신이 이루어진다. 리액트의 이벤트 핸들러는 (addEventListener 함수를 사용하는 방법과 달리) 리액트 요소나 컴포넌트 자체에 설정된다. 이렇게 설정된 이벤트가 전달하는 데이터를 이용해 컴포넌트의 상태를 갱신할 수도 있다.

리액트에서는 데이터가 위에서 아래로(top-down) 흐른다. 즉, 부모 컴포넌트에서 발생한 입력이 자식 요소들로 전달된다. 부모 컴포넌트에 메서드를 정의하고 이 메서드를 자식 컴포넌트에 속성으로 전달해 주는 것이다.

```javascript
// 기본 선언 생략

// CommentBox 컴포넌트에 사용할 모의 데이터 정의
const data = {
  post: {
    id: 123,
    content:
      "What we hope ever to do with ease, we must first learn to do with diligence. — Samuel Johnson",
    user: "Mark Thomas"
  },
  comments: [
    {
      id: 0, 
      user: "David",
      content: "such. win."
    },
    {
      id: 1,
      user: "Haley",
      content: "Love it."
    },
    {
      id: 2,
      user: "Peter",
      content: "Who was Samuel Johnson?"
    },
    {
      id: 3,
      user: "Mitchell",
      content: "@Peter get off Letters and do your homework"
    },
    {
      id: 4,
      user: "Peter",
      content: "@mitchell ok :P"
    }
  ]
};

// Post, Comment 컴포넌트 선언 생략

class CreateComment extends Component {
  constructor(props) {
    super(props);
    this.state = {
      content: "",
      user: ""
    };
    // 클래스로 생성한 컴포넌트는 메서드를 자동으로 바인딩을 하지 않기 때문에
    // 생성자 내에서 직접 바인딩함.
    this.handleUserChange = this.handleUserChange.bind(this);
    this.handleTextChange = this.handleTextChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  // 작성자 필드의 값이 변경된 경우를 처리하기 위한 이벤트 핸들러를 대입
  // input 요소에 입력된 값은 event.target.value 속성을 통해 가져와 this.setState 메서드에 전달해서 컴포넌트 상태를 갱신
  handleUserChange(event) {
    const val = event.target.value;
    this.setState(() => ({
      user: val
    }));
  }
  handleTextChange(event) {
    const val = event.target.value;
    this.setState({
      content: val
    });
  }
  // 폼 제출 이벤트를 처리하기 위한 이벤트 핸들러
  handleSubmit(event) {
    event.preventDefault();
    // 부모가 속성으로 전달한 onCommentSubmit 함수를 호출 할 때 폼에서 읽어온 데이터를 전달한 후,
    // 사용자가 폼 제출 동작이 올바르게 수행되었음을 알 수 있도록 폼을 초기화 한다.
    this.props.onCommentSubmit({
      user: this.state.user.trim(),
      content: this.state.content.trim()
    });
	// 폼을 제출할 때 입력 필드를 초기화
    this.setState(() => ({
      user: "",
      content: ""
    }));
  }
  render() {
    return React.createElement(
      "form",
      {
        className: "createComment",
        // onSubmit 이벤트에 설정한 메서드를 바인딩하는 것을 잊으면 안된다.
        // 바인딩을 해 주지 않으면 이벤트와 메서드가 올바르게 연결되지 않는다.
        onSubmit: this.handleSubmit
      },
      React.createElement("input", {
        type: "text",
        placeholder: "Your name",
        value: this.state.user,
        onChange: this.handleUserChange
      }),
      React.createElement("input", {
        type: "text",
        placeholder: "Thoughts?",
        value: this.state.content,
        onChange: this.handleTextChange
      }),
      React.createElement("input", {
        type: "submit",
        value: "Post"
      })
    );
  }
}
CreateComment.propTypes = {
  onCommentSubmit: PropTypes.func.isRequired,
  content: PropTypes.string
};

class CommentBox extends Component {
  constructor(props) {
    super(props);
    this.state = {
      // comments 데이터를 CommentBox 컴포넌트의 최상위 수준 데이터로 전달한다.
      comments: this.props.comments
    };
    this.handleCommentSubmit = this.handleCommentSubmit.bind(this);
  }
  handleCommentSubmit(comment) {
    // 상태는 절대 직접 갱신하지 않는다. 대신 복사본을 생성한다.
    const comments = this.state.comments;
    comment.id = Date.now();
    const newComments = comments.concat([comment]);
    this.setState({
      comments: newComments
    });
  }
  render() {
    return React.createElement(
      "div",
      {
        className: "commentBox"
      },
      React.createElement(Post, {
        // 앞과 마찬가지로 Post 데이터에 접근하기 위한 데이터 변수들을 최상위 수준 데이터로 전달한다.
        id: this.props.post.id,
        content: this.props.post.content,
        user: this.props.post.user
      }),
      // map 메서드를 이용해 this.state.comments 배열에 저장된 각 댓글에 대응하는
      // 리액트 요소를 생성해 리턴한다.
      this.state.comments.map(function(comment) {
        return React.createElement(Comment, {
          key: comment.id,
          id: comment.id,
          content: comment.content,
          user: comment.user
        });
      }),
      React.createElement(CreateComment, {
        // CreateComment 컴포넌트에 부모 컴포넌트의 handleCommentSubmit 메서드를 전달한다.
        onCommentSubmit: this.handleCommentSubmit
      })
    );
  }
}

CommentBox.propTypes = {
  post: PropTypes.object,
  comments: PropTypes.arrayOf(PropTypes.object)
};

// CommentBox 컴포넌트에 모의 데이터를 속성으로 전달한다.
render(
  React.createElement(CommentBox, {
    comments: data.comments,
    post: data.post
  }),
  node
);
```

리액트 요소의 새로운 배열을 리턴하려면 .map() 함수를 이용하면 된다. 반면 .forEach() 함수는 사용할 수 없는데 그 이유는 이 메서드가 배열을 리턴하지 않으므로 React.createElement() 메서드가 사용할 객체를 얻을 수 없기 때문이다. 하지만 forEach 함수를 이용해 배열을 만들어 그 배열을 전달할 수 있다.

## 2.4 JSX와의 첫 만남

### 2.4.1 JSX를 이용한 컴포넌트의 생성

JSX는 XML과 유사하며, XML을 오로지 코드 변환 도구로만 사용하는 JS의 확장 기능이다. ECMAScript 명세에는 전혀 적용되어 있지 않다.

### 2.4.2 JSX의 장점, 그리고 HTML과의 차이점

JSX가 리액트 컴포넌트를 다루는 부분에 있어 가져오는 장점은 다음과 같다.

- HTML과의 유사성과 쉬운 문법 : HTML과 유사하기 때문에 컴포넌트의 구조를 익숙한 방법으로 선언할 수 있어 훨씬 쉬우며 가독성도 월등히 좋다.
- 선언적이면서 캡슐화된 사용법 : 관련된 메서드들과 뷰를 함께 코드에 포함하면 특정기능을 그룹화할 수 있다. 컴포넌트를 더욱 쉽게 이해할 수 있으며, 이 컴포넌트가 시스템 내에서 어떻게 동작하는지 완전히 이해할 수 있다.

HTML이나 XML과 같은 문법이나 규칙을 따르지 않는다.

- HTML 태그와 리액트 컴포넌트의 차이 : React.createClass 메서드를 이용해 생성했던 사용자 정의 리액트 컴포넌트는 대문자를 표기하는 것이 규칙이다.
- 특성 표현식(Attribute expressions) : 특성 값으로 JS 표현식을 사용하는 경우, `<Comment a={this.props.b}/>` 처럼 중괄호로 표현한다.
- 불리언 특성 : 특성 값을 `</Planactive/>`, `<Input checked/>`와 같이 생략하면 JSX는 이 값들을 true로 간주한다. false 값을 전달하려면 `attribute={false}`와 같이 특성 표현식을 사용해야 한다.

# Chapter. 3 리액트의 데이터와 데이터 흐름

## 3.1 상태

### 3.1.1 상태란 무엇일까?

- 상태 : 특정 시점에 프로그램이 사용하고 있는 정보

상태는 어느 한 시점에 추가 대입이나 연산 없이 참조할 수 있는 모든 값을 포함하고 있다. 다시 말해 어느 특정 시점에 프로그램에 대해 알고 있는 것들의 스냅샷(snapshot)이다.

JS는 완료될 때까지 실행(run-to-completion)이라는 개념으로 동작한다. 즉, 프로그램은 위에서 아래로 실행되며, 우리가 예상하는 순서대로 실행된다.

실행 중인 프로그램이 어느 정도 복잡해지면(심지어 간단한 UI도 제법 복잡해지는 경향이 있다) 그 상태를 파악하기가 더 어려워진다. 즉, 시스템의 로직 역시 생각하기 어려워진다는 것이다.

### 3.1.2 가변 상태와 불변 상태

컴포넌트의 상태를 다루는 방법은 크게 두 가지이다.

1. 변경할 수 있는 상태를 다루는 것
   - 컴포넌트 내에서 변경 가능한(가변성, mutability) 데이터인 **상태**
2. 변경할 수 없는 상태를 다루는 것
   - 컴포넌트가 변경할 수 없으며(불변성, immutability), 수신만 가능한 데이터인 **속성**

불변 상태와 가변상태에 대해 더 알아보면 다음과 같다.

- 불변 상태 : 불변이며 영속적인 데이터 구조는 직접 덮어쓸 수 없지만, 시간이 지나면서 변화되는 다양한 버전의 데이터를 지원
  - 영구 데이터 구조 : 시간의 흐름에 따른 변화를 계속 추적할 수 있다. 즉, 데이터가 교체되는 것이 아니라 현재 상태의 복사본이 만들어짐
- 가변 상태 : 가변이며 순간적(ephemeral) 데이터 구조는 시간이 지나도 단 한 가지 버전의 데이터만 지원, 변경될 때 새로운 값으로 덮어써지며, 그외의 추가 버전은 지원하지 않음
  - 순간 데이터 구조 : 데이터의 어느 한순간만을 저장할 수 있고 버전을 갖지 않기에 변경이 발생하면 이전 상태는 모두 사라짐

JS가 본질적으로 완전한 불면 데이터 구조를 제공하지 못하나 리액트는 컴포넌트의 상태를 (setState를 이용해 변경이 가능한) 가변 객체로 다루며, 속성은 읽기 전용으로 다룬다.

불젼 데이터 객체를 포괄적으로 다루고자 하면, Immutable JS 같은 라이브러리를 사용한다.

## 3.2 리액트에서의 상태

### 3.2.1 리액트에서의 가변 상태: 컴포넌트 상태

모든 컴포넌트는 통상적인 개념의 '상태'를 가지고 있으나 모든 컴포넌트가 로컬 컴포넌트 상태(리액트의 상태 API)를 가지고 있지는 않다.

React.Component 클래스를 상속해 생성한 컴포넌트 상태는 this.state를 통해 접근할 수 있다. this는 클래스의 인스턴스를 참조하며, state는 리액트가 추적하는 특별한 속성이다.

통상적으로 setState 메서드는 성능과 복잡도 문제로 인해 가능하면 보조적으로 사용하는 편이다. 리액트는 개발자를 대신해서 뭔가 다른 것을 추적해야 하며, 필요한 데이터는 개발자가 직접 추적하는 편이 좋다. 컴포넌트의 상태를 필요한 경우만 최소한 이용할 수 있도록 도와주는 리덕스(Redux), 몹스(Mobx), 플럭스(Flux) 등과 같은 다양한 패턴들을 이용할 수 있다.

만일 this.state를 직접 갱신한 후에 setState 메서드를 호출하면 직접 변경한 내용이 다시 수정될 수 있으며, 개발자가 직접 갱신한 상태를 리액트가 제대로 처리하지 못한다.

상태를 불변 객체로 취급해야하는 중요한 이유는 setState 메서드가 this.state 객체를 곧바로 갱신하는 것이 아니라 상태 전환을 미결처리(pending)하기 때문이다. 그래서 setState 메서드를 호출한 후에 this.state에 접근하면 잠재적으로 기존의 값이 리턴될 가능성이 있다.

*setState*

```javascript
setState(
  updater,
  (callback)
) -> void

updater(
  prevState,
  props
) -> stateChange

```

setState 메서드는 컴포넌트이 새로운 상태를 설정하기 위한 updater 함수와 선택적인 callback 함수를 매개변수로 정의하고 있다. 

버전 16 이전에는 첫 번째 인수로 함수 대신 객체를 전달해야 했지만 16 버전부터는 setState 메서드를 호출하면 리액트는 상태의 변경을 예약하는 반면, 메서드 자체는 동기식(synchronous)으로 동작하는 것처럼 보인다. 즉, 필요할 때 시스템(리액트)이 갱신 작업의 수행을 예약할 뿐, 실제 갱신이 이루어지는 시점은 보장되지 않는다.

현재 상태나 속성에 읳존하는 상태를 갱신해야 하는 경우에는 prevState와 props 인수를 통해 기존의 상태를 알아낼 수 있다. Boolean 값을 토글할 때 갱신을 수행하기 앞서 정확한 기존의 상태를 알아야 하는 경우에 상당히 유용하다.

이 메서드는 updater 함수가 리턴한 객체를 얕은 복사(shallow copy)기법을 이용해 최상위 속성만을 현재의 상태에 병합한다. 또한 어떤 이유로든 이 과정의 완료 시점을 알아야 한다면 선택 매개변수인 callback 함수를 지정하면 된다.

### 3.2.2 리액트의 불변 상태: Props
리액트에서 불변 데이터를 전달하기 위한 가장 기본적인 방법은 속성(props)을 이용하는 것이다. 모든 컴포넌트가 속성을 수신할 수 있으며, 이 속성을 constructor, render 메서드 및 생명주기 메서드에서 활용할 수 있다.

리액트의 props API는 그 자체로 반-불변적(semi-immutable)이다. JS에 내장된 Object.freeze 메서드를 이용해서 특정 객체에 새로운 속성을 추가하거나 이미 존재하는 속서을 제거하는 작업을 수행하지 못하도록 한다. 또한, 객체에 이미 존재하는 속성(객체의 열거성(enumerability), 구성 용이성(configurability), 쓰기 가능성(writability) 등)의 변경과 프로토타입의 변경 역시 허용하지 않는다. 이 특징은 props 객체의 가변성을 제거하기엔 충분하지만 기술적으로 완전한 불변 객체를 구현하지 못한다.

컴포넌트의 상태는 개별 컴포넌트가 따로 관리하는 반면, 속성은 보통 부모 컴포넌트가 전달한다. 대부분 JSX의 특성 문법을 이용해 전달하지만, React.createElement 메서드를 사용한다면 이 메서드를 통해 자식 컴포넌트에 직접 속성을 전달할 수도 있다. 

일단 속성을 컴포넌트에 전달하면, 그 컴포넌트 내에서 속성값을 절대로 변경해서는 안된다. 속성의 변경을 시도하면 Uncaught TypeError가 발생한다. 이 규칙은 단방향 데이터 흐름의 일부이며 이는 갱신된 데이터는 부모 컴포넌트로부터 자식 컴포넌트로만 전달된다는 것을 의미한다.

### 3.2.3 속성 다루기: PropTypes와 기본 속성
PropTypes API는 컴포넌트가 어떤 종류의 속성을 필요로 하는지를 명시하는 타입 확인 기능을 제공한다. 컴포넌트에서 PropTypes API를 사용하려면 클래스에 PropTypes라는 정적 속성을 추가해야 한다.

컴포넌트의 클래스에 추가한 정적 속성의 이름은 소문자로 시작하는 반면, prop-types 라이브러리가 제공하는 객체의 이름은 대문자로 시작(PropTypes)한다는 점을 알 수 있다.

컴포넌트가 필요로 하는 속성을 정의하려면 확인할 속성의 이름을 추가하고 그 속성에 prop-types 라이브러리가 기본적으로 제공하는 속성들을 대입해 주면 된다.

defaultProps라는 정적 속성을 추가하면 컴포넌트의 속성에 대한 기본값을 정의할 수 있다. 기본 속성을 이용하면 속성을 제공하지 않아도 정상 작동한다.

### 3.2.4 상태가 없는 함수형 컴포넌트
오로지 속성만을 사용하는, 상태가 없는 함수형 컴포넌트(stateless functional component)를 지원한다.

이 컴포넌트는 명명된 함수(named functions) 또는 변수에 대입한 익명 함수 표현식(anonymous function expression)을 이용해 생성한다. 속성만을 이용해 입력된 값에 따라 같은 값을 출력하기 때문에 기본적으로 순수(pure) 함수라고 할 수 있다.

생명주기 메서드도 없고, 컴포넌트 상태도 없으므로 더 적은 메모리를 소비하고 불필요한 생명주기 검사를 하지 않아 성능이 좋다.

지원 인스턴스를 가지고 있는 부모 컴포넌트와 조합하여 사용할 때 특히 그 진가를 발휘한다. 상태를 가진 하나의 부모 컴포넌트를 만들고 나머지 자식 컴포넌트들은 최대한 가볍게 구현할 수 있다. 이런 패턴은 리덕스를 이용해 작성할 수 있는데 컴포넌트는 최소한으로 구현하고 단 한 곳(store, 상태 저장소)에서 상태를 집중적으로 관리한다.

## 3.3 컴포넌트 간의 통신
컴포넌트가 자식 컴포넌트를 소유할 수도 있고 한 컴포넌트가 어느 특정한 역할을 수행할 수도 있다. 

통상적으로 생명주기가 긴 객체에 상태를 저장하고 이 상태를 애플리케이션의 여러 부분이 서로 공유하는 방식을 사용한다. 반면에 리액트는 다른 컴포넌트와 통신하기 위해서는 속성을 전달해야 하며, 속성을 전달할 때는 다음의 두 가지 사항을 염두해 두어야 한다.

- (상태나 속성) 데이터에 대한 접근은 부모 컴포넌트에서 이루어진다.
- 필요한 데이터는 자식 컴포넌트에 전달한다.

## 3.4 단방향 데이터 흐름
데이터 바인딩은 애플리케이션 UI와 다른 데이터 사이의 연결을 수립하는 과정이다. 실제로 이 과정은 라이브러리나 프레임워크가 모델(예를 들면 사용자) 같은 앱 데이터를 사용자 인터페이스에 연결하고 계속해서 동기화하는 과정이다. 둘이 동기화 하기 때문에 서로 결합(bind)하는 것이다. 이러한 과정을 프로젝션(projection)이라 할 수 있다. 데이터 바인딩은 데이터의 흐름, 즉 데이터가 애플리케이션의 각기 다른 영역으로 전달되는 방법으로 생각하면 된다. 

리액트에서는 데이터의 흐름이 단방향이기 때문에 컴포넌트에 데이터를 전달할 수는 있지만, 속성을 전달하지 않고 다른 컴포넌트의 상태나 속성을 갱신할 수 없다. 또한, 부모 컴포넌트의 데이터를 수정할 수도 없다.

하지만 콜백을 이용해 계층 구조에서 부모에 해당하는 컴포넌트로 데이터를 돌려보낼 수는 있다. 콜백을 이용해도 데이터를 아래쪽으로 보내는 것은 변하지 않으며 그것을 보낼지는 부모 컴포넌트가 결정한다.

지원 인스턴스를 가진 컴포넌트는 자신의 상태를 수정할 수 있지만, 자신의 자식 컴포넌트의 속성을 지정하는 것 이외에 다른 컴포넌트는 수정할 수 없다.

컴포넌트가 계층 구조를 가진다는 점과 더불어 속성과 상태가 컴포넌트 내에서 관리되므로 대부분의 경우 애플리케이션 내에서 데이터가 어떻게 이동하는지를 예측하기가 매우 수월하다.

# Chapter 4. 리액트의 렌더링과 생명주기 메서드
먼저 렌더링 과정은 리액트가 데이터를 사용자 인터페이스에 반영하는 과정이며, 생명주기 메서드를 이용해 컴포넌트와 상호작용하는 방법이다.

## 4.2 렌더링 과정과 생명주기 메서드
### 4.2.1 생명주기 메서드의 소개
어떤 경우에는 이벤트 없이도 자동으로 작업을 수행해야하는데 그 지점이 생명주기 메서드이다. 생명주기 메서드는 클래스 기반 리액트 컴포넌트에 추가된 특별한 메서드로 컴포넌트의 생명주기 내의 특정 시점에 실행된다. 생명주기를 가진 컴포넌트는 컴포넌트가 동작을 시작하는 시점, 동작 중인 시점, 그리고 완료되는 시점인 수명을 표현하게 된다.

컴포넌트의 생명주기에서 가장 중요한 것은 마운팅(mounting), 갱신(updating), 언마운팅(unmounting)이다. 

렌더링은 리액트가 사용자 인터페이스를 만들고 관리하는 과정에서 수행하는 작업으로 애플리케이션을 화면에 그려내는 작업이다. 생명주기 메서드를 이용하면 이 과정을 가로챌 수 있다.

### 4.2.2 생명주기 메서드의 종류
생명주기 메서드는 크게 두 가지가 있다.

- Will 메서드: 어떤 작업이 실행되기 직전에 호출된다.
- Did 메서드: 어떤 작업이 실행된 직후에 호출된다.

이외의 메서드는 주로 초기화나 에러 처리를 위한 것이나 갱신 작업을 위한 것이다.

컴포넌트의 생명주기는 크게 4부분으로 분류할 수 있으며, 각각의 생명주기에 해당하는 메서드는 다음과 같다.

- 초기화: 컴포넌트 클래스의 인스턴스가 생성되는 시점
- 마운팅: 컴포넌트가 DOM에 삽입되는 시점
  - componentWillMount(), componentDidMount()
- 갱신: 컴포넌트가 상태나 속성으로 전달된 새 데이터에 의해 갱신되는 시점
  - componentWillReceiveProps(nextProps), shouldComponentUpdate(nextProps, nextState), componentWillUpdate(nextProps, nextState), componentDidUpdate(prevProps,prevState)
- 언마운팅: 컴포넌트가 DOM에서 제거되는 시점
  - componentWillUnmount()

- 수집되지 않은 에러들
  - componentDidCatch(error, errorInfo)

### 4.2.3 초기 데이터
컴포넌트의 초기 데이터를 제공하기 위한 것들은 다음 두 속성이다.

- defaultProps: 컴포넌트의 기본 속성값을 제공하기 위한 정적인 속성이다. 부모 컴포넌트가 속성을 제공하지 않은 경우 this.props에 기본적으로 설정되며, 컴포넌트가 마운트 되기 전이어서 this.props나 this.state를 사용할 수 없을 때 호출한다. 정적 속성이므로 인스턴스가 아닌 클래스에서 접근한다.
- state(최초): 생성자 내에서 컴포넌트의 초기 상태를 설정하는 데 사용한다. defaultProps와 유사하지만, 데이터가 변경될 가능서이 있으며, React.Component로부터 상속된 컴포넌트에서만 사용할 수 있다.

최초 상태와 속성의 설정은 constructor 메서드에서 설정하며 이 또한 컴포넌트의 생명주기에 속한다.

### 4.2.4 컴포넌트의 마운팅
마운팅은 리액트가 컴포넌트를 실제 DOM에 삽입하는 과정이다. 

마운팅 메서드를 이용하면 컴포넌트의 수명이 시작되는 시점과 끝나는 시점을 '가로챌' 수 있으며, 오직 한 번만 호출된다. 마운팅이 완료되면 비로소 컴포넌트가 동작할 '준비'가 되며, 이 시점에서 HTTP 호출이나 쿠키를 읽는 작업 등을 수행할 수 있다. 또한, 이 시점부터는 'ref'라 부르는 참조를 이용해 DOM 요소에도 접근할 수 있다.

- componentWillMount

  > 컴포넌트가 마운트 되기 전에 상태를 결정하거나 다른 동작을 수행할 기회를 제공한다. 이 메서드 내에서 상태를 변경한다고 해도 렌더링을 다시 수행하지 않지만, 다른 메서드에서 상태를 갱신하면 렌더링 과정이 다시 실행된다.

- componentDidMount

  > 컴포넌트 참조(ref)에 접근할 수 있다. 이 메서드에서는 컴포넌트의 상태와 속성에 접근할 수 있음은 물론 컴포넌트 갱신도 가능하다. 즉, 네트워크 요청의 응답으로 전달받은 데이터를 이용해 컴포넌트 상태를 갱신하는 작업 등을 수행하기에 적절한 시점이며 DOM을 조작하는 jQuery나 다른 서드파티 라이브러리를 호출하기에도 적절한 시점이다.

render 같은 다른 메서드 내에서 핸들러나 함수를 실행하면 리액트의 동작에 대해 예측이 불가능한 결과를 볼 수 있다.

### 4.2.5 갱신 메서드
컴포넌트가 마운트되어 DOM에 위치하게 되면 컴포넌트는 자신의 상태를 갱신할 수 있다. this.setState 메서드를 이용하면 얕은 병합 기법을 이용해 데이터를 컴포넌트의 상태에 반영할 수 있지만, 실제 갱신 과정에서는 이보다 더 많은 일이 일어난다.

- shouldComponentUpdate

  > 특별히 명시하지 않으면 true를 리턴하지만 false를 리턴하면 다음에 다시 상태가 변경될 때까지 render() 메서드를 실행하지 않는다. 즉, 불필요하게 갱신되는 상황을 방지할 수 있다. componentWillUpdate와 componentDidUpdate 메서드는 호출되지 않는다.

- componentWillUpdate
- componentDidUpdate

