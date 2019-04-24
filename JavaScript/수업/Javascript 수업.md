Seamless : 봉제선이 없다.

# Javascript

- Javascript는 사실 언어가 아니다.

- python 처럼 재단이 있는 것도 아니다.
- JAVA의 인기를 편승하기 위해 이름을 'Java'를 썼다.
- 처음에는 넷스케이프에서 개발되었으나 MS에서 IE에서 사용하기 위해 복사판을 만들었다.
- 실질적인 이름은 ECMAScript 이다.
- ECMAScript 를 준수한 각 브라우저에서 embed되어 있는 스크립트를 Javascript라고 한다.
- 최근에는 Javascript가 하나의 표준이 될 정도로 맞춰졌기에 언어라고 취급하고 있다.

- 브라우저를 조작하기 위한 언어이다.

`document.head.style`처럼 style은 JS의 객체에 불과하다. document는 트리 구조로 브라우저가 html문서를 다루는 형태이다. 이러한 노드들은 JS의 object로 되어있다.

const는 rebind가 안될 뿐 객체로써 property는 갱신이 가능하다. 즉, const가 다른 값을 가리키도록 못만든다.

원시자료형(number, string, boolean,....) : 우리가 정의하지 않은 자료형, immutable

사용자 정의 자료형 (==객체) 

JS는 원시자료형을 빼고 모든 것이 객체다.

|          | var       | let    | const |
| -------- | --------- | ------ | ----- |
| reassign | O         | X      | X     |
| rebind   | O         | O      | X     |
| update   | O         | O      | O     |
| scope    | 함수 단위 | 블록 단위 |블록 단위|

function keyword로 선언한 함수의 this : 실행하는 시점의 객체

Arrow function으로 선언한 함수의 this : 선언하는 시점의 객체

# Node.js

- node 기반에서 JS가 돌아간다.

### Why Lodash?

Lodash makes JavaScript easier by taking the hassle out of working with arrays, numbers, objects, strings, etc.Lodash’s modular methods are great for:

- Iterating arrays, objects, & strings
- Manipulating & testing values
- Creating composite functions

```bash
$ npm i --save lodash
```



# JSON

## 1. 파일포맷 & 단순 문자열(string)

```json
{
    "cofffee": "Americano",
    "iceCream": "Red Velvet"
}
```

## 2. JS 코드가 읽을 수 있는 Object

```javascript
const stringObject = JSON.stringify({'cofffee': 'Americano','iceCream': 'Red Velvet'})
console.log(stringObject)
// string
// {"cofffee":"Americano","iceCream":"Red Velvet"}

JSONData = '{"cofffee": "Americano","iceCream": "Red Velvet"}';
const parsedData = JSON.parse(JSONData);
console.log(parsedData)
// object
// { cofffee: 'Americano', iceCream: 'Red Velvet' }
```



# AJAX (Asynchronous Javascript and XML)

비동기적인 웹 애플리케이션의 제작을 위해 아래와 같은 조합을 이용하는 웹 개발 기법

`XHR(XMLHttpRequest)`는 브라우저마다 bulit-in  되어있는 객체이며 fetch는 ES6 이후에 나온 `ajax `함수이다.

*[XMLHttpRequest](https://developer.mozilla.org/ko/docs/XMLHttpRequest)*

```javascript
// XMLHttpRequest는 브라우저 상에서만 동작한다.
const XHR = new XMLHttpRequest(); // class 인스턴스 생성시 new를 사용
const URL = "https://koreanjson.com/posts/1";

// 요청을 초기화
XHR.open("GET", URL);
// 요청을 보냄
XHR.send();
// 요청이 끝났을 때 함수 실행
XHR.addEventListener('load', (event) => {
    const rawData=event.target.response; // JSON 형식을 받는다.
}) 
```



```javascript
JSON.parse(객체) // JSON으로 변환
JSON.stringify(객체) // JSON을 보내기 위해 string으로 변환
```

