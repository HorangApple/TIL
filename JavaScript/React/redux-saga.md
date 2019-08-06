# redux-saga

*본 문서는 [redux-saga의 공식 한글 번역 문서](https://mskims.github.io/redux-saga-in-korean/introduction/BeginnerTutorial.html)를 바탕으로 정리한 내용이다.*

## 1. 개요
react & redux를 사용하는 환경에서 비동기 작업을 다룰 때는 미들웨어를 활용하면 손쉽게 상태를 관리할 수 있다. 

*redux-saga 는 리액트/리덕스 애플리케이션의 사이드 이펙트, 예를 들면 데이터 fetching이나 브라우저 캐시에 접근하는 순수하지 않은 비동기 동작들을, 더 쉽고 좋게 만드는 것을 목적으로하는 라이브러리입니다.*

위와 같은 목적으로 react & redux 환경에서 사용하는 미들웨어이다. **redux-thunk**와 비교대상이 되며 이와 다르게 redux-saga는 callback hell에 빠지지 않고 비동기 흐름들을 쉽게 테스트 할 수 있고 액션들을 순수하게 유지한다.

ES6의 **Generator**를 주로 사용한다. Generator에 간략히 설명하자면 `function*`로 선언한 Generator 함수는 내부에서 키워드 `yield`를 사용하여 함수 실행의 흐름을 제어할 수 있다. Generator 함수를 호출하면 Iterator 객체가 반환되는데 이것의 메서드인 `next()`를 사용하면 yield를 선언한 부분까지 실행하고 멈추는 식으로 동작된다. 자세한 것은 [MDN 문서](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/function*)를 참고하자

## 2. 설치
```bash
$ npm install --save redux-saga
```

또는

```bash
$ yarn add redux-saga
```

## 3. 적용
다음과 같은 순서로 기존의 환경(react+redux)에 redux-saga를 적용한다.

1) 액션에 대한 Generator 함수가 선언된 saga 파일을 생성한다.
2) store가 선언된 파일에서 saga 미들웨어를 생성하고 redux 스토어에 mount한다. 그리고 saga를 실행시킨다.

## 4. 개념
effect는 Generator의 yield를 통해 온 순수 자바스크립트 객체를 가리키는 것으로 `put`, `takeEvery`와 같이 redux-saga에서 제공하는 함수를 담고 있는 effect는 미들웨어에 의해 해석되어 작동이 된다.

### 1) 핼퍼함수
- takeEvery: 들어오는 특정 액션마다 태스크를 실행하게 만들어주는 핼퍼 함수
- takeLatest: 이전 태스크들을 모두 취소시키고 단 하나의 태스크만 실행시키는 핼퍼 함수

### 2) 서술적 이펙트