# AJAX

요즘은 페이지를 전체를 리로드하지 않고 일부만 바꾸는 방식으로 작동된다. SPA (Single Page Application)이 대표적인 예시이고 여기서 AJAX를 사용한다. 



# Vue.js

React와 Angular의 장점을 가져왔고 셋 중에서 가장 가볍다.

어글리파이는 배포할 때 라이브러리를 가볍게 사용하기 위해 띄어쓰기 등을 제거한 상태로 [뷰티파이](https://beautifier.io/)를 통해 다시 바꿔 놓을 수 있다.

HTML에 js를 어느 위치에 넣느냐에 따라 성능에 영향이 미친다.

http://stevesouders.com/examples/rule-js-bottom.php

JS가 Top에 넣으면 비동기적인 기능 때문에 시간이 많이 걸린다. 반면 Bottom에 넣으면 먼저 내용을 출력하고 이후에 JS를 로드시켜 적용하기 때문에 체감적으로 후자가 빠르다. 만약 중간에다 넣는다면 JS가 전체에 적용되지 않을뿐더러 많은 시간이 걸린다.

명령형(imperative) 특징은 다음과 같다.

- 상세적으로 알려줘야한다.
- 절차적 (스텝 바이 스텝)

선언형(declarative, descriptive)

imperative

1. id : "app" element를 찾는다.
2. 해당 element 내용을 바꾼다.

declarative

1. 하나하나 묘사하지 않고 전체적으로 이야기하되 객체로 이야기한다.
2. 상태(객체)가 가장 중요해진다.

Vue와 같은 frontend-framework가 선언된 객체를 받아 알아서 렌더링 해주기때문에 선언형으로 프로그래밍을 할 수 있다.

Vue에서 권고하는 HTTP 통신 라이브러리는 액시오스(Axios)이다. 이것은 Promise 기반의 HTTP 통신 라이브러리이다.

Vue는 MVVM (Model, View, View Model) 패턴으로 되어 있다.

html 태그에 넣어 사용하는 directive 가 있다.

```html
v-html
v-for
v-if
v-once
```



브라우저 콘솔창에서 localStorage에 접근할 수 있다. localStorage는 반영구적인 DB로 활용할 수 있다. cache로 저장되기 때문에 브라우저 설정으로 삭제하지 않는 한 정보를 계속 유지시킬 수 있다.

sessionStorage는 같은 역할을 하지만 브라우저가 종료하면 (세션이 끝나면) 지워진다.

과거에는 sessionStorage만 존재했기에 창을 끄면 로그인 정보가 다 날아갔는데 localStorage 덕분에 브라우저가 꺼져도 로그인이 유지된다.

```
>localStorage.setItem('students',["ab","bc","cd"])
undefined
>localStorage.getItem('students')
"ab,bc,cd"
>localStorage.getItem('students')[0]
"a"
>localStorage.setItem('people','["ab","bc","cd"]')
undefined
>localStorage.getItem('people')
"["ab","bc","cd"]"
>localStorage.getItem('people')[0]
"["
>let arr = localStorage.getItem('people')
undefined
>arr
"["ab","bc","cd"]"
>JSON.parse(arr)[0]
"ab"

>let person = JSON.stringify({name:'jong',job:'developer',address:'seoul'})
undefined
>person
"{"name":"jong","job":"developer","address":"seoul"}"
>localStorage.setItem("person",person)
undefined
>localStorage.person
"{"name":"jong","job":"developer","address":"seoul"}"
>JSON.parse(person)
{name: "jong", job: "developer", address: "seoul"}
```

localStorage.clear() 를 하면 저장된 정보가 삭제된다.