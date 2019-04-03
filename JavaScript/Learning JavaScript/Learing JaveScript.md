[TOC]

# Chapter 01 첫 번째 애플리케이션

<img src="images/image 001.png">

*index.html*

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="main.css">
    <title>Document</title>
</head>
<body>
    <h1>My first application!</h1>
    <p>Welcome to <i>Learning JavaScript, 3rd Edition</i></p>
    <!--자바스크립트가 적용되는 코드-->
    <!--id 속성은 JS와 CSS에서 요소를 쉽게 찾기 위한 것, 페이지 하나에 하나씩 사용-->
    <canvas id="mainCanvas"></canvas>
    
    <!--jQuery 로드, 가장 먼저 로드해야함-->
    <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
    <!--그림 그리는 것을 도와줄 Paper.js 로드-->
    <!--라이브러리 링크하는 순서가 중요함-->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/paper.js/0.9.25/paper-full.min.js"></script>
    <!--자바스크립트 로드-->
    <script src="main.js"></script>
</body>
</html>
```

html 주석은 `<!--`,`-->`이 사용된다.



*main.css*

```css
/* style */
#mainCanvas{
    width: 400px;
    height: 400px;
    border:solid 1px black;
}
```

css 주석은 `/*`,`*/`이 사용된다.



*main.js*

```javascript
// jQuery가 JS 코드를 실행하기 전에 브라우저가 html을 전부 불러왔는지 확인
$(document).ready(function() {
    // JS 인터프리터에서 코드를 더 엄격하게 처리하라는 뜻
    'use strict';
    //Paper.js를 전역 스코프에 설치
    paper.install(window);
    // canvas와 연결
    paper.setup(document.getElementById('mainCanvas'))

    var c = Shape.Circle(200, 200, 80);
    c.fillColor = 'black';
    var text = new PointText(200, 200);
    text.justification = 'center';
    text.fillColor = 'white';
    text.fontSize = 20;
    text.content = 'hello world';
    
    var tool = new Tool();
    // 비동기적 이벤트 처리, 이벤트 핸들러
    tool.onMouseDown = function(event){
        // var c = Shape.Circle(event.point, 20);로 사용할 수 있음
        var c = Shape.Circle(event.point.x, event.point.y, 20);
        c.fillColor='green';
    };   
	
    //
    paper.view.draw();
    // 프로그램을 진단할 때 사용하는 텍스트 전용도구인 콘솔
    console.log('main.js loaded')
});

```

JS의 주석은 인라인 주석인 `//`와 블럭 주석인 `/*`,`*/`이 사용된다.

사용자 입력은 항상 비동기적 이벤트로 취급되어야한다. **비동기적 이벤트**란 이벤트가 언제 일어날지 알 수 없는 이벤트를 가리킨다. 

여기서 `onMouseDown` 이벤트 핸들러는 마우스를 클릭할 때 코드를 실행하고 클릭한 위치를 보고하는 역할을 한다.

JS는 넘겨받은 매개변수를 바탕으로 추론하는 능력이 있어서 `event.point`와 같이 묶어서 넘겨도 알아서 값이 넣어진다.

# Chapter 02 자바스크립트 개발 도구

JS가 ES5에서 ES6로 넘어가는 과정은 점진적이다. 즉, 지금 사용하는 브라우저가 ES6의 기능을 일부 지원하지만 전체를 지원하지 못할 수도 있다. 그렇기 때문에 걱정없이 ES6를 사용하려면 몇 년은 기다릴 수도 있다.

JS 개발 도구는 아래의 것들을 사용한다.

```
1) Git : 버전 관리
2) Node.js : 브라우저 밖에서 JS를 실행할 수 있게 하는 도구, 같이 설치되는 npm은 다른 도구를 설치할 때 필요함
3) Gulp : 반복적인 개발 작업을 자동화하는 빌드 도구
4) Babel : ES6 코드를 ES5 코드로 변환하는 트랜스컴파일러
5) ESLint : 자주 하는 실수를 알려주는 프로그램
```

## 1) Node.js의 npm

npm은 패키지를 설치할 때 globally, 또는 locally로 설치할 수 있다. 전역 패키지는 터미널에서 실행하는 도구들이고 로컬 패키지는 각 프로젝트에 종속되는 패키지이다. `npm install`을 이용하여 설치한다. 특정 버전을 설치할 때는 `패키지 이름@*.*.*`형식으로 사용한다. 

```bash
$ npm init
$ npm install --save-dev gulp gulp-babel @babel/core @babel/preset-env
```

package.json

```json
{
  "name": "first",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "underscore": "^1.9.1"
  },
  "devDependencies": {
    "@babel/core": "^7.3.4",
    "@babel/preset-env": "^7.3.4",
    "eslint": "^5.15.2",
    "gulp": "^4.0.0",
    "gulp-babel": "^8.0.0",
    "gulp-eslint": "^5.0.0"
  }
}
```

`init`을 통해 package.json을 만든다. 생성시 묻는 name은 package 집합에 대한 이름을 묻는 것이며 임의로 작성하면 된다. 

프로젝트에 설치하고 사용하는 모듈을 **의존성**이라고 부른다. 패키지를 설치할 때 `--save-dev`로 설치하면 `devDependencies`에 기록되며 최종 사용자에게 필요 없지만, 개발 과정에서 도움이 되는 **개발 의존성**에 속하게 된다. 반대로 `--save`만 작성할 경우 `dependencies`로 기록되며 최종 사용자에게도 필요한 **일반 의존성**에 속하게 된다. 만일 아무것도 안 적고 install하게 되면 package.json에 기록되지 않는다.

## 2) Gulp

반복 작업을 자동화하는 빌드 도구이며 `$ npm install -g gulp`를 입력하여 전역 설치한다. 그리고 프로젝트마다 로컬 걸프가 필요하므로 `$ npm install --save-dev gulp` 명령을 실행해 개발 의존성에 속하도록 한다. 이후 `gulpfile.js`를 만든다.

*gulpfile.js*

```javascript
const gulp = require('gulp');
// 걸프 의존성 작업을 여기 작성

gulp.task('default',function() {
    // 걸프 작업을 여기 작성
});
```

`$ gulp` 명령어로 성공적으로 설치됐는지 확인할 수 있다. 

## 3) 트랜스컴파일러 (Babel+Gulp)

바벨은 ES5를 ES6로 바꾸는 트랜스컴파일러로 시작했고, 프로젝트가 성장하면서 ES6와 React, ES7 등 여러 가지를 지원하는 범용 트랜스컴파일러가 됐다. 

<img src="images/image 002.png">

위와 같이 디렉터리 `es6`, `dist`, `public/es6`, `public/dist`를 만든다.

`$ npm install --save-dev gulp-babel @babel/core @babel/preset-env` 를 입력하여 바벨과 걸프를 같이 이용하도록 만든다. 이후 `.babelrc`를 만들어 다음과 같이 입력한다.

*.babelrc*

```
// babel6는 "es2015"로 작성
{"presets":["@babel/preset-env"]}
```

그리고  `gulpfile.js`를 다음과 같이 수정한다.

*gulpfile.js*

```javascript
const gulp = require('gulp');
// 걸프 의존성 작업을 여기 작성
const babel = require('gulp-babel');
const eslint = require('gulp-eslint');

gulp.task('default',function() {
    // 걸프 작업을 여기 작성
    // 노드 소스
    gulp.src("es6/**/*.js")
        .pipe(babel()) // 변형
        .pipe(gulp.dest("dist")); // 변형한 코드 저장위치
    // 브라우저 소스
    gulp.src("public/es6/**/*.js")
        .pipe(babel())
        .pipe(gulp.dest("public/dist"));
});
```

걸프는 파이프라인 개념으로 작업을 처리한다.  

*es6/test.js*, *public/es6/test.js*

```javascript
'use strict';
// es6 기능: 블록 스코프 변수 선언
const sentence = [
    {subject: 'JavaScript', verb: 'is', object: 'great'},
    {subject: 'Elephants', verb: 'are', object: 'large'}
];
// es6 기능: 객체 분해
function say({ subject, verb, object}){
    // es6 기능: 템플릿 문자열
    console.log(`${subject} ${verb} ${object}`);
}
// es6 기능: for ..of
for(let s of sentence){
    say(s);
}
```

`$ gulp` 명령어를 통해 트랜스컴파일을 시키면 다음과 같이 변환된다.

*dist/test.js*, *public/dist/test.js*

```javascript
'use strict'; // es6 기능: 블록 스코프 변수 선언

var sentence = [{
  subject: 'JavaScript',
  verb: 'is',
  object: 'great'
}, {
  subject: 'Elephants',
  verb: 'are',
  object: 'large'
}]; // es6 기능: 객체 분해

function say(_ref) {
  var subject = _ref.subject,
      verb = _ref.verb,
      object = _ref.object;
  // es6 기능: 템플릿 문자열
  console.log("".concat(subject, " ").concat(verb, " ").concat(object));
} // es6 기능: for ..of


for (var _i = 0; _i < sentence.length; _i++) {
  var s = sentence[_i];
  say(s);
}
```

`$ node es6/test.js`, `$ node dist/test.js` 를 각각 실행해보면 다음과 같은 결과가 출력된다.

```bash
JavaScript is great
Elephants are large

```

과거에 `$ gulp`와  `$ node dist/test.js` 대신에 `$ babel-node es6/test.js`를 사용할 수 있었는데 `babel-node` 자체가 필요없이 무겁고 메모리를 많이 사용해서 더 이상 사용하지 않는다고 한다.

## 4) Lint

린트는 코드를 세심히 검토해서 자주 일어나는 실수를 알려준다. 여기서는 ESLint를 사용한다.

`$ npm install -g eslint`를 실행하여 설치한다. 이후 프로젝트에 쓸 설정 파일인 `.eslintrc.yml`을 만들기 위해 `$ eslint --init` 명령을 내리고 몇 가지 질문에 답한다.

그다음에 `$ npm install --save-dev gulp-eslint` 명령을 내리고 `gulpfile.js`에 eslint를 추가시킨다.

*gulpfile.js*

```javascript
const gulp = require('gulp');
// 걸프 의존성 작업을 여기 작성
const babel = require('gulp-babel');
const eslint = require('gulp-eslint');

gulp.task('default',function() {
    // 걸프 작업을 여기 작성
    // ESLint를 실행
    gulp.src(["es6/**/*.js", "public/es6/**/*.js"])
        .pipe(eslint())
        .pipe(eslint.format())
    // 노드 소스
    gulp.src("es6/**/*.js")
        .pipe(babel())
        .pipe(gulp.dest("dist"));
    // 브라우저 소스
    gulp.src("public/es6/**/*.js")
        .pipe(babel())
        .pipe(gulp.dest("public/dist"));
});
```



# Chapter 03 리터럴과 변수, 상수, 데이터 타입

## 1) 변수, 상수 선언

```javascript
let currentTempC = 22;
let targetTempC; // let targetTempC=undefined;와 동일
let targetTempC, room1 = "conference_room_a", room2 = "lobby"; // 변수 3개 선언
const ROOM_TEMP_C = 21.5, MAX_TEMP_C = 30; // 상수 2개 선언
```

## 2) 식별자

변수와 상수, 함수 이름을 식별자(idntifier)라 부르며 다음과 같은 규칙을 따른다.

```
1. 식별자는 반드시 글자나 달러 기호($), 밑줄(_)로 시작한다.
2. 식별자에는 글자와 숫자, 달러 기호, 밑줄만 쓸 수 있다.
3. 유니코드 문자도 쓸 수 있다.
4. for, let 등과 같은 예약어는 식별자로 쓸 수 없다.
```

식별자를 만들 때는 다음과 같은 방침을 따른다.

```
1. 식별자는 대문자로 시작해서는 안되며 클래스에만 적용된다.
2. 밑줄 한 개 또는 두 개로 시작하는 식별자는 아주 특별한 상황, 또는 '내부' 변수에서만 사용한다.
3. jQuery를 사용할 경우, 달러 기호로 시작하는 식별자는 보통 jQuery 객체를 의미한다.
```

## 3) 리터럴

**리터럴(literal)**은 직접 값을 만들어 식별자에 사용한다. 즉, 값을 만드는 방법이라 할 수 있다. **숫자형 리터럴**과 **문자열 리터럴**이 있다.

## 4) 원시 타입과 객체

JS 값은 **원시 값(primitive)** 또는 **객체(object)**이다. 

원시 값

- 불변(immutable)
- 숫자, 문자열, 불리언, null, undefined, 심볼

객체

- 여러 가지 형태와 값을 가질 수 있음
- Array, Date, RegExp, Map과 WeakMap, Set과 WeakSet
- Number, String, Boolean (원시 타입의 숫자, 문자열, 불리언에 대응)

## 5) 숫자

IEEE-764 (double-precision) 부동소숫점 숫자 형식을 사용하며 **더블** 형식으로 칭한다. 

한 가지 형식으로 10진수, 2진수, 8진수, 16진수의 네 가지 숫자형 리터럴과 10진수의 소수, 정수, 무한대, 지수표기법, '숫자가 아님'을 나타내는 값까지 인식할 수 있다.

```javascript
let count = 10; // 숫자 리터럴
const blue = 0x000ff; // 16진수
const umask = 0o0022; // 8진수
const roomTemp = 21.5; // 10진수, 소수
const c = 3.0e6; // 지수
const e = -1.6e-19; // 지수
const inf = Infinity; // 양의 무한대
const ninf = -Infinity; // 음의 무한대
const nan = NaN; // 숫자가 아님
```

숫자에 대응하는 Number 객체는 다음과 같은 유용한 프로퍼티가 있다.

```javascript
const small = Number.EPSILON;

const bigInt = Number.MAX_SAFE_INTEGER;
const max = Number.MAX_VALUE;
const minInt = Number.MIN_SAFE_INTEGER;
const min = Number.MIN_VALUE;
const inf = Number.POSITIVE_INFINITY;
const nInf = Number.NEGATIVE_INFINITY;
const nan = Number.NaN;
```

## 6) 문자열

JS 문자열은 **유니코드(Unicode)** 텍스트이다. 유니코드는 텍스트 데이터에 관한 표준이며 사람이 사용하는 언어 대부분의 글자와 심볼에 해당하는 code point를 포함하고 있다. 유니코드 자체는 모든 언어의 텍스트를 나타낼 수 있지만, 유니코드를 사용하는 SW가 모든 코드 포인트를 정확히 렌더링한다고 보장하지 않는다.

문자열 리터럴에는 작은따옴표(''), 큰따옴표(""), 백틱(``)을 사용하는데 백틱은 ES6에서 새로 추가되었다.

### 6-1 이스케이프

```
\n : 줄바꿈 문자(Newline)
\r : 캐리지 리턴(Carriage return)
\t : 탭(Tab)
\' : 작은따옴표
\" : 큰따옴표
\` : 백틱(Backtick), ES6에서 추가
\$ : 달러 기호, ES6에서 추가
\\ : 역슬래시
\uXXXX : 임의의 유니코드 코드 포인트
\xXX : 라틴-1 문자, 유니코드 \u00XX와 동일
\0 : NUL 문자
\v : 세로 탭(Vertical tab)
\b : 백스페이스
\f : 폼 피드(Form feed)
```

### 6-2 템플릿 문자열

문자열 병합(concatenation)을 통해 변수나 상수를 문자열 안에 쓸 수 있다. 또한 문자열 템플릿(interpolation)을 사용하여 나타낼 수 있다. 이때 큰따옴표나 작은따옴표를 사용하지 않고 백틱을 사용한다.

```javascript
let currentTemp = 19.5;
const message = "The current temperature is " + currentTemp + "\u00b0C"; // concatenation
const message = `The current temperature is ${currentTemp}\u00b0C`; // interpolation
```

### 6-3 여러 줄 문자열

JS 콘솔에서는 적용되지 않으며 파일을 만들어야 구현할 수 있다. 그리고 되도록이면 가독성과 오류 예방을 위해 사용하지 않는 것이 좋다.

```javascript
const multiline = "line1\
line2"; 
// line1line2로 출력

const multiline = `line1
	line2`;
/*
line1
	line2
로 출력
*/
```

여러 행에 나눠 쓰고 싶다면 문자열 병합을 사용하자.

### 6-4 숫자와 문자열

JS는 필요하다면 숫자가 들어 있는 문자열을 자동으로 숫자로 바꾼다. 혼란스러울 수 있으므로 되도록 숫자가 필요할 땐 숫자를, 문자열이 필요할 땐 문자열을 사용하는 것이 좋다.

```javascript
const result = 3 + '30'; // 3이 문자열로 바뀌어 결과는 문자열 '330'
const result = 3 * '30'; // '30'이 숫자로 바뀌어 결과는 숫자 90
```

데이터 타입을 바꾸는 방법을 사용하는 것이 좋다.

## 7) 불리언

모든 값을 참 같은 값(truthy), 거짓 같은 값(falsy)로 나눌 수 있다.

```javascript
let heating = true;
let cooling = false;
```

## 8) 심볼

심볼(symbol)은 유일한 토큰을 나타내기 위해 ES6에서 도입한 새 데이터 타입이다. 심볼은 항상 유일하다는 것이 특징이며 이런 점에서 유일함을 가진 객체와 유사하다. 유일하다는 점을 제외하면 심볼은 원시 값의 특징을 모두 가지고 있으므로 확장성 있는 코드를 만들 수 있다.

```javascript
const RED = Symbol("The color of a sunset!");
const ORANGE = Symbol("The color of a sunset!");
RED === ORANGE // false : 심볼은 모두 서로 다르다.
```

다른 식별자와 혼동해서는 안 되는 고유한 식별자가 필요하면 심볼을 사용한다.

## 9) null과 undefined

null이 가질 수 있는 값은 null 하나뿐이며, undefined가 가질 수 있는 값도 undefined 하나뿐이다. 모두 존재하지 않는 것을 나타내지만 일반적으로 null은 프로그래머에게 허용된 타입이고 undefined는 JS 자체에서 사용한다고 생각한다.

변수의 값을 아직 모르거나 적용할 수 없는 경우에는 대부분 null을 사용한다. 할당되지 않은 변수는 자동으로 undefined가 할당되므로 직접 undefined를 할당할 필요가 없다.

```javascript
let currentTemp; // 암시적으로 undefined
const targetTemp = null; // 아직 모르는 값
currentTemp = 19.5; // 값이 존재
currentTemp = undefined; //초기화되지 않은 듯함, 권장하지 않는 방법
```

## 10) 객체

원시 타입은 단 하나의 값만 나타낼 수 있고 불변이지만, 객체는 여러 가지 값이나 복잡한 값을 나타낼 수 있으며, 변할 수도 있다. 객체의 본질은 **컨테이너**이며 컨테이너의 내용물은 시간이 지나면서 바뀔 수도 있지만, 내용물이 바뀐다고 컨테이너가 바뀌는 건 아니다. 

객체에는 중괄호`{,}`를 사용하는 리터럴 문법을 사용한다.

```javascript
const obj = {};
obj.color = "yellow";
obj["not an identifier"] = 3;
obj["not an identifier"]; // 3
obj.color; // "yellow"

// 객체를 프로퍼티로 품을 수 있다.
const sam = {
    name:'Sam',
    classification:{
        kingdom:'Anamalia',
        class: 'Mamalia',
    }
}

// 모두 같은 결과로 'Anamalia'
sam.classification.kingdom;
sam.classification["kingdom"];
sam.["classification"].kingdom;
sam.["classification"]["kingdom"];

// 함수도 담을 수 있다.
sam.speak = function() {return "Meow!";};
sam.speak(); // "Meow!"

// 삭제시 delete 연산자를 사용한다.
delete sam.classification;
delete sam.speak;
```

객체의 콘텐츠는 **프로퍼티(property)** 또는 **멤버(member)**라고 부른다. 프로퍼티는 이름(키)과 값으로 구성된다. 프로퍼티 이름은 반드시 문자열 또는 심볼이어야 하며, 값은 어떤 타입이든 상관없고 다른 객체여도 상관없다. 

객체는 멤버 접근 연산자인 `.`과 계산된 멤버 접근 연산자인 `[]`를 사용할 수 있다. 

## 11) Number, String, Boolean 객체

원시 타입과 다르게 이 세 가지의 객체 타입은 `Number.INFINITY` 같은 특별한 값을 저장하거나 함수 형태로써 기능을 제공하기 위해 존재한다.

```javascript
const s = "hello";
s.toUpperCase(); // "HELLO"
s.rating = 3;
s.rating; // undefined
```

JS는 toUpperCase와 같은 함수를 부르기 위해 임시객체를 만든다. 이후 함수를 호출하는 즉시 임시 객체를 파괴한다. 이 임시 객체에는 값을 할당해도 파괴되기 때문에 undefined로 취급된다.

## 12) 배열

일반적인 객체와 달리 항상 순서가 있고, 키는 순차적인 숫자이다. JS의 배열은 C언어의 와 동적 배열, linked list를 혼합했다고 볼 수 있다. python과 특징이 비슷한데 특징은 다음과 같다.

```
1) 배열 크기는 고정되지 않아 언제든 요소를 추가하거나 제거할 수 있다.
2) 요소의 데이터 타입을 가리지 않는다.
3) 배열요소는 0으로 시작한다.
```

배열에 숫자가 아닌 키나 분수, 음수 등으로 키로 쓸 수 있으나 설계 목적에 어긋날 뿐 아니라 어려운 버그를 초래할 수 있다.

```javascript
const a1 = [1,2,3,4];
const a2 = [1,'two'];
const a3 = [
    [1,2],
    [1,3],
];
const a4 = [
    { name: "Ruby", hardness: 9 },
    { name: "Diamond", hardness: 10},
]
a3.length; // 3
a3.[0]; // [1,2]
a3.[a3.length-1]; // [1,3]
```

## 13) 객체와 배열의 마지막의 쉼표

```javascript
const arr = [
    "One",
    "Two",
]
const o = {
    one: 1,
    two: 2,
}
```

trailing comma, dangling comma, terminal comma 라고 한다. 과거 익스플로러 초기 버전은 마지막 쉼표를 쓰면 에러를 냈었다. 객체 마지막에 프로퍼티를 추가하는 일이 많으므로 항상 마지막에 쉼표를 사용하는 것이 좋다.

참고로 JS 객체 표기법인 JSON에서는 마지막 쉼표를 허용하지 않는다.

## 14) 날짜

JS에 내장된 Date 객체에서 담당하지만 사용하기가 어려운 편이다. 특히 타임존이 다른 날짜를 다룰 때는 매우 어렵다. Date 객체는 원래 Java에서 가져온 것이다.

```javascript
const now = new Date(); // 현재 날짜와 시간을 나타내는 객체
const halloween = new Date(2016, 9, 31); // 특정 날짜에 해당하는 객체
const halloweenParty = new Date(2016, 9, 31, 19, 0); // 특정 날짜와 시간에 해당하는 객체
halloweenParty.getFullYear(); // 2016
halloweenParty.getMonth(); // 9
halloweenParty.getDate(); // 31
halloweenParty.getDay(); // 1 (월요일. 0은 일요일)
halloweenParty.getHours(); // 19
halloweenParty.getMinutes(); // 0
halloweenParty.getSeconds(); // 0
halloweenParty.getMilliseconds(); // 0
```

## 15) 정규표현식

regular expression (regex 또는 regexp)라고도 하며 JS의 부속 언어에 가깝다. 정규표현식은 여러 가지 프로그래밍 언어에서 일종의 확장으로 제공하며, 문자열에서 필요한 검색과 교체 작업을 비교적 단순하게 만든다. JS의 정규표현식은 RegExp 객체를 사용한다. 슬래시 한 쌍 `/.../` 사이에 심볼을 넣는 리터럴 문법도 있다.

## 16) 맵과 셋

ES6에서 새로운 데이터 타입 Map과 Set, 그리고 그들의 '약한' 짝인 WeakMap과 WeakSet을 도입했다.

맵은 객체와 마찬가지로 키와 값을 연결하지만, 특정 상황에서 객체보다 유리한 부분이 있다. 셋은 배열과 비슷하지만 중복이 허용되지 않는다. 위크맵과 위크셋은 맵과 셋과 마찬가지로 동작하나 특정 상황에서 성능이 더 높아지도록 일부 기능을 제거한 버전이다.

## 17) 데이터 타입 변환

### 17-1 숫자로 바꾸기

- Number 객체 생성자 사용
  - 숫자로 바꿀 수 없는 문자열에서는 NaN이 반환
  - 객체 생성자지만 생성된 결과는 객체의 인스턴스가 아니다.
- 내장함수 parseInt나 parse 함수 사용
  - 모두 숫자로 판단할 수 있는 부분까지만 변환하고 그 뒤에 있는 문자열은 무시함
  - parseInt에는 기수(radix)를 넘길 수 있어서 해당 숫자의 기수(기본 값 10진수)를 입력함
- Date 객체를 숫자로 바꿀 때 valueOf() 메서드 사용
  - UTC 1970년 1월 1일 자정으로부터 몇 밀리초가 지났는지 나타내는 숫자를 반환
- 불리언 값은 조건연산자를 활용하여 숫자로 변환

### 17-2 문자열 변환

- 모든 객체에 있는 toString() 메서드 사용
  - 문자열 병합에서 자동으로 숫자를 문자열로 변환하므로, 숫자를 문자열로 바꿀일이 많이 없음
  - 배열에서는 각 요소를 문자열로 바꾼 다음 쉼표로 연결한 문자열을 반환함

### 17-3 불리언으로 변환

- 부정 연산자 `!` 사용
  - '참 같은 값은' false로 변하고 한 번 더 사용하면 true로 변함
- Boolean 생성자 사용



# Chapter 04 제어문

## 1) 기본

```javascript
// while 문
let funds = 50;
while(fund >1 && funds < 100){
    funds = funds + 2;
    funds = funds - 1;
}

while(fund >1 && funds < 100)
    funds = funds + 2; // 이것만 반복
funds = funds - 1; // 반복 끝나고 실행, 들여쓰기와 무관

// for 문
let hand = [];
let winnings = 0;
for(let die = 0; die <hand.length; die++){
    let face = hand[die];
    if(bets[face]>0) winnings = winnings + bets[face];
}

// if 문
if(new Date().getDay() === 3){
    totalBet = 1;
} else if(funds === 7) {
    totalBet = funds;
} else {
    console.log("No superstition here!");
}
```

반복문에서 블록`{,}`을 사용하지 않으면 코드 한 줄만 반복문으로 실행된다. 명확하게는 블록을 사용하는 것이 좋다.

## 2) 메타 문법

메타 문법(metasyntax)은 다른 문법을 설명하는 문법이다. 이를 이용해 JS 제어문의 문법을 간결할게 표기할 수 있다.

대괄호(`[]`)로 감싼 것은 옵션이고, 생략 부호(`...`)는 '여기 들어갈 내용이 더 있다'는 뜻이다. 각 제어문의 메타 문법은 다음과 같다.

```javascript
// while 문
while(condition)
    statement

// if..else 문
if(condition)
    statement1
[else
	statement2]

// do..while 문
do
    statement
while(condition);

// for문
for([initialization];[condition];[final-expression])
    statement
    
// for문을 while문으로 변경
[initialization]
while([condition]){
    statement
    [final-expression]
}

// 객체의 프로퍼티에 루프 실행
for(variable in object)
    statement

// iterable 객체(배열, 컬렉션 등)에 모두 사용
for(variable of object)
    statement

// switch문
switch(expression){
    case value1:
        [action]// expression을 평가한 결과가 value1일 때 실행
    	[break;] // 협업할 시 break;를 의도적으로 없앤다면 따로 주석을 다는 것이 좋음
    case value2: [action] [break;] // JS는 공백을 신경쓰지 않으므로 한 줄로 표현할 수 있음
    ...
    case valueN:
        [action]// expression을 평가한 결과가 valueN일 때 실행
    	[break;]
    default:
        [action]// expression을 평가한 결과가 맞는 것이 없을 때 실행
        [break;]
}
```

## 3) 유용한 제어문 패턴

### 3-1 continue 문을 사용하여 조건 중첩 줄이기

```javascript
while(funds > 1 && funds < 100){
    let totalBet = rand(1, funds);
    if(totalBet === 13){
        console.log("Unlucky! Skip this round....");
        continue;
    }
    // 플레이...
}
```

if문 다음에 else문을 붙여 플레이를 실행할 수 있겠으나 continue를 사용하여 else문을 사용하지 않게 만들 수 있다.

중첩을 제거하면 코드를 읽고 이해하기 쉬워진다.

### 3-2 break나 return 문을 써서 불필요한 연산 줄이기

```javascript
let firstPrime = null;
for(let n of bigArrayOfNumbers){
    // 소수를 찾게 되면 나머지 연산을 하지 않고 빠져나온다.
    if(isPrime(n)){
        firstPrime = n;
        break;
    }
}
```

### 3-3 루프를 완료한 뒤 인덱스 값 사용하기

```javascript
let i = 0;
for(; i < bigArrayOfNumbers.length; i++){
    if(isPrime(bigArrayOfNumbers[i])) break;
}
if(i === bigArrayOfNumbers.length) console.log('No prime numbers!');
else console.log('First prime number found at position ${i}');
```

루프를 일찍 종료했을 때의 인덱스 변수 값이 필요할 때 사용한다. for 루프가 끝나도 인덱스 변수의 값은 그대로 유지되는 것을 활용하였다.

### 3-4 배열을 수정할 때 감소하는 인덱스 사용하기

```javascript
for(let i = 0; i < bigArrayOfNumbers.length; i--){
	if(isPrime(bigArrayOfNumbers[i])) bigArrayOfNumbers.splice(i,1);    
}
```

위와 같이 배열에 루프를 실행하면서 루프 바디에서 배열을 수정하는 것은 위험할 수 있다. 

```javascript
for(let i=bigArrayOfNumbers.length-1; i >= 0 ; i--){
	if(isPrime(bigArrayOfNumbers[i])) bigArrayOfNumbers.splice(i,1);    
}
```

이런 경우 감소하는 인덱스를 써서, 배열 마지막 요소에서 루프를 시작하는 방법을 사용한다. 이렇게 하면 배열에 요소를 추가하거나 제거해도 종료 조건이 바뀌는 일은 없다.



# Chapter 05 표현식과 연산자

- 표현식(expression) 

  - 값으로 평가될 수 있는 문, 즉 결과가 값인 문

  - 결과를 반환할 필요가 있음

  - 다른 표현식에 결함해서 다른 값을 얻을 수 있음

  - 표현식의 값을 변수, 상수, 프로퍼티에 할당할 수 있음

  - 연산자 표현식, 식별자 표현식(변수와 상수 이름), 리터럴 표현식이 있음

    ```javascript
    let x,y; // statement
    y = x = 3 * 5; // 원래 문
    y = x = 15; // 곱셈 표현식을 평가
    y = 15; // 첫 번째 할당을 평가, x=15, y=undefined
    15; // 두 번째 할당을 평가, 전체 문의 결과는 15, 이후에 사용되거나 할당되지 않았으니 버려짐
    ```

- 표현식이 아닌 문(statement) : 일종의 지시, 결과를 반환할 필요가 없음

## 1) 연산자

- 표현식이 값이 되는 것이면 연산자는 값을 만드는 행동
- 피연산자를 매개변수(argument)라고 부르는 경우도 많이 있음

## 2) 산술 연산자

- +, -, /, *, %, -(단항 부정), +(단항 플러스), ++(전위 증가, 후위 증가), --(전위 감소, 후위 감소)

- +(단항 플러스)는 대상이 숫자가 아니면 숫자로 변환하려는 시도를 함

  ```javascript
  const s = "5";
  const y = 3 + +s; // y는 8, 단항 플러스를 사용하지 않았다면 문자열 병합이 일어나 "35"가 된다.
  ```

- 증가 연산자, 감소 연산자가 표현식 깊숙이 묻혀 있다면, 연산자의 부작용을 파악하기 어렵게 될 수 있다.

  ```javascript
  let x = 2;
  const r1 = x++ + x++;
  // ((x++) + (x++))
  // ( 2 + (x++))
  // ( 2 + 3 )
  // 5
  const r2 = ++x + ++x;
  // ((++x) + (++x))
  // ( 5 + (++x))
  // ( 5 + 6 )
  // 11
  const r3 = x++ + ++x;
  // ((x++) + (++x))
  // ( 6 + (++x))
  // ( 6 + 8 )
  // 14
  ```

## 3) 연산자 우선순위

표현식 순서가 잘 기억이 나지 않으면, 순서대로 괄호를 쓰면 된다.

JS에는 56개의 연산자가 있고, 우선순위를 기준으로 19개의 그룹으로 묶을 수 있다.

우선순위가 같은 연산자들은 오른쪽에서 왼쪽으로 또는 왼쪽에서 오른쪽으로 평가한다.

## 4) 비교 연산자

- 일치함(strict equality, ===) : 같은 타입이고 값도 같다면(원시 타입) 두 값은 일치함 (반대의 경우 : !==)
- 동등함(loose equality, ==) : 두 값이 같은 객체를 가리키거나 같은 값을 갖도록 변환할 수 있다면 두 값은 동등함
  - ex. "33"==33
  - 동등 연산자로 인해 대개 null과 undefined, 빈 문자열, 숫자 0 때문에 오류가 생기기 때문에 기계적으로 동등 연산자를 쓰는 습관은 빨리 버리는 것이 좋다.
  - 문자열은 미리 숫자로 변환해서 일치하는지 비교하는 것이 좋다.

```javascript
const n = 5;
const s = "5";
n === s; // false
n !== s; // true
n === Number(s); // true
n !== Number(s); //false
n == s; // ture, 비권장
n != s; // false, 비권장

// 객체 a와 b에 같은 정보가 들어 있더라도 둘은 서로 다른 객체이며, 일치하지도 않고 동등하지도 않다.
const a = { name: "an object" };
const b = { name: "an object" };
a === b; // false, 객체는 항상 다름
a !== b; // true
a == b;  // false, 비권장
a != b; // true, 비권장
```

- 관계 연산자 `>, <, >=, <=` 를 사용한다.

## 5) 숫자 비교

NaN은 그 자신을 포함하여 무엇과도 같지 않다. 즉, `NaN === NaN`, `NaN == NaN` 모두 false이다.

내장 함수 `isNaN`을 사용하면 NaN일 때 true, 그렇지 않으면 false를 반환한다.

부동소숫점 연산 때문에 실수를 비교할 시 오차로 인해 제대로 작동되지 않는다. 매우 작은 값인 2.22e-16과 같은 `Number.EPSILON`를 이용해 아래와 같이 비교한다.

```javascript
let n = 0;
while(true){
    n += 0.1;
    if(Math.abs(n - 0.3) < Number.EPSILON) break;
}
console.log(`Stopped at ${n}`);
```

## 6) 문자열 병합

`+` 연산자는 덧셈과 문자열 병합에 모두 사용된다. 두 경우 모두 왼쪽에서 오른쪽으로 평가한다. 피연산자 중 하나라도 문자열이면 문자열 병합을 수행한다.

```javascript
3 + 5 + "8" // 문자열 "88"
"3" + 5 + 8 // 문자열 "358"
```

## 7) 논리 연산자

JS의 논리 연산자는 불리언이 아닌 값도 다룰 수 있고, 불리언이 아닌 값을 반환하기도 한다. 그렇기에 불리언이 아닌 값을 불리언 값으로 바꾸고 논리 연산자를 사용하는 것이 좋다.

불리언 값에 사용하면 결과는 불리언 값만 나온다.

### 7-1 참 같은 값과 거짓 같은 값

- 거짓 같은 값
  - undefined
  - null
  - false
  - 0
  - NaN
  - ' ' (빈 문자열)

- 참 같은 값
  - 거짓 같은 값 이외의 모든 값
  - 모든 객체, `valueOf( )` 메서드를 호출했을 때 false를 반환하는 객체도 참
  - 배열. 빈 배열도 참
  - 공백만 있는 문자열 (" ")
  - 문자열 "false"

빈 배열이 거짓 같은 값으로 평가되길 원한다면 `arr.length`를 사용한다.

## 8) AND, OR, NOT

- AND(&&), OR(||), NOT(!)

- XOR에 해당하는 논리 연산자는 없지만 비트 연산자는 있다.

### 8-1 단축 평가(short-circuit evaluation)

두 번째 피연산자에 **부수 효과(side effect)**가 있다 하더라도 단축 평가를 거치면 그 효과는 일어나지 않는다. 표현식에서 부수 효과는 증가, 감소, 할당, 함수 호출에서 일어날 수 있다.

```javascript
const skipIt = ture;
let x = 0;
const result = skipIt || x++; // 단축 평가 발생, x의 값은 그대로 0

const skipIt = false;
let x = 0;
const result = skipIt || x++; // result의 값은 0, x의 값은 1 
```

### 8-2 피연산자가 불리언이 아닐 때 논리 연산자가 동작하는 방법

| x            | y             | x && y |
| ------------ | ------------- | -------- |
| **거짓 같은 값** | 거짓 같은 값  | x(거짓 같은 값)|
| **거짓 같은 값** | 참 같은 값  | x(거짓 같은 값) |
| 참 같은 값  | **거짓 같은 값** | y(거짓 같은 값) |
| 참 같은 값  |  **참 같은 값**  | y(참 같은 값)  |

| x            | y             | x \|\| y |
| ------------ | ------------- | -------- |
| 거짓 같은 값  | **거짓 같은 값** | y(거짓 같은 값)|
| 거짓 같은 값 | **참 같은 값** | y(참 같은 값) |
| **참 같은 값** | 거짓 같은 값 | x(참 같은 값) |
| **참 같은 값** |  참 같은 값  | x(참 같은 값)  |

이런 동작을 활용한 팁은 다음과 같다.

```javascript
const options = suppliedOptions || { name: "Default" }
```

`suppliedOptions`가 null이나 undefined라면 `{ name: "Default" }`가 초기화 된다.

`NOT`은 불리언이 아닌 값을 반환할 수 없으므로 `!` 연산자는 피연산자의 타입이 무엇이든 항상 불리언을 반환한다.

### 8-3 조건 연산자, 쉼표 연산자

- 조건 연산자

  ```javascript
  const doIt = false;
  const result = doIt ? "Did it!" : "Didn't do it"; // 조건 ? 참일 때 값 : 거짓일 때 값
  ```

- 쉼표 연산자

  ```javascript
  let x = 0, y = 10, z;
  z = (x++, y++); // z = 10 초기화, 괄호를 사용하지 않으면 0이 저장되고 그다음에 y가 1만큼 늘어난다.
  ```

  for 문에서 표현식을 결합할 때 사용하거나 함수에서 빠져나오기 전에 여러 가지 작업을 한데 묶을 때 사용함

## 9) 연산자 그룹

### 9-1 비트 연산자

비트 연산자가 꼭 필요한 경우는 거의 없다.

```javascript
0b1010 & 0b1100 // 0b1000
0b1010 | 0b1100 // 0b1110
0b1010 ^ 0b1100 // 0b0110
~0b1100 // 0b0101
0b1010 << 2 // 0b101000
let n = 22 // 00000000000000000000000000010110
n >> 1 // 00000000000000000000000000001011
n >>> 1 // 00000000000000000000000000001011
n = ~n // 1의 보수: 11111111111111111111111111101001
n++ // 2의 보수: 11111111111111111111111111101010
n >> 1 // 11111111111111111111111111110101, 부호가 따라가는 오른쪽 시프트
n >>> 1 // 01111111111111111111111111110101, 0으로 채우는 오른쪽 시프트
```

하드웨어 조작을 제외하고 비트 연산자를 쓰는 것이 효율적인 경우는 플래그 (불리언 값)를 다룰 때이다.

```javascript
const FLAG_EXECUTE = 1 // 0b001
const FLAG_WRITE = 2 // 0b010
const FLAG_READ = 4 // 0b100

let p = FLAG_READ | FLAG_WRITE; // 0b110
let hasWrite = p & FLAG_WRITE; // 0b010, 참 같은 값
let hasExecute = p & FLAG_EXECUTE; // 0b000, 거짓 같은 값
p = p ^ FLAG_WRITE; // 0b100, 쓰기 플래그 토글 (쓰기 권한 없어짐)
p = p ^ FLAG_WRITE; // 0b110, 쓰기 플래그 토글 (쓰기 권한 생성)

// 표현식 하나로 여러 플래그를 동시에 판단할 수도 있다.
const hasReadOrExecute = p & (FLAG_READ | FLAG_EXECUTE);
const hasReadAndExecute = p & (FLAG_READ | FLAG_EXECUTE) === FLAG_READ | FLAG_EXECUTE;
```

### 9-2 typeof 연산자

typeof 연산자는 피연산자의 타입을 나타내는 문자열을 반환하나 JS의 일곱 가지 데이터 타입(undefined, null, 불리언, 숫자, 문자열, 심볼, 객체)을 정확히 나타내지 못하고 있다.

typeof는 연산자이므로 괄호는 필요 없다.

| 표현식               | 반환식      | 참고              |
| -------------------- | ----------- | ----------------- |
| typeof undefined     | "undefined" |                   |
| typeof null          | "object"    | 애석하지만 사실   |
| typeof {}            | "object"    |                   |
| typeof true          | "boolean"   |                   |
| typeof 1             | "number"    |                   |
| typeof ""            | "string"    |                   |
| typeof Symbol()      | "symbol"    | ES6에서 새로 생김 |
| typeof function() {} | "function"  |                   |

### 9-3 void 연산자

피연산자를 평가 후 undefined를 반환한다. 

쓸모 없지만 매우 가끔 HTML에서 <a> 태그의 URI에 사용한다. 권장되는 방법은 아니지만 아래와 같이 하면 브라우저에서 다른 페이지로 이동하는 일을 막을 수 있다.

```html
<a href="javascript:void 0">Do nothing.</a>
```

### 9-4 할당 연산자

등호의 왼쪽에 있는 것은 반드시 값을 저장할 수 있는 변수나 프로퍼티, 배열 요소 중 하나이어야 한다.

```javascript
let v, v0;
v = v0 = 9.8; // 먼저 v0가 9.8이 되고 그 다음 v가 9.8이 된다.
```

## 10) 해체 할당

ES6에서 새로 도입한 해체 할당(destructuring assignment)은 객체나 배열을 변수로 '해체'할 수 있다.

```javascript
// 객체 선언
const obj = {b:2, c:3, d:4};

// 해체 할당
const {a,b,c} = obj;
console.log(a); // undefined
console.log(b); // 2
console.log(c); // 3
console.log(d); // ReferenceError: d is not defined

// 에러
{a,b,c} = obj;

// 정상적으로 실행
({a,b,c} = obj);

// 확산 연산자(...) 사용
const arr = [1,2,3,4,5];
let [x,y, ...rest] = arr;
x; // 1
y; // 2
rest; // [3, 4, 5], 임의의 변수 rest에 저장

// swap
let a = 5, b = 10;
[a,b] = [b,a];
a; // 10
b; // 5
```

객체를 해체할 때는 반드시 변수 이름과 객체의 프로퍼티 이름이 일치해야 한다. 이터러블 객체에는 모두 사용 가능하다.

객체 해체는 할당만으로 이뤄질 수도 있지만, 그렇게 하려면 반드시 괄호를 써야 한다. 괄호를 쓰지 않으면 JS는 표현식 좌변을 블록으로 해석한다.

해체의 진가는 다른 곳에서 가져온 객체나 배열에서 원하는 요소를 뽑아내야 할 때 드러난다.

## 11) 객체와 배열 연산자

객체와 배열, 함수에 사용하는 연산자이다.

| 연산자     | 설명                          |
| ---------- | ----------------------------- |
| .          | 점 연산자                     |
| [ ]        | 대괄호 연산자                 |
| in         | 프로퍼티 존재 연산자          |
| new        | 객체 인스턴스화 연산자        |
| instanceof | 프로토타입 체인 테스트 연산자 |
| ...        | 확산 연산자                   |
| delete     | 삭제 연산자                   |

## 12) 템플릿 문자열과 표현식

템플릿 문자열은 어떤 표현식이든 그 값을 문자열에 넣을 수 있다.

## 13) 표현식과 흐름 제어 패턴

### 13-1 if...else 문을 3항 연산자로 바꾸기

```javascript
if(isPrime(n)){
    label = 'prime';
} else {
    label = 'non-prime'
}

label = isPrime(n) ? 'prime' : 'non-prime';
```

### 13-2 if 문을 단축 평가하는 OR 표현식으로 바꾸기

```javascript
if(!options) options = {};

options = options || {};
```



# Chapter 6 함수

## 1) 반환 값

함수 바디 안에 return 키워드를 사용하면 함수를 즉시 종료하고 값을 반환함. 그 값이 함수 호출의 값이다.

## 2) 호출과 참조

JS에서 함수도 객체이기에 다른 객체와 마찬가지로 넘기거나 할당할 수 있다.

함수 식별자 뒤에 괄호를 쓰면 JS는 함수를 호출하려 한다고 이해하고, 함수 바디를 실행한다. 그리고 함수를 호출한 표현식은 반환 값이 된다.

괄호를 쓰지 않으면 함수를 참조하는 것이며, 함수는 실행되지 않는다.

```javascript
function getGreeting(){
    return "Hello world!"
}

getGreeting(); // "Hello World!"
getGreeting; // function getGreeting()

// 변수에 할당
const f = getGreeting;
f(); // "Hello world!"

// 프로퍼티에 할당
const o = {};
o.f = getGreeting;
o.f(); // "Hello world!"

// 배열에 할당
const arr = [1,2,3];
arr[1] = getGreeting; // arr은 [1, function getGreeting(), 2]
arr[1](); // "Hello world!"

```

## 3) 함수와 매개변수

함수를 호출하면서 정보를 전달할 때는 함수 매개변수(argument, parameter)를 이용한다. 매개변수는 함수가 호출되기 전에는 존재하지 않는다는 점을 제외하면 일반적인 변수나 마찬가지이다.

```javascript
// a,b는 정해진 매개변수(formal argument)
function abg(a,b){
    return (a+b)/2;
}

avg(5, 10); // 7.5, 매개변수는 값을 받아 실제 매개변수(actual argument)가 됨
```

원시 값을 담은 변수는 수정할 수 있지만(다른 값으로 바꿀 수 있지만) 원시 값 자체는 바뀌지 않는다. 그라나 객체는 바뀔 수 있다.

원시 값을 값 타입(value type), 객체는 참조 타입(reference type)이라 부른다.

### 3-1 매개변수가 함수를 결정하는가?

C언어에서는 f(), f(x), f(x,y) 가 각각 다른 함수로 취급하지만, JS 경우 매개변수 숫자와 관계없이 같은 함수로 취급된다.

정해진 매개변수에 값을 제공하지 않으면 내부의 실제 매개변수 값은 암시적으로 undefined가 된다.

### 3-2 매개변수 해체

```javascript
// 프로퍼티가 있는 객체 해체
function getSentence({ subject, verb, object }){
    return `${subject} ${verb} ${object}`;
}

const o = {
    subject: "I",
    verb: "love",
    object: "JavaScript",
};

getSentence(o); // "I love JavaScript"

// 배열 해체
function getSentence([ subject, verb, object ]){
    return `${subject} ${verb} ${object}`;
}

const arr = ["I","love","JavaScript"]
getSentence(arr); // "I love JavaScript"

// 확산 연산자 활용, 항상 마지막 매개변수에 사용한다.
function addPrefix(prefix, ...words){
    const prefixedWords = [];
    for(let i=0; i<words.length; i++){
        prefixedWords[i] = prefix + words[i];
    }
    return prefixedWords;
}

addPrefix("con", "verse", "vex"); // ["converse", "convex"]
```

ES5에서는 함수 바디 안에서만 존재하는 특별한 변수 arguments를 사용해서 확산과 비슷한 일을 할 수 있다. arguments는 실제 배열이 아니라 배열 비슷한 객체이므로 특별 취급하거나 일반적인 객체로 변환해야 했다. ES6에서는 확산 매개변수를 사용해 이런 약점을 해결했다.

### 3-3 매개변수 기본값

ES6에서 매개변수에 기본값(default value)을 지정하는 기능이 추가 됐다. 일반적으로 매개변수에 값을 제공하지 않으면 undefined가 값으로 할당된다.

```javascript
function f(a, b = "default", c = 3){
    return `${a} - ${b} - ${c}`;
}

f(5, 6, 7); // "5 - 6 - 7"
f(5, 6); // "5 - 6 - 3"
f(5); // "5 - default - 3"
f(); // "undefined - default - 3"
```

## 4) 객체의 '프로퍼티'인 함수

객체의 프로퍼티인 함수를 메서드(method)라고 불러서 일반적인 함수와 구별한다. 객체 리터럴에서도 메서드를 추가할 수 있다.

```javascript
const o = {
    name: 'Wallace', // 원시 값 프로퍼티
    // bark() { return 'Woof!';}, 과 동일, ES6부터 가능
    bark: function() { return 'Woof!';}, // 함수 프로퍼티(메서드)
}
```

## 5) this 키워드

함수 바디 안에는 특별한 읽기 전용 값인 this가 있다. this는 일반적으로 객체지향 프로그래밍 개념에 밀접한 연관이 있다. 

일반적으로 this는 객체의 프로퍼티인 함수에서 의미가 있다. 메서드를 호출하면 this는 호출한 메서드를 소유하는 객체가 된다.

```javascript
const o = {
    name: 'Wallace',
    speak() {return `My name is ${this.name}!`}
}
o.speak(); // "My name is Wallace!", 함수 호출시 this는 o에 묶임, o에서 함수를 호출한 상황
const speak = o.speak;
speak === o.speak; // true
speak(); // "My name is undefined!"
//JS는 이 함수가 어디서 호출하는지 모르니까 name은 undefined된다.
```

중첩된 함수일 경우 의도한 대로 값을 읽기 위해서는 별도로 `const self=this;`처럼 선언해야한다.

```javascript
const o ={
    name:'Julie',
    greetBackWards: function(){
        const self = this; // 이후의 다른 함수 안에서 사용하기위해 o를 가리키는 this를 저장
        function getReverseName(){
            let nameBackwards = '';
            for(let i=self.name.length-1; i>=0; i--){
                nameBackwards += self.name[i];
            }
            return nameBackwards;
        }
        return `${getReverseName()} si eman ym, olleH`;
    },
};
console.log(o.greetBackWards());
```

## 6) 함수 표현식과 익명 함수

함수 표현식(function expression)은 함수를 선언하는 한 가지 방법이며, 함수의 이름을 생략하는 익명 함수(anonymous function)이 될 수도 있다. 또한 식별자에 할당할 수도 있고 즉시 호출할 수도 있다.

```javascript
// 함수 표현식, 이름을 생략한 함수 선언
const f = function(){
    //...
}

// 재귀를 사용하려면 일반적인 함수 선언을 해야한다.
const g = function f(stop){
    if(stop) console.log('f stopped');
    f(true);
};
g(false);
```

함수 선언과 함수 표현식이 완전히 똑같이 보인다면, JS는 컨텍스트를 이용해 구분한다. 즉 ,함수 선언이 표현식으로 사용됐다면 함수 표현식이고 표현식으로 사용되지 않았다면 함수 선언으로 구분한다.

호출할 생각으로 함수를 만든다면 함수 선언을 사용하면 되고, 다른곳에 할당하거나 다른 함수에 넘길 목적으로 함수를 만든다면 함수 표현식을 사용한다.

## 7) 화살표 표기법

화살표 표기법(arrow notation)은 `function`이라는 단어와 중괄호 숫자를 줄이려고 고안된 단축 문법이다.

- function을 생략해도 된다.
- 함수에 매개변수가 단 하나 뿐이라면 괄호도 생략할 수 있다.
- 함수 바디가 표현식 하나라면 중괄호와 return 문도 생략할 수 있다.

```javascript
const f1 = function() {return "hello!";}
// 또는
const f1 = () => "hello!";

const f2 = function(name) {return `Hello, ${name}!`;}
// 또는
const f2 = name => `Hello, ${name}!`;

const f3 = function(a,b){return a+b;}
// 또는
const f3 = (a,b) => a+b;
```

화살표 함수는 익명 함수를 만들어 다른 곳에 전달하려 할 때 가장 유용하다.

```javascript
const o ={
    name:'Julie',
    greetBackWards: function(){
        // const self = this; 사용하지 않아도 된다.
        const getReverseName = () => {
            let nameBackwards = '';
            for(let i=this.name.length-1; i>=0; i--){
                nameBackwards += this.name[i];
            }
            return nameBackwards;
        }
        return `${getReverseName()} si eman ym, olleH`;
    },
};
console.log(o.greetBackWards()); 
```

일반적인 함수와 다른 점은 this가 다른 변수와 마찬가지로, 정적으로(lexically) 묶인다는 것이다. 그렇기 때문에 이전의 예제처럼 별도의 `self`를 만들지 않아도 의도한 대로 this가 가리켜진다.

또 다른 차이점은 화살표 함수는 객체 생성자로 사용할 수 없고, arguments 변수도 사용할 수 없다. 그러나 ES6에서 확산 연산자가 생겼으니 arguments 변수는 필요없다.

## 8) call과 apply, bind

```javascript
const bruce = { name: "Bruce" };
const madeline = { name: "Madeline"};

function greet(){
    return `Hello, I'm ${this.name}!`;
}

greet(); // "Hello, I'm undefined!" - this는 어디에도 묶이지 않았다.
greet.call(bruce); // "Hello, I'm Bruce!" - this는 bruce
greet.call(madeline); // "Hello, I'm Madeline!" - this는 madeline

function update(birthYear, occupation){
    this.birthYear = birthYear;
    this.occupation = occupation;
}

update.call(bruce, 1949, 'singer');
// bruce는 이제 {name: "Bruce", birthYear: 1949, occupation: "singer"}
update.call(madeline, 1942, 'actress');
// madeline은 이제 {name: "Madeline", birthYear: 1942, occupation: "actress"}
```

call 메서드는 모든 함수에서 사용할 수 있으며, this를 특정값으로 지정할 수 있다.

함수를 호출하면서 call을 사용하고 this로 사용할 객체를 넘기면 해당 함수가 주어진 객체의 메서드인 것처럼 사용할 수 있다. 

call의 첫 번째 매개변수는 this로 사용할 값이고, 매개변수가 더 있으면 그 매개변수는 호출하는 함수로 전달된다.

```javascript
function update(birthYear, occupation){
    this.birthYear = birthYear;
    this.occupation = occupation;
}

update.apply(bruce, [1949, 'singer']);
// bruce는 이제 {name: "Bruce", birthYear: 1949, occupation: "singer"}
update.apply(madeline, [1942, 'actress']);
// madeline은 이제 {name: "Madeline", birthYear: 1942, occupation: "actress"}
```

apply는 함수 매개변수를 처리하는 방법을 제외하면 call과 완전히 같다. 

call은 일반적인 함수와 마찬가지로 매개변수를 직접 받지만, apply는 매개변수를 배열로 받는다. 그렇기에 배열 요소를 함수 매개변수로 사용해야 할 때 유용하다.

```javascript
const arr = [2, 3, -5, 15, 7];
Math.min.apply(null, arr); // -5
Math.max.apply(null, arr); // 15

const newBruce = [1940, "martial artist"];
update.call(bruce, ...newBruce); // apply(bruce, newBruce)와 같다.
Math.min(...arr); // -5
Math.max(...arr); // 15
```

Math.min와 Math.max는 this와 관계없이 작동되기에 null이외에 아무값이나 넣어도 돌아간다.

ES6의 확장 연산자(...)를 사용해도 apply와 같은 결과를 얻을 수 있다.

```javascript
const updateBruce = update.bind(bruce);

updateBruce(1904, "actor");
// bruce는 이제 { name: "Bruce", birthYear: 1904, occupation: "actor"}
updateBruce(madeline, 1274, "king"); 
// bruce는 이제 { name: "Bruce", birthYear: 1274, occupation: "king"}
// madeline은 변하지 않는다.

const updateBruce1949 = update.bind(bruce, 1949);
// 태어난 해가 1949로 항상 고정
updateBruce1949("singer, songwriter");
// bruce는 이제 { name: "Bruce", birthYear: 1949, occupation: "singer, songwriter"}
```

bind를 사용하면 함수의 this 값을 영구적으로 바꿀 수 있다. call이나 apply, 다른 bind와 함께 호출하더라도 this 값이 bruce가 되도록 하려면 bind를 사용한다.

bind는 함수의 동작을 영구적으로 바꾸므로 찾기 어려운 버그의 원인이 될 수 있다. 그렇기에 함수의 this가 어디에 묶이는지 정확히 파악하고 사용해야한다.

bind에 매개변수를 넘기면 항상 그 매개변수를 받으면서 호출되는 새 함수를 만드는 효과가 있다.



# Chapter 7 스코프

스코프(scope)는 변수와 상수, 매개변수가 언제 어디서 정의되는지 결정한다. 

```javascript
function f(x) {
    return x+3;
}
f(5); // 8
x; // ReferenceError: x is not defined
```

x는 함수 바디를 버어나면 x는 존재하지 않는 것처럼 보이게 된다. 따라서 x의 스코프가 함수 f라고 말할 수 있다.

변수의 스코프가 어떤 함수라고 말할 때는, 함수를 실제 호출할 때까지는 함수 바디의 정해진 매개변수(formal argument)가 존재하지 않음을 반드시 상기해야한다.

var를 제외한 let이나 const로 선언 하기 전에는 스코프 안에 존재하지 않는다.

## 1) 스코프와 존재

가시성(visibility)이라고도 불리는 **스코프**는 프로그램의 현재 실행 중인 부분, 즉 실행 컨텍스트(execution context)에서 현재 보이고 접근할 수 있는 식별자들을 말한다. 반면 존재한다는 말은 그 식별자가 메모리가 할당된(예약된) 무언가를 가리키고 있다는 뜻이다.

## 2) 정적스코프와 동적 스코프

JS의 스코프는 **정적(어휘적, lexical)**이다. 소스 코드만 봐도 변수가 스코프에 있는지 판단할 수 있지만 즉시 스코프를 분명히 알 수 있다는 뜻은 아니다.

**정적 스코프**는 어떤 변수가 함수 스코프 안에 있는지 함수를 정의할 때 알 수 있다는 뜻이다.

```javascript
const x = 3;

function f() {
    console.log(x);  // 3
    console.log(y);  // 5, y는 정적 스코프에 해당
}

{// 새 스코프
    y=5;
    f();
}
```

변수 x는 함수 f를 정의할 때 존재하지만, y는 그렇지 않다. f를 호출하면 x는 그 바디 안의 스코프에 있지만 y는 그렇지 않다. 함수 f는 자신이 정의될 때 접근할 수 있었던 식별자에는 여전히 접근할 수 있지만, 호출할 때 스코프에 있는 식별자에 접근할 수 없다.

JS의 정적 스코프는 **전역 스코프(global scope)**와 **블록 스코프(block scope)**, **함수 스코프(function scope)**에 적용된다.

## 3) 전역 스코프

**전역 스코프**는 프로그램을 시작할 때 암시적으로 주어지는 스코프를 가리키며 전역 스코프에서 선언한 것은 무엇이든 프로그램의 모든 스코프에서 볼 수 있다.

전역 스코프에서 선언된 것들을 전역 변수라고 하며 전역 스코프를 남용하지 않도록 충분히 생각하고 사용해야한다.

```javascript
let name = "Irena"; // 전역
let age = 25; // 전역

function great(){
    console.log(`Hello, ${name}!`);
}
function getBirthYear(){
    return new Date().getFullYear() - age;
}
```

위의 예제는 함수가 호출하는 **컨텍스트(스코프)**에 대단히 의존적이다. 어떤 함수든 프로그램 어디에서든 상관없이 name 값을 바꿀 수 있다. 그리고 name과 age는 흔한 이름이므로 다른 곳에서 다른 이유로 사용할 가능성이 크다. greet와 getBirthYear는 전역 변수에 의존하므로, 프로그램의 다른 부분에서 name과 age를 정확히 사용한다고 가정하고 있다. 

```javascript
let user = {
    name = "Irena",
    age = 25,
};

function great(user){
    console.log(`Hello, ${user.name}!`);
}
function getBirthYear(user){
    return new Date().getFullYear() - user.age;
}
```

사용자 정보를 단일 객체에 보관하는 방법이 더 낫다. 그리고 명시적으로 user를 전달 받도록 수정한다. 프로그램의 규모가 커지면 모든 스코프를 기억하고 관리하기 힘들기 때문에 전역 스코프에 의존하지 않는 것이 중요하다.

## 4) 블록 스코프

**블록 스코프**는 그 블록의 스코프에서만 보이는 식별자를 의미한다.

```javascript
console.log('before block');
{// 독립 블록
    console.log('inside block');
    const x = 3;
    console.log(x); // 3
}
console.log(`outside block; x=${x}`); // ReferenceError: x는 정의되지 않았습니다.
```

앞의 예제는 독립 블록을 사용했다. 블록은 보통 if나 for 같은 제어문의 일부분으로 쓰이지만, 블록 그 자체로도 유효한 문법이다. 그러나 필요한 경우는 드물다.

## 5) 변수 숨기기

다른 스코프에 있으면서 이름이 같은 변수나 상수는 혼란을 초래할 때가 많다.

```javascript
{
    //외부 블록
    let x = { color:"blue" };
    let y = x;
    let z = 3;
    {
        // 내부 블록
        let x = 5; // 바깥의 x는 가려졌다.
        console.log(x); // 5
        console.log(y.color); // "blue"; y가 가리키는,
        // 외부 스코프의 x가 가리키는 객체는 스코프 안에 있다.
        y.color = "red";
        console.log(z);
    }
    console.log(x.color); // "red"; 객체는 내부 스코프에서 수정됐다.
    console.log(y.color); // "red"; x와 y는 같은 객체를 가리킨다.
    console.log(z); // 3
}
console.log(typeof x); // "undefined"; x는 스코프에 있지 않다.
```

이 예제는 **변수 숨김(variable masking)**을 잘 보여준다. 내부 블록의 x는 외부 블록에서 정의한 x와는 이름만 같을 뿐 다른 변수이므로 외부 스코프의 x를 숨기는(가리는) 효과가 있다.

변수의 이름이 같으므로 외부 스코프에 있는 변수에 접근할 방법이 없다. 변수를 숨기면 그 변수는 해당 이름으로는 절대 접근할 수 없다.

스코프의 계층적인 성격 때문에 어떤 변수가 스코프에 있는지 확인하는 **스코프 체인(scope chain)**이란 개념이 생겼다. 현재 스코프 체인에 있는 모든 변수는 스코프에 있는 것이며, 숨겨지지 않았다면 접근할 수 있다.

## 6) 함수, 클로저, 정적 스코프

모든 함수를 전역에서 정의하고 함수 안에서 전역 스코프를 참조하지 않도록 신경 쓰는 전통적 프로그램에서는 함수가 어떤 스코프에 접근할 수 있는지 생각할 필요가 없다.

하지만 JS에서는 함수가 필요한 곳에서 즉석으로 정의할 때가 많다. 함수가 특정 스코프에 접근할 수 있도록 의도적으로 그 스코프에서 정의하는 경우가 많다. 이런 것을 보통 **클로저(closure)**라고 부른다. 스코프를 함수 주변으로 좁히는(closing) 것이라고 생각해도 된다. 

```javascript
let globalFunc; // 정의되지 않은 전역 함수
{
    let blockVar = 'a'; // 블록 스코프에 있는 변수
    globalFunc = function(){
        console.log(blockVar);
    }
}
globalFunc(); // "a"
```

`globalFunc`는 블록 안에서 값을 할당받았다. 이 블록 스코프와 그 부모인 전역 스코프가 클로저를 형성한다. 

`globalFunc`을 호출하면, 이 함수는 스코프에서 빠져나왔음에도 불구하고 `blockVar`에 접근할 수 있다. 일반적으로 스코프에서 빠져나가면 해당 스코프에서 선언한 변수는 메모리에서 제거해도 안전하다. 하지만 여기서는 스코프 안에서 함수를 정의했고, 해당 함수는 스코프 밖에서도 참조할 수 있으므로 JS는 스코프를 계속 유지한다. 또한 일반적으로는 접근할 수 었는 것에 접근할 수 있는 효과를 얻을 수 있다.

## 7) 즉시 호출하는 함수 표현식

함수 표현식을 사용하면 즉시 호출하는 **함수 표현식(IIFE)**이란 것을 만들 수 있다. 

```javascript
(function() {
    // IIFE 바디
})();
```

IIFE는 함수를 선언하고 즉시 실행한다. IIFE의 장점은 내부에 있는 것들이 모두 자신만의 스코프를 가지지만, IIFE 자체는 함수이므로 그 스코프 밖으로 무언가를 내보낼 수 있다는 것이다.

```javascript
const f = (function() {
    let count = 0;
    return function() {
        return `I have been called ${++count} time(s).`;
    }
})();
console.log(f); // I have been called 1 time(s).
console.log(f()); // I have been called 2 time(s).

// 괄호를 씌우지 않았을 때
const f = function() {
    let count = 0;
    return function() {
        return `I have been called ${++count} time(s).`;
    }
};
console.log(f); // [Function: f]
console.log(f()); // [Function]
console.log(f()()); // I have been called 1 time(s).
console.log(f()()); // I have been called 1 time(s).
```

변수 `count`는 IIFE 안에 안전하게 보관되어 있으므로 손댈 방법이 없다. `f`는 자신이 몇 번 호출됐는지 항상 정확히 알고 있다.

## 8) 함수 스코프와 호이스팅

ES6에서 let을 도입하기 전에는 **var**를 써서 변수를 선언했고, 이렇게 선언된 변수들은 함수스코프라 불리는 스코프를 가졌다. (var로 선언한 전역 변수는 명시적인 함수 안에 있지는 않지만 함수 스코프와 똑같이 동작한다.)

**let**으로 변수를 선언하면, 그 변수는 선언하기 전에는 존재하지 않는다. var로 선언한 변수는 현재 스코프 안이라면 어디서든 사용할 수 있으며, 심지어 선언하기도 전에 사용할 수 있다.

```javascript
// let으로 선언
x; // ReferenceError: x는 정의되지 않았다.
let x = 3; // 에러가 일어나서 실행이 멈췄으므로 여기에는 도달할 수 없다.	
```

```javascript
// var로 선언
x; // undefined, 호이스팅, 할당까지 끌어올려지지 않음.
var x = 3;
x; // 3
```

var로 선언한 변수는 끌어올리다는 뜻의 **호이스팅(hoisting)**이라는 메커니즘을 따른다. JS는 함수나 전역 스코프 전체를 살펴보고 var로 선언한 변수를 맨 위로 끌어올린다. 중요한 것은 선언만 끌어올려진다는 것이며, 할당은 끌어올려지지 않는다.

```javascript
var x = 3;
if(x === 3){
    var x = 2;
    console.log(x); // 2
}
console.log(x); // 2

// ------------

let x = 3;
if(x === 3){
    let x = 2;
    console.log(x); // 2
}
console.log(x); // 3

// ------------

let x = 3;
if(x === 3){
    x = 2;
    console.log(x); // 2
}
console.log(x); // 2
```

같은 함수나 전역 스코프 안에서는 var로 새 변수를 만들 수 없으며, let으로 가능했던 변수 숨김도 불가능함을 알 수 있다. 이 예제는 블록 안에서 두 번째 var 문을 썼지만 변수 x는 하나뿐이다.

var를 쓰면 혼란스럽고 쓸모없는 코드가 생길 수 있기에 위와 같은 스타일은 권장하지 않는다. 기존에 사용한 var를 뜯어고치면 기존 코드가 모두 망가지므로 대신 ES6에서 let을 새로 만들었다.

달리 말해 var에는 let보다 나은 점이 없지만 ES5로 트랜스컴파일을 해야히기에 어떻게 동작하는지 이해하고 있어야한다.

## 9) 함수 호이스팅

```javascript
f(); // 'f'
function f(){
    console.log('f');
}

// ------------

f(); // ReferrenceError: f 는 정의되지 않았다.
let f = function(){
    console.log('f');
}
```

var로 선언된 변수와 마찬가지로, 함수 선언도 스코프 맨 위로 끌어올려진다. 따라서 함수를 선언하기 전에 호출할 수 있다.  그러나 변수에 할당한 함수 표현식은 끌어올려지지 않는다.

## 10) 사각지대

```javascript
if(typeof x === "undefined"){
    console.log("x doesn't exist of is undefined");
} else{
    // x를 사용해도 안전한 코드
} // 여기까지만 작성하면 에러가 발생하지 않는다.

// let x ---> 사용하면 에러가 발생한다.
```

**사각지대(temporal dead zone)**는 let으로 선언하는 변수는 선언하기 전까지 존재하지 않는다는 직관적 개념을 잘 나타내는 표현이다. 스코프 안에서 변수의 사각지대는 변수가 선언되기 전의 코드이다.

typeof 연산자는 변수가 선언됐는지 알아볼 때 널리 쓰이고, 존재를 확인하는 안전한 방법으로 알려져 있어 위와 같이 사용되었지만 ES6의 let의 등장으로 사각지대가 생겨났고 예시에 let을 사용하면 에러가 발생하게 된다.

ES6에서는 변수가 정의되어있는지 확인할 필요가 거의 없으니 typeof가 문제를 일으킬 소지도 거의 없다.

## 11) 스트릭트 모드

**스트릭트 모드(strict mode)**는 ES5의 암시적 전역 변수(implicit global)로 인한 에러를 해결하기 위해 도입되었다.

**암시적 전역 변수**는 var로 변수 선언하는 것을 잊은 채 변수를 사용하면 JS는 전역 변수를 참조하려 한다고 간주하고, 만약 없다면 스스로 만드는 것을 이야기한다.

스트릭트 모드는 암시적 전역 변수를 허용하지 않는다. 코드 맨 앞에 "use strict"를 사용하면 스크립트 전체가 스트릭트 모드로 실행되고, 함수 안에서 "use strict"를 사용하면 해당 함수만 스트릭트 모드로 실행된다.

전역 스코프에 적용을 시키면 스크립트 전체의 동작 방식이 바뀌므로 주의해야한다. 최신 웹사이트는 다양한 스크립트를 불러와서 사용하므로 전역 스코프에서 스트릭트 모드를 사용하면 불러온 스크립트 전체에 스트릭트 모드가 강제된다. 그러므로 전역 스코프에서 스트릭트 모드를 사용하지 않는 것이 좋다.

```javascript
(function(){
    'use strict';
    // 코드를 전부 이 안에 작성한다.
    // 이 코드와 함께 동작하는 다른 스크립트는
    // 스트릭트 모드에 영향받지 않는다.
})();
```

함수마다 일일이 스트릭트 모드를 설정하는 건 귀찮으므로 위와 같이 블록 안에 작성하여 실행한다.

린트 프로그램을 사용한다면 스트릭트 모드가 막아주는 문제를 대부분 막아주지만, 두 번 체크해서 나쁠 건 없다.



# Chapter 8 배열과 배열 처리

## 1) 배열의 기초

- 배열은 객체와 달리 본질에서 순서가 있는 데이터 집합이며 0으로 시작하는 숫자형 인덱스를 사용한다.
- JS의 배열은 비균질적(nonhomogeneous)이며 한 배열의 요소가 모두 같은 타입일 필요가 없다.
- 배열 리터럴과 인덱스 접근 시에 대괄호를 사용한다.
- 모든 배열에는 요소가 몇 개 있는지 나타내는 length 프로퍼티가 있다.
- 배열 길이보다 큰 인덱스를 사용해서 요소를 할당하면 배열은 자동으로 그 인덱스에 맞게 늘어나며 빈 자리는 undefined로 채워진다.
- Array 생성자를 써서 배열을 만들 수도 있지만 그렇게 해야하는 경우는 별로 없다.

## 2) 배열 요소 조작

배열 메서드 중 일부는 배열 **'자체를'** 수정하며, 다른 일부는 새 배열을 반환한다.

### 2-1 배열의 처음이나 끝에서 요소 하나를 추가하거나 제거하기 (수정)

배열 첫 요소는 인덱스가 0인 것, 끝 요소는 `arr.length - 1`인 요소를 가리킨다.

`push`, `pop`은 오른쪽 끝의 요소를 추가하거나 제거하고 `shift`와 `unshift`는 왼쪽 끝의 요소를 추가하거나 제거한다.

```javascript
const arr = ["b","c","d"];
arr.push("e"); // ["b","c","d","e"]
arr.pop(); // ["b","c","d"]
arr.unshift("a"); //["a","b","c","d"]
arr.shift(); // ["b","c","d"]
```

### 2-2 배열의 끝에 여러 요소 추가하기 (반환)

`concat` 메서드는 배열의 끝에 여러 요소를 추가한 사본을 반환한다. concat에 배열을 넘기면 이 메서드는 배열을 분해해서 원래 배열에 추가한 사본을 반환한다.

```javascript
const arr = [1,2,3];
arr.concat(4,5,6); // [1,2,3,4,5,6]
arr.concat([4,5,6]); // [1,2,3,4,5,6]
arr.concat([4,[5,6]]); // [1,2,3,4,[5,6]]
arr.concat([4,5],6); // [1,2,3,4,5,6]
```

concat은 제공받은 배열을 한 번만 분해한다.

### 2-3 배열 일부 가져오기 (반환)

`slice` 메서드는 배열의 일부만 가져올 때 사용한다. `slice` 메서드는 매개변수 두 개를 받는다. 첫 번째 매개변수는 어디서부터 가져올지를, 두 번째 매개변수는 어디까지 가져올지를 지정한다. 두 번째 매개변수를 생략하면 배열의 마지막까지 반환한다. 음수 인덱스를 쓰면 배열의 끝에서부터 요소를 센다.

```javascript
const arr = [1,2,3,4,5];
arr.slice(3); // [4,5]
arr.slice(2,4); // [3,4]
arr.slice(-2); // [4,5]
arr.slice(1,-2); // [2,3]
arr.slice(-2,-1); // [4]
```

### 2-4 임의의 위치에 요소 추가하거나 제거하기 (수정)

`splice`는 배열을 자유롭게 수정할 수 있다. 첫 번째 매개변수는 수정을 시작할 인덱스이고, 두 번째 매개변수는 제거할 요소 숫자이다. 아무 요소도 제거하지 않을 때는 0을 넘긴다. 나머지 매개변수는 배열에 추가될 요소이다. 제거할 요소들이 있다면 제거 후 그것들을 리턴한다.

```javascript
const arr = [1,5,7];
arr.splice(1,0,2,3,4); // []. arr은 [1,2,3,4,5,7]
arr.splice(5,0,6); // []. arr은 [1,2,3,4,5,6,7]
arr.splice(1,2); // [2,3]. arr은 [1,4,5,6,7]
arr.splice(2,1,'a','b'); // [5]. arr은 [1,4,'a','b',6,7]
```

### 2-5 배열 안에서 요소 교체하기 (수정)

`copyWithin`은 ES6에서 도입한 새 메서드이다. 배열 요소들을 복사해서 다른 위치에서 시작해, 기존의 요소를 덮어쓴다. 첫 번째 매개변수는 복사한 요소를 붙여넣을 위치이고, 두 번째 매개변수는 복사를 시작할 위치이고, 세 번째 매개변수는 복사를 끝낼 위치이다(생략 가능). slice와 마찬가지로, 음수 인덱스를 사용하면 배열의 끝에서부터 센다.

```javascript
const arr = [1,2,3,4];
arr.copyWithin(1,2); // [3,4]를 복사, arr은 [1,3,4,4]
arr.copyWithin(2,0,2); // [1,3]을 복사, arr은 [1,3,1,3]
arr.copyWithin(0,-3,-1); // [3,1]을 복사, arr은 [3,1,1,3]
```

### 2-6 특정 값으로 배열 채우기 (수정)

`fill`은 ES6에 도입한 새 메서드이다. 정해진 값으로 배열을 채운다. 크기를 지정해서 배열을 생성하는 Array 생성자와 잘 어울린다. 배열의 일부만 채우려 할 때는 시작 인덱스와 끝 인덱스를 지정하면 된다. 음수 인덱스도 사용할 수 있다.

```javascript
const arr = new Array(5).fill(1); // arr이 [1,1,1,1,1]로 초기화
arr.fill("a"); // arr은 ["a","a","a","a","a"]
arr.fill("b",1); // arr은 ["a","b","b","b","b"]
arr.fill("c",2,4); // arr은 ["a","b","c","c","b"]
arr.fill(5.5,-4); // arr은 ["a",5.5,5.5,5.5,5.5]
arr.fill(0,-3,-1); // arr은 ["a",5.5,0,0,5.5]
```

### 2-7 배열 정렬과 역순 정렬 (수정)

```javascript
const arr = [1,2,3,4,5];
arr.reverse(); // arr은 [5,4,3,2,1], 역순 정렬
arr.sort(); // arr은 [1,2,3,4,5], 오름 차순 정렬
```

`sort`는 정렬 함수를 받을 수 있다. 예를 들어 일반적으로는 객체가 들어있는 배열을 정렬할 수 없지만, 정렬 함수를 사용하면 가능하다.

```javascript
const arr = [{name:"Suzanne"},{name:"Jim"},
{name:"Trevor"},{name:"Amanda"}]
arr.sort(); // arr은 바뀌지 않는다.
// arr의 name 프로퍼티의 알파벳 순으로 정렬
arr.sort((a,b) => a.name>b.name); 
// arr의 name 프로퍼티의 두 번째 글자의 알파벳 역순으로 정렬
arr.sort((a,b) => a.name[1]<b.name[1]); 
```

## 3) 배열 검색

```javascript
const arr = [1,5,"a",o,true,5,[1,2],"9"];
arr.indexOf(5); // 1
arr.lastIndexOf(5); // 5
arr.indexOf("a"); // 2
arr.lastIndexOf("a"); // 2

arr.indexOf("a",5); // -1
arr.indexOf(5,5); // 1
arr.lastIndexOf(5,4); // 1
arr.lastIndexOf(ture,3); // -1
```

`indexOf`, `lastIndexOf`는 배열의 시작 또는 끝에서 부터 검색하여 해당 값의 인덱스를 리턴한다. 만약 찾지 못하면 -1을 반환한다. 두 번째 매개변수로 검색 시작 인덱스를 받는다(생략 가능).

```javascript
const arr = [{id:5,name:"Suzanne"},{id:7,name:"Jim"}]
arr.findIndex(o => o.id === 5); // 0
arr.findIndex(o => o.name === "Jim"); // 1
arr.findIndex(o => o === 3); // -1
arr.findIndex(o => o.id === 17); // -1
```

`findIndex`는 일치하는 것을 찾지 못했을 때 -1을 반환하고 보조 함수를 써서 검색 조건을 지정할 수 있다.

```javascript
const arr = [{id:5,name:"Suzanne"},{id:7,name:"Jim"}]
arr.find(o => o.id === 5); // 객체 {id:5,name:"Suzanne"}
arr.find(o => o.id === 2); // undefined

const arr = [1,17,16,5,4,16,10,3,49]
arr.find((x,i)=>i>2 && Number.isInteger(Math.sqrt(x))); // 4
```

`find`는 조건에 맞는 요소의 인덱스가 아닌 요소 자체를 원할 때 사용한다. `find`는 `findIndex`와 마찬가지로 검색 조건을 함수로 전달할 수 있다. 조건에 맞는 요소가 없을 때는 `undefined`를 반환한다.

`find`와 `findIndex`에 전달하는 함수는 배열의 각 요소를 첫 번째 매개변수로 받고, 현재 요소의 인덱스와 배열 자체도 매개변수로 받는다. 이런 점에서 다양하게 응용할 수 있다.

```javascript
class Person{
    constructor(name){
        this.name = name;
        this.id = Person.nextId++;
    }
}
Person.nextId = 0;
const jamie = new Person("Jamie"),
juliet = new Person("Juliet"),
peter = new Person("Peter"),
jay = new Person("Jay");
const arr = [jamie,juliet,peter,jay];

// 옵션 1: ID를 직접 비교하는 방법
arr.find(p => p.id === juliet.id); // juliet 객체

// 옵션 2: "this" 매개변수를 이용하는 방법
arr.find(function(p){
    return p.id === this.id
}, juliet); // juliet 객체
```

`find`와 `findIndex`에 전달하는 함수의 `this`도 수정할 수 있다. 이를 이용해서 함수가 객체의 메서드인 것처럼 호출할 수 있다. 

```javascript
const arr = [5,7,12,15,17];
arr.some(x => x%2 === 0); // ture; 12는 짝수이다.
arr.some(x => Number.isInteger(Math.sqrt(x))); // false; 제곱수가 없다.

const arr = [4,6,16,36];
arr.every(x => x%2 === 0); // true; 홀수가 없다.
arr.every(x => Number.isInteger(Math.sqrt(x))); // false; 6은 제곱수가 아니다.
```

`some`은 조건에 맞는 요소를 찾으면 즉시 검색을 멈추고 `true`를 반환하며, 조건에 맞는 요소를 찾지 못하면 `false`를 반환한다.

`every`는 배열의 모든 요소가 조건에 맞아야 `true`를 반환하며 그렇지 않다면 `false`를 반환한다. `every`는 조건에 맞지 않는 요소를 찾아야만 검색을 멈추고 `false`를 반환한다. 조건에 맞지않는 요소를 찾지 못하면 배열 전체를 검색한다.

`some`과 `every`도 콜백 함수를 호출할 때 `this`로 사용할 값을 두 번째 매개변수로 받을 수 있다.


## 4) map과 filter (반환)
`map`은 배열 요소를 변형한다. 일정한 형식의 배열을 다른 형식으로 바꿔야 할 때 `map`을 사용한다. 

```javascript
const cart = [ {name:"Widget", price:9.95},{name:"Gadget",price:22.95}];
const names = cart.map(x => x.name); // ["Widget","Gadget"]
const prices = cart.map(x => x.price); // [9.95,22.95]
const discountPrices = prices.map(x => x*0.8) // [7.96,18.36]
```

콜백 함수는 각 요소에서 호출될 때 요소 자체와 요소 인덱스, 배열 전체를 매개변수로 받는다(배열 매개변수는 유유용하지 않다). 

```javascript
const items = ["Widget","Gadget"];
const prices = [9.95,22.95];
const cart = items.map((x,i) => ({name:x,price:prices[i]}));
// cart: [{name:"Widget",price:9.95},{name:"Gadget",price:22.95}]
```

객체를 괄호로 감싼 이유는, 이렇게 하지 않으면 화살표 표기법에서 객체 리터럴의 중괄호를 블록으로 판단하기 때문이다.

```javascript
// 카드 덱을 만든다.
const card = [];
for(let suit of ['H','C','D','S'])
    for(let value=1; value<=13; value++)
        card.push({suit,value});

// value 가 2인 카드
card.filter(c => c.value === 2);

// 다이아몬드
cards.filter(c => c.suit === 'D'); // length: 13
// 킹,퀸,주니어
cards.filter(c => c.value > 10); // length: 12
```

`filter`는 배열에서 필요한 것들만 남길 목적으로 만들어졌다. `filter`는 `map`과 마찬가지로 사본을 반환하며 새 배열에는 필요한 요소만 남는다. 어떤 요소를 남길지 판단할 함수를 넘겨도 된다.

## 5) 배열의 마법 reduce
`map`이 배열의 각 요소를 변형한다면 `reduce`는 배열 자체를 변형한다. `reduce`라는 이름은 이 메서드가 보통 배열을 값 하나로 줄이는 데 쓰이기 때문에 붙여졌다.

`reduce`가 반환하는 값 하나는 객체일 수도 있고, 다른 배열일 수도 있다. `map`과 `filter`를 비롯한 여러 배열 메서드의 동작을 대부분 대신할 수 있다.

```javascript
const arr = [5,7,2,4];
// 누적값이 0부터 시작
const sum = arr.reduce((a,x) => a += x,0); // 18
// 누적값이 undefined부터 시작
const sum = arr.reduce((a,x) => a += x); // 18
```

`reduce` 역시 콜백 함수를 받는다. 첫번째 매개변수는 배열이 줄어드는 대상인 **어큐뮬레이터(accumulator, 누적값)**이다. 두 번째 매개변수부터는 콜백의 순서대로 현재 배열요소, 현재 인덱스, 배열 자체가 입력된다.

누적값이 제공되지 않으면 `reduce`는 첫 번째 배열 요소를 초깃값으로 보고 두 번째 요소에서부터 함수를 호출한다.

```javascript
const words = ["Beachball","Rodeo","Angel",
"Aardvark","Xylophone","November","Chocolate",
"Papaya","Uniform","Joker","Clover","Bali"];

const alphabetical = words.reduce((a,x)=>{
    // 단어의 알파벳 첫 글자를 index로 배열 생성 (없다면)
    if(!a[x[0]]) a[x[0]] = [];
    a[x[0]].push(x);
    return a;
}, {});

console.log(alphabetical)
// { B: [ 'Beachball', 'Bali' ],
//   R: [ 'Rodeo' ],
//   A: [ 'Angel', 'Aardvark' ],
//   X: [ 'Xylophone' ],
//   N: [ 'November' ],
//   C: [ 'Chocolate', 'Clover' ],
//   P: [ 'Papaya' ],
//   U: [ 'Uniform' ],
//   J: [ 'Joker' ] }
```

## 6) 삭제되거나 정의되지 않은 요소들
```javascript
const arr = Array(10).map(function(x) {return 5})
console.log(arr) // arr의 모든 요소는 undefined

const arr = [1,2,3,4,5];
delete arr[2];
arr.map(x => 0); // [0,0,undefined,0,0]
```
`Array` 메서드인 `map`과 `filter`, `reduce`는 삭제되거나 정의되지 않은 요소들에서 콜백 함수를 호출하지 않는다.

배열에 `delete`를 사용할 일은 거의 없으니 이런 문제가 발생할 가능성은 낮다.

## 7) 문자열 병합
```javascript
const arr = [1,null,"hello","world",true,undefined];
delete arr[3];
arr.join(); // "1,,hello,,true,"
arr.join(''); // "1hellotrue"
arr.join(' -- '); // "1 -- -- hello -- -- true --"
```
`Array.prototype.join`은 매개변수로 구분자 하나를 받고 요소들을 하나로 합친 문자열을 반환한다. 이 매개변수가 생략됐을 때의 기본값은 **쉼표**이며, 문자열 요소를 합칠 때 정의되지 않은 요소, 삭제된 요소, `null`, `undefined`는 모두 빈 문자열로 취급한다.


# Chapter 9 객체와 객체지향 프로그래밍
JS 객체 역시 컨테이너지만, 크게 보면 다음 두 가지 측면에서 배열과 다르다. 
- 배열은 값을 가지며 각 값에는 숫자형 인덱스가 있다. 객체는 프로퍼티를 가지며 각 프로퍼티에는 문자열이나 심볼 인덱스가 있다.
- 배열에는 순서가 있다. 즉, arr[0]은 항상 arr[1]보다 앞에 있다. 반면 객체에는 그런 순서가 보장되지 않는다. obj.a가 obj.b보다 앞에 있다고 말할 수 없다.

객체를 정말로 객체답게 만드는 것은 **프로퍼티**이며 프로퍼티는 키(문자열 또는 심볼)과 값으로 구성된다. 객체의 진짜 특징은 키를 통해 프로퍼티에 접근 할 수 있다는 점이다.

## 1) 프로퍼티 나열
일반적으로 어떤 컨테이너의 콘텐츠를 리스트로 나열한다고 하면, 보통 배열을 생각하지 객체를 생각하지 않는다. 하지만 객체도 분명 컨테이너이고 프로퍼티 나열을 지원한다.

프로퍼티 나열에서 기억해야 할 것은 **순서가 보장되지 않는다**는 점이다. 브라우저나 노드 등의 프로그램에서 속도나 효율 향상을 목적으로 언제든 바뀔 수도 있다.

### 1-1 for...in
```javascript
const SYM = Symbol();
const o = {a:1,b:2,c:3,[SYM]:4};
for(let prop in o){
    if (!o.hasOwnProperty(prop)) continue;
    console.log(`${prop}: ${o[prop]}`);
}
// a: 1
// b: 2
// c: 3
```
`hasOwnProperty`는 `for...in`에 나타날 위험을 제거하기 위해 사용한다. 생략해도 아무 차이도 없으나 다른 타입의 객체, 특히 다른 사람이 만든 객체의 프로퍼티를 나열하다 보면 예상치 못한 상황이 생길 수도 있다.

`for...in` 루프에는 키가 심볼인 프로퍼티는 포함되지 않다.

`for...in`을 배열에 사용할 수도 있겠지만, 배열에는 일반적인 `for` 루프나 `forEach`를 사용하는 것이 좋다.

### 1-2 Object.keys
```javascript
const SYM = Symbol();
const o = {a:1,b:2,c:3,[SYM]:4};
Object.keys(o).forEach(prop => console.log(`${prop}: ${o[prop]}`));
// a: 1
// b: 2
// c: 3
```
`Object.keys`는 객체에서 나열 가능한 문자열 프로퍼티를 배열로 반환한다.

객체의 프로퍼티 키를 배열로 가져와야 할 때는 `Object.keys`가 편리하다.

## 2) 객체지향 프로그래밍
OOP의 개념 중 일부는 1950년대부터 있었지만, 시뮬러 67과 스몰토크가 등장하면서 OOP의 형태가 갖춰지기 시작했다.

**객체**는 데이터와 기능을 논리적으로 묶어놓은 것이다. OOP는 우리가 사물을 이해하는 자연스러운 방식을 반영하도록 설계되었다.

**클래스**는 어떤 자동차처럼 추상적이고 범용적인 것이다. **인스턴스**는 특정 자동차처럼 구체적이고 한정적인 것이다. 그것의 기능은 메서드라고 부른다. 클래스에 속하지만 특정 인스턴스에 묶이지 않는 기능을 클래스 메서드라고 부른다. 인스턴스를 처음 만들 때는 **생성자(constructor)**가 실행된다. 생성자는 객체 인스턴스를 초기화한다.

예를 들어 운송 수단을 자동차의 **수퍼 클래스(superclass)**라 부르고, 자동차를 운송 수단의 **서브클래스(subclass)**라 부른다.

### 2-1 클래스와 인스턴스 생성
ES6 이전에 JS에서 클래스를 만드는 건 직관적이도 않고 무척 번거로운 일이었다. ES6에서는 클래스를 만드는 간편한 새 문법을 도입했다.
```javascript
class Car{
    constructor(make,model){
        this.make = make;
        this.model = model;
        this.userGears = ['P','N','R','D'];
        this.userGear = this.userGears[0];
    }
    shift(gear){
        if(this.userGears.indexOf(gear) < 0)
            throw new Error(`Invalid gear: ${gear}`);
        this.userGear = gear;
    }
}

const car1 = new Car("Tesla","Model S"); // Car의 인스턴스 car1
const car2 = new Car("Mazda","3i"); // Car의 인스턴스 car2

car1 instanceof Car // ture, 인스턴스 확인
car1 instanceof Array // False

car1.shift('D');
car2.shift('R');
```
여기서 `this` 키워드는 의도한 목적, 즉 메서드를 호출한 인스턴스를 가리키는 목적으로 쓰였다. 클래스를 만들 때 사용한 `this` 키워드는 나중에 만들 인스턴스의 플레이스홀더이다. 메서드를 호출하는 시점에서 this가 무엇인지 알 수 있게 된다.

```javascript
car1.userGear // "D"
car2.userGear // "R"
```
`Car` 클래스에 `shift` 메서드를 사용하면 잘못된 기어를 선택하는 실수를 방지할 수 있을 것처럼 보인다. 하지만 완벽하게 보호되는 것은 아니다. 직접 `car1.userGear = 'X'`라고 설정한다면 막을 수 없다. 대부분의 객체지향 언어에서는 메서드와 프로퍼티에 어느 수준까지 접근할 수 있는지 대단히 세밀하게 설정할 수 있는 메커니즘을 제공해서 직접 선언하는 것을 막을 수 있다. 하지만 JS에는 그런 메커니즘이 없기에 다른 방법을 사용해야한다.

그러한 약속으로 **외부에서 접근하면 안 되는 프로퍼티 이름 앞에 밑줄을 붙이는 방법**을 사용한다. 이렇게 하여 실수를 빨리 찾을 수 있도록 한다.

```javascript
const Car = (function(){

    const carProps = new WeakMap();

    class Car{
        constructor(make,model){
            this.make = make;
            this.model = model;
            this._userGears = ['P','N','R','D'];
            carProps.set(this,{userGear:this._userGears[0]});
        }
        get userGear() {return carProps.get(this).userGear;}
        set userGear(value){
            if(this._userGears.indexOf(value) < 0)
                throw new Error(`Invalid gear: ${value}`);
            carProps.get(this).userGear = value;
        }
        shift(gear){this.userGear = gear;}
    }
    return Car;
})();
```

프로퍼티를 꼭 보호해야 한다면 위와 같이 스코프를 이용해 보호하는 `WeakMap` 인스턴스를 사용할 수 있다. 

여기서는 즉시 호출하는 함수 표현식을 써서 `WeakMap`을 클로저로 감싸고 바깥에서 접근할 수 없게 했다. 

프로퍼티 이름에 심볼을 쓰는 방법도 있으나 역시 접근 불가능한 것은 아니므로 한계가 있다.

### 2-2 클래스는 함수다
ES6에서 class 키워드를 도입하기 전까지, 클래스를 만든다는 것은 곧 **클래스 생성자로 사용할 함수를 만든다**는 의미였다.

```javascript
// ES5에서의 클래스와 같은 문법 구현
function Car(make,model){
    this.make = make;
    this.model = model;
    this._userGears = ['P','N','R','D'];
    this._userGear = this._userGears[0];
}

class Es6Car {}
function Es5Car {}
> typeof Es6Car // "function"
> typeof Es5Car // "function"
```

사실 class는 단축 문법일 뿐이며 JS의 클래스 자체가 바뀐 것은 아니다. 클래스는 함수일 뿐이다.

### 2-3 프로토타입
클래스의 인스턴스에서 사용할 수 있는 메서드라고 하면 그건 **프로토타입(prototype) 메서드**를 말하는 것이다. `Array`의 `forEach`를 `Array.prototype.forEach`라고 쓰는 것과 동일하다.

최근에는 프로토타입 메서드를 `Array#forEach` 처럼 `#`으로 표시하는 표기법이 널리 쓰인다.

모든 함수에는 `prototype`이라는 특별한 프로퍼티가 있다. 일반적인 함수에서는 프로토타입을 사용할 일이 없지만, **객체 생성자(클래스)로 동작하는 함수**에서는 프로토타입이 대단히 중요하다.

함수의 `prototype` 프로퍼티가 중요해지는 시점은 **new 키워드로 새 인스턴스를 만들었을 때**이다. `new` 키워드로 만든 새 객체는 생성자의 `prototype` 프로퍼티에 접근할 수 있다. 객체 인스턴스는 생성자의 `prototype` 프로퍼티를 `__proto__` 프로퍼티에 저장한다. 밑줄 두 개로 둘러싼 프로퍼티는 JS의 내부 동작 방식에 영향을 미치기에 되도록 손대지 않는 것이 좋다.

프로토타입에서 중요한 것은 **동적 디스패치**라는 메커니즘이다. 객체의 프로퍼티나 메서드에 접근하려 할 때 그런 프로퍼티나 메서드가 존재하지 않으면 JS는 객체의 프로토타입에서 해당 프로퍼티나 메서드를 찾는다. 클래스의 인스턴스는 모두 같은 프로토타입을 공유하므로 프로토타입에 프로퍼티나 메서드가 있다면 해당 클래스의 인스턴스는 모두 그 프로퍼티나 메서드에 접근할 수 있다.

**클래스의 프로토타입에서 데이터 프로퍼티를 수정하는 것은 일반적으로 권장하지 않는다.** 인스턴스 중 하나에 동일 이름의 프로퍼티가 있다면 해당 인스턴스는 프로토타입에 있는 값이 아닌 인스턴스에 있는 값을 사용한다. 이는 혼란과 버그를 초래할 수 있기에 초깃값이 필요하다면 생성자에서 만드는 편이 낫다.

```javascript
// Car 클래스는 이전에 만든 거
const car1 = new Car();
const car2 = new Car();
car1.shift === Car.prototype.shift; // true
car1.shift('D');
car1.shift('d'); // error
car1.userGear; // 'D'
car1.shift === car2.shift // true

car1.shift = function(gear) {this.userGear = gear.toUppercase();}
car1.shift === Car.prototype.shift; // false
car1.shift === car2.shift; // false
car1.shift('d');
car1.userGear; // 'D'
```

인스턴스에서 메서드나 프로퍼티를 정의하면 프로토타입에 있는 것을 가리는 효과가 있다. JS는 먼저 인스턴스를 체크하고 거기에 없으면 프로토타입을 체크하기 때문이다.

위의 예제처럼 `car1` 객체에는 `shift` 메서드가 없지만, `car1.shift('D')`를 호출하면 JS는 `car1`의 프로토타입에서 그런 이름의 메서드를 검색한다. `car1`에 `shift` 메서드를 추가하면 이후에 프로토타입의 메서드는 호출되지 않는다. 이것을 통해 동적 디스패치가 어떻게 구현되는지 알 수 있다.

### 2-4 정적 메서드
인스턴스 메서드 외에도 **정적메서드**(클래스 메서드)가 있다. 이 메서드는 특정 인스턴스에 적용되지 않는다. 정적 메서드에서 `this`는 인스턴스가 아니라 **클래스 자체**에 묶인다. 하지만 일반적으로 정적 메서드에는 `this` 대신 클래스 이름을 사용하는 것이 좋은 습관이다.

```javascript
class Car {
    static getNextVin(){
        return Car.nextVin++;
        // this대신 Car를 앞에 쓰면 
        //정적 메서드라는 점을 상기하기 쉽다.
    }
    constructor(make,model) {
        this.make = make;
        this.model = model;
        this.vin = Car.getNextVin();
    }
    static areSimilar(car1,car2) {
        return car1.make===car2.make && car1.model===car2.model;
    }
    static areSame(car1,car2) {
        return car1.vin===car2.vin;
    }
}
Car.nextVin=0;

const car1 = new Car("Tesla","S");
const car2 = new Car("Mazda","3");
const car3 = new Car("Mazda","3");

car1.vin; // 0
car2.vin; // 1
car3.vin; // 2

Car.areSimilar(car1,car2); // false
Car.areSimilar(car2,car3); // ture
Car.areSame(car2,car3); // false
Car.areSame(car2,car2); // true
```

정적 메서드는 클래스에 관련되지만 인스턴스와는 관련이 없는 범용적인 작업에 사용된다. 그리고 여러 인스턴스를 대상으로 하는 작업에도 종종 쓰인다.

### 2-5 상속
**상속**은 한 단계로 끝나지 않는다. 객체의 프로토타입에서 메서드를 찾지 못하면 자바스크립트는 프로토타입의 프로토타입을 검색한다. 프로토타입 체인은 이런식으로 만들어진다. 조건에 맞는 프로토타입을 찾지 못하면 에러를 일으킨다.

프로토타입 체인에서 가장 적절한 위치에 메서드를 정의해야 효율적인 구조를 만들 수 있다.

```javascript
class Vehicle {
    constructor(){
        this.passengers = [];
        console.log("Vehicle created");
    }
    addPassenger(p) {
        this.passengers.push(p);
    }
}

// Car를 Vehicle의 서브클래스로 만듦
class Car extends Vehicle {
    constructor() {
        // 슈퍼클래스의 생성자를 호출하는 함수
        super();
        console.log("Car created");
    }
    deployAirbags() {
        console.log("BWOOSH!");
    }
}

const v = new Vehicle();
v.addPassenger("Frank");
v.addPassenger("Judy");
v.passengers; // ["Frank", "Judy"]

const c = new Car();
c.addPassenger("Alice");
c.addPassenger("Cameron");
c.passengers; // ["Alice","Cameron"]

v.deployAirbags(); // error
c.deployAirbags(); // "BWOOSH!"
```
서브클래스에서 `super` 함수를 반드시 호출해야하며 그렇지 않으면 에러가 일어난다.

예제에서 볼 수 있듯이 상속은 단방향이다.

### 2-6 다형성
```javascript
class Motorcycle extends Vehicle {}
const c = new Car();
const m = new Motorcycle();
c instanceof Car; // true
c instanceof Vehicle // true
m instanceof Car; // false
m instanceof Motorcycle; //true
m instanceof Vehicle; //true
```

**다형성**(polymorphism)은 객체지향 언어에서 여러 슈퍼클래스의 멤버인 인스턴스를 가리킨다. JS는 느슨한 타입을 사용하고 어디서든 객체를 쓸 수 있으므로, 어떤 면에서 JS의 객체는 모두 다형성을 갖고 있다고 할 수 있다.

JS의 모든 객체는 루트 클래스인 Object의 인스턴스이다. 즉, 객체 o에서 o instanceof Object는 항상 true이다(__proto__프로퍼티를 수정한다면 다른 결과가 나올수 있으며 건들면 안된다).

### 2-7 객체 프로퍼티 나열 다시보기
객체 obj와 프로퍼티 x에서, obj.hasOwnProperty(x)는 obj에 프로퍼티 x가 있다면 true를 반환하며, 프로퍼티 x가 obj에 정의되지 않았거나 프로토타입 체인에만 정의되었다면 false를 반환한다.

```javascript
class Super {
    constructor() {
        // 인스턴스에 정의
        this.name = 'Super';
        this.isSuper = true;
    }
}

// 유효하지만, 권장하지 않는다.
// 슈퍼클래스의 프로토타입에 직접 정의
Super.prototype.sneaky = 'not recommended!';

class Sub extends Super {
    constructor(){
        super();
        // 인스턴스에 정의
        this.name = 'Sub';
        this.isSub = true;
    }
}

const obj = new Sub();

for(let p in obj) {
    console.log(`${p}: ${obj[p]}` + 
    (obj.hasOwnProperty(p) ? '' : ' (inherited)'))
}
// name: Sub
// isSuper: true
// isSub: true
// sneaky: not recommended! (inherited)
```

ES6 클래스를 설계 의도대로 사용한다면 데이터 프로퍼티는 항상 프로토타입 체인이 아니라 인스턴스에 정의해야 한다. 하지만 프로퍼티를 프로토타입에 정의하지 못하도록 강제하는 장치는 없으므로 확실히 확인하려면 항상 hasOwnProperty를 사용하는 편이 좋다.

### 2-8 문자열 표현
```javascript
class Car {
    toString() {
        return `${this.make} ${this.model}: ${this.vin}`;
    }
    //...
}
```
모든 객체는 Object를 상속하므로 Object의 메서드는 기본적으로 모든 객체에서 사용할 수 있다. 객체의 기본적인 문자열 표현을 제공하는 toString도 그런 메서드 중 하나이다. 기본 동작은 쓸모 없으나 객체에 관한 중요한 정보를 제공한다면 디버깅에도 유용하고, 객체를 한 눈에 파악할 수 있다.

## 3) 다중 상속, 믹스인, 인터페이스
다중 상속(multiple inheritance)는 클래스가 슈퍼클래스 두 개를 가지는 기능이며, 슈퍼클래스의 슈퍼클래스가 존재하는 일반적인 상속과는 다르다. 다중 상속은 동일한 메서드가 존재할 때 등의 충돌의 위험이 있다.

```javascript
class InsurancePolicy() {}
function makeInsurable(o) {
    o.addInsurancePolicy = function(p) {this.insurancePolicy = p;}
    o.getInsurancePolicy = function() {return this.insurancePolicy;}
    o.isInsured = function() {return !!this.insurancePolicy;}
}

makeInsurable(Car); // error

const car1 = new Car();
car1.addInsurancePolicy(new InsurancePolicy()); // error

// 되지만 모든 자동차에서 makeInsurable 호출 필요
const car1 = new Car();
makeInsurable(car1);
car1.addInsurancePolicy(new InsurancePolicy()); // works

// 보험 관련 메서드들은 모두 Car 클래스에 정의된 것처럼 동작
makeInsurable(Car.prototype);
const car1 =new Car();
car1.addInsurancePolicy(new InsurancePolicy()); // works
```

JS가 다중 상속이 필요한 문제에 대한 해답으로 내놓은 개념이 믹스인(mixin)이다. 믹스인은 기능을 필요한 만큼 섞어 놓은 것이다. JS는 느슨한 타입을 사용하고 대단히 관대한 언어이므로 그 어떤 기능이라도 언제든, 어떤 객체에든 추가할 수 있다.

```javascript
class InsurancePolicy() {}
const ADD_POLICY = Symbol();
const GET_POLICY = Symbol();
const IS_INSURED = Symbol();
const _POLICY = Symbol();
function makeInsurable(o) {
    o[ADD_POLICY] = function(p) { this[_POLICY] = p;}
    o[GET_POLICY] = function() {return this[_POLICY];}
    o[IS_INSURED] = function() {return !!this[_POLICY];}
}
```

그러나 믹스인이 모든 문제를 해결해 주지는 않기에 심볼을 이용해 문제 일부를 경감 시킬 수 있다. 만약 Car 클래스의 메서드와의 충돌을 방지한다고 하면 위와 같이 믹스인을 작성할 수 있다.

# Chapter 10 맵과 셋
맵(map)과 셋(set)은 ES6에서 새로 도입한 데이터 구조이다.

## 1) 맵
ES6 이전에는 객체를 사용해야 키와 값을 연결할 수 있었다. 이런 경우에 발생하는 단점은 다음과 같다.

- 프로토타입 체인 때문에 의도하지 않은 연결이 생길 수 있다.
- 객체 안에 연결된 키와 값이 몇 개나 되는지 쉽게 알아낼 수 있는 방법이 없다.
- 키는 반드시 문자열이나 심볼이어야 하므로 객체를 키로 써서 값과 연결할 수 없다.
- 객체는 프로퍼티 순서를 전혀 보장하지 않는다.

Map 객체는 이들 결함을 모두 해결했고, 키와 값을 연결할 목적이면 Map 객체를 사용하는 것이 좋다.

```javascript
const u1 = {name:'Cynthia'};
const u2 = {name:'Jackson'};
const u3 = {name:'Olive'};
const u4 = {name:'James'};

// #1
const userRoles = new Map();
userRoles.set(u1,'User');
userRoles.set(u2,'User');
userRoles.set(u3,'Admin');

// #2 체인으로 연결
const userRoles = new Map();
userRoles
    .set(u1,'User')
    .set(u2,'User')
    .set(u3,'Admin');

// #3 생성자에 배열의 배열을 넘김
const userRoles = new Map([
    [u1,'User'],
    [u2,'User'],
    [u3,'Admin'],
]);
```

위와 같이 선언을 하면 된다.

```javascript
userRoles.has(u1); // true, 키 존재 확인
userRoles.get(u4); // undefined
userRoles.get(u1); // 'User'
userRoles.set(u1,'Admin'); // 값 교체
userRoles.get(u1); // 'Admin'
userRoles.size; // 3
```

has(), get(), set() 메서드를 사용하여 데이터를 다룰 수 있다.

```javascript
for(let u of userRoles.keys())
    console.log(u.name);
// Cynthia
// Jackson
// Olive

for(let r of userRoles.values())
    console.log(r);
// Admin
// User
// Admin

for(let ur of userRoles.entries())
    console.log(`${ur[0].name}: ${ur[1]}`);
// Cynthia: Admin
// Jackson: User
// Olive: Admin

//맵도 분해(destruct)할 수 있다.
for(let [u,r] of userRoles.entries())
    console.log(`${u.name}: ${r}`);
// Cynthia: Admin
// Jackson: User
// Olive: Admin

// entries() 메서드는 맵의 기본 이터레이터라 
// 아래와 같이 단축해서 사용할 수 있다.
for(let [u,r] of userRoles)
    console.log(`${u.name}: ${r}`);
// Cynthia: Admin
// Jackson: User
// Olive: Admin
```

keys() 메서드는 맵의 키를, values() 메서드는 값을, entries() 메서드는 첫 번째 요소가 키이고 두 번째 요소가 값인 배열을 각각 반환한다. 모두 이터러블 객체를 반환하므로 for...of 루프를 사용할 수 있다.

```javascript
// 배열이 필요하면 확산 연산자(spread operator) 사용
[...userRoles.values()]; // ["Admin","User","Admin"]

// 맵의 한 요소 삭제
userRoles.delete(u2);
userRoles.size; // 2

// 맵의 요소를 모두 삭제
userRoles.clear();
userRoles.size; // 0
```

## 2) 위크맵
WeakMap은 다음 차이점을 제외하면 Map과 같다.
- 키는 반드시 객체
- WeakMap의 키는 가비지 콜렉션에 포함될 수 있음
- WeakMap은 이터러블이 아니며 clear() 메서드도 없다.

```javascript
const SecretHolder = (function(){
    const secrets = new WeakMap();
    return class {
        setSecret(secret){
            secrets.set(this, secret);
        }
        getSecret(){
            return secrets.get(this);
        }
    }
})();

const a = new SecretHolder();
const b = new SecretHolder();

a.setSecret('secret A');
b.setSecret('secret B');
a.getSecret(); // 'secret A'
b.getSecret(); // 'secret B'
```

이러한 특징으로 객체 인스턴스의 private 키를 저장하기에 알맞다.
예제는 위크맵과 그 위크맵을 사용하는 클래스와 함께 IIFE에 넣었다. 결과적으로 비밀을 저장할 때 setSecret 메서드를 쓰고, 보려 할 때는 getSecret 메서드를 쓰는 SecretHolder 클래스를 얻게 된다.

## 3) 셋
```javascript
const roles = new Set();
roles.add("User"); // Set ["User"]
roles.add("Admin"); // Set ["User", "Admin"]

roles.size; // 2
roles.add("User"); // Set ["User", "Admin"]
roles.size; // 2

roles.delete("Admin"); // true
roles; // Set ["User"]
roles.delete("Admin"); // false
```

셋은 중복을 허용하지 않는 데이터 집합이다.

## 4) 위크셋
```javascript
const naughty = new WeakSet();

const children = [
    {name: "Suzy"},
    {name: "Derek"},
];

naughty.add(children[1]);

for(let child of children){
    if(naughty.has(child))
        console.log(`Coal for ${child.name}!`);
    else
        console.log(`Presents for ${child.name}!`);
}
// Presents for Suzy!
// Coal for Derek!
```

위크셋은 객체만 포함할 수 있으며, 이 객체들은 가비지 콜렉션의 대상이 된다. WeakMap과 마찬가지로 WeakSet도 이터러블이 아니므로 위크 셋의 용도는 매우 적다. 주어진 객체가 셋 안에 존재하는지 여부를 알아보는 것에만 사용된다.

# Chapter 11 예외와 에러 처리
예외 처리(exeception handling)는 에러를 컨트롤하는 메커니즘이다. 예상치 못한 상황에 대처하는 방식이며 예상한 에러와 예상치 못한 에러(예외)를 구분하는 기준은 불명확하고 상황에 따라 크게 달라진다.

## 1) Error 객체
```javascript
// instanceof 연산자와 써서 Error 인스턴스가 반환됐는지 확인
// 에러메시지는 Error 인스턴스의 message 프로퍼티에 있다.
function validateEmail(email){
    return email.match(/@/) ?
        email :
        new Error(`invalid email: ${email}`);
}

const email = "janedoe.com";

const validatedEmail = validateEmail(email);
if(validatedEmail instanceof Error){
    console.error(`Error: ${validatedEmail.message}`);
} else {
    console.log(`Valid email: ${validatedEmail}`);
}
// Error: invalid email: janedoe.com
```
JS에는 내장된 Error 객체가 있고 이 객체는 에러 처리에 간편하게 사용할 수 있다. Error 인스턴스를 만들면서 에러 메시지를 지정할 수 있다. 이 인스턴스는 에러와 통신하는 수단이다. 주로 예외 처리에서 더 자주 사용된다.

## 2) try/catch와 예외 처리
뭔가를 시도(try)하고, 예외가 있으면 그것을 캐치(catch)한다는 것처럼 예상치 못한 에러를 대치할 수 있다.

```javascript
const email = null;

try {
    const validatedEmail = validateEmail(email);
    if(validatedEmail instanceof Error) {
        console.error(`Error: ${validatedEmail.message}`);
    } else {
        console.log(`Valid email: ${validatedEmail}`);
    }
} catch(err) {
    console.error(`Error: ${err.message}`);
}

// Error: Cannot read property 'match' of null
```

에러를 캐치했으므로 프로그램은 멈추지 않는다. 엘어가 일어나는 즉시 catch 블록으로 이동한다. 즉, validatedEmail을 호출한 다음에 있는 if문은 실행되지 않는다. try 블록 안에 쓸 수 있는 문의 숫자에 제한은 없고 그중 에러가 일어나는 문에서 실행 흐름을 catch 블록으로 넘긴다.

## 3) 에러 일으키기
JS가 에러를 일으키기만 기다릴 필요 없이 직접 에러를 일으켜서(throw,raise) 예외 처리 작업을 시작할 수 있다.
JS는 에러를 일으킬 때 꼭 객체만이 아니라 숫자나 문자열 등 어떤 값이든 catch 절에 넘길 수 있다. 하지만 Error 인스턴스를 넘기는 것이 편하다. 대부분의 catch 블록은 Error 인스턴스를 받을 것이라고 간주하고 만든다.

```javascript
function billPay (amount, payee, account) {
    if(amount > account.balance)
        throw new Error("insufficient funds");
    account.transfer(payee, amount);
}
```

throw를 호출하면 현재 함수는 즉시 실행을 멈춘다. 따라서 위 예제에서 account.transfer가 호출되지 않으므로 잔고가 부족한데도 현금을 찾아가는 사고는 발생하지 않는다.

## 4) 예외 처리와 호출 스택
프로그램이 함수 a를 호출하고, 그 함수는 다른 함수 b를 호출하고, 호출된 함수는 또 다른 함수 c를 호출하는 일이 반복된다. JS 인터프리터는 이런 과정을 모두 추적하고 있어야한다. a, b 함수들은 완료되지 않고 쌓이는데 이를 호출 스택(call stack)이라 부른다.

에러는 호출 스택 어디에서든 캐치할 수 있다. 어디에서 이 에러를 캐치하지 않으면 JS 인터프리터는 프로그램을 멈춘다. 이런 것을 처리하지 않은(unhandled) 예외, 캐치하지 않은(uncaught) 예외라고 부르며 프로그램이 충돌하는 원인이 된다. 에러가 일어날 수 있는 곳은 다양해서 모두다 캐치하기는 어렵다.

```javascript
function a() {
    console.log('a: calling b');
    b();
    console.log('a: done');
}
function b() {
    console.log('b: calling c');
    c();
    console.log('b: done');
}
function c() {
    console.log('c: throwing error');
    throw new Error('c error');
    console.log('c: done');
}
function d() {
    console.log('d: calling c');
    c();
    console.log('d: done');
}

try {
    a();
} catch(err) {
    console.log(err.stack);
}

try {
    d();
} catch(err) {
    console.log(err.stack);
}
// a: calling b
// b: calling c
// c: throwing error
// Error: c error
// ...생략
// d: calling c
// c: throwing error
// Error: c error
// ...생략
```

에러를 캐치하면 호출 스택에서 발생한 문제를 해결하는데에 유용한 정보를 얻을 수 있다.

## 5) try...catch...finally
try 블록의 코드가 HTTP 연결이나 파일 같은 일종의 '자원'을 처리할 때가 있다. 프로그램에서 이 자원을 계속 가지고 있을 수 없으므로 에러 여부와 상관 없이 어느 시점에서는 이 자원을 해제해야 한다. 만약 에러가 난다면 자원을 해제할 기회가 사라지므로 try 블록에서 자원을 해제하는 건 안전하지 않다. 또한 에러가 일어나지 않으면 실행되지 않는 catch 블록 역시 안전하지 않다. 이런 상황에서 finally 블록이 필요하다. 

```javascript
try {
    console.log("this line is executed...");
    throw new Error("whoops");
    console.log("this line is not...");
} catch(err) {
    console.log("there was an error...");
} finally {
    console.log("...always executed");
    console.log("perform cleanup here");
}
// this line is executed...
// there was an error...
// ...always executed
// perform cleanup here
```

finally 블록은 에러가 일어나든, 일어나지 않든 반드시 호출된다.

예외 처리 자체도 대가를 지불해야 하는 연산이다. 예외는 catch 블록을 만날 때까지 스택을 거슬러 올라가야 하므로 JS 인터프리터가 예외를 계속 추적하고 있어야 한다. 자주 실행되는 코드에서 예외를 발생시키면 성능 문제가 발생할 가능성이 있다.

프로그램을 일부러 멈추려 하는 게 아니라면, 예외를 일으켰으면 반드시 캐치해야 한다. 원인 없는 결과는 없는 법이다. 예외 처리는 예상할 수 없는 상황에 대비한 마지노선으로 생각하고, 예상할 수 있는 에러는 조건문으로 처리하는 것이 최선이다.

# Chapter 12 이터레이터와 제너레이터

 ES6에서 매우 중요한 새로운 개념 이터레이터(iterator)와 제너레이터(generator)를 도입했다. 제너레이터는 이터레이터에 의존하는 개념이다.

이터레이터는 '지금 어디 있는지' 파악할 수 있도록 돕는다는 면에서 일종의 책갈피와 비슷한 개념이다. 예시로 배열이 이터러블(iterable) 객체의 좋은 예이다. 

```javascript
const book = [
    "Twinkle, twinkle, little star",
    "How I wonder what you are!",
    "Up above the world so high",
    "Like a diamond in the sky!",
];

// values 메서드를 이용하여 이터레이터 생성
const it = book.values();
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());

// { value: 'Twinkle, twinkle, little star', done: false }
// { value: 'How I wonder what you are!', done: false }
// { value: 'Up above the world so high', done: false }
// { value: 'Like a diamond in the sky!', done: false }
// { value: undefined, done: true }
// { value: undefined, done: true }
```

next에서 마지막을 반환했다 해서 끝난 것은 아니다. 더 진행할 것이 없으면 value는 undefined가 되지만, next는 계속 호출할 수 있다. 일단 이터레이터가 끝까지 진행하면 뒤로 돌아가서 다른 데이터를 제공할 수 없다.

배열의 요소를 나열하는 것이 목적이라면 for 루프나 for...of 루프를 쓸 수 있다. for 루프는 인덱스를 사용하지만 for...of 루프는 이터레이터라서 인덱스 없이 사용 가능하다.

이터레이터는 모두 독립적이라 새 이터레이터를 만들 때마다 처음에서 시작한다. 그리고 각각 다른 요소를 가리키는 이터레이터 여러 개를 동시에 사용할 수도 있다.

## 1) 이터레이션 프로토콜
이터레이터 프로토콜은 모든 객체를 이터러블 객체로 바꿀 수 있다.

```javascript
class Log {
    constructor() {
        this.messages = [];
    }
    add(messages) {
        this.messages.push({messages,timestamp:Date.now()});
    }
    [Symbol.iterator](){
        return this.messages.values();
    }
}

const log = new Log();
log.add("first day at sea");
log.add("spotted whale");
log.add("spotted another vessel");

// 배열처럼 순회
for (let entry of log) {
    console.log(`${entry.messages} @ ${entry.timestamp}`);
}

// first day at sea @ 1554126308321
// spotted whale @ 1554126308321
// spotted another vessel @ 1554126308321
```

이터레이션 프로토콜은 클래스에 심볼 메서드 Symbol.iterator가 있고 이 메서드가 이터레이터처럼 동작하는 객체, 즉 value와 done 프로퍼티가 있는 객체를 반환하는 next 메서드를 가진 객체를 반환한다면 그 클래스의 인스턴스는 이터러블 객체라는 뜻이다.

```javascript
class Log {
    //...
    [Symbol.iterator]() {
        let i = 0;
        const messages = this.messages;
        return {
            next() {
                if(i>=messages.lenght)
                    return { values: undefined, done: true};
                return {values: messages[i++], done: false};
            }
        }
    }
}
```

위와 같이 직접 이터레이터를 만들 수도 있다.

## 2) 제너레이터
제너레이터는 이터레이터를 사용해 자신의 실행을 제어하는 함수다. 일반적인 함수는 매개변수를 받고 값을 반환하지만, 호출자는 매개변수 외에는 함수의 실행을 제어할 방법이 전혀 없다. 함수를 호출하면 그 함수가 종료될 때까지 제어권을 완전히 넘기는 것이다. 제너레이터에서는 그렇지 않다.

- 함수의 실행을 개별적 단계로 나눔으로써 함수의 실행을 제어한다.
- 실행 중인 함수와 통신한다.
- 언제든 호출자에게 제어권을 넘길(yield) 수 있다.
- 호출한 즉시 실행되지는 않고 이터레이터를 반환한다. 이터레이터의 next 메서드를 호출함에 따라 실행된다.

제너레이터를 만들 떄는 function 키워드 뒤에 '*' 를 붙인다. 이것을 제외하면 문법은 일반적인 함수와 같다.

```javascript
function* rainbow() {
    yield 'red';
    yield 'orange';
    yield 'yellow';
    yield 'green';
    yield 'blue';
    yield 'indigo';
    yield 'violet';
}

const it = rainbow();
console.log(it.next());
console.log(it.next());
console.log(it.next());

// 제너레이터는 이터레이터를 반환하므로 
// for...of를 사용할 수 있다.
for(let color of rainbow()){
    console.log(color);
}

// { value: 'red', done: false }
// { value: 'orange', done: false }
// { value: 'yellow', done: false }
// red
// orange
// yellow
// green
// blue
// indigo
// violet
```

### 2-1 yield 표현식과 양방향 통신
제너레이터와 호출자 사이의 양방향 통신은 yield 표현식을 통해 이뤄진다. 표현식은 값으로 평가되고 yield는 표현식이므로 반드시 어떤 값으로 평가된다. yield 표현식의 값은 호출자가 제너레이터의 이터레이터에서 next를 호출할 때 제공하는 매개변수이다.

```javascript
function* interrogate() {
    const name = yield "What is your name?";
    const color = yield "What is your favorite color?";
    return `${name}'s favorite color is ${color}.`;
}

const it =interrogate();
console.log(it.next()); // 'undefined'를 제너레이터에 넘김
console.log(it.next('Ethan')); // name에 'Ethan' 초기화
console.log(it.next('orange')); // color에 'orange' 초기화

// { value: 'What is your name?', done: false }
// { value: 'What is your favorite color?', done: false }
// { value: 'Ethan\'s favorite color is orange.', done: true }
```

next를 호출하면 제너레이터는 첫 번째 행을 실행하려 한다. 하지만 그 행에는 yield 표현식이 들어 있으므로 제너레이터는 반드시 제어권을 호출자에게 넘겨야 한다. 제너레이터의 첫 번째 행이 완료(resolve)되려면 호출자가 next를 다시 호출해야 한다. 그러면 name은 next에서 전달하는 값을 받는다.

호출자가 제너레이터에 정보를 전달하므로, 제너레이터는 그 정보에 따라 자신의 동작 방식 자체를 바꿀 수 있다.

제너레이터는 화살표 표기법으로 만들 수 없으며 반드시 function*을 써야한다.

### 2-2 제너레이터와 return
yield 문은, 제너레이터의 마지막 문이라도 제너레이터를 끝내지 않는다. return 문을 사용하면 그 위치와 관계없이 done은 true가 되고, value 프로퍼티는 return이 반환하는 값이 된다.

```javascript
function* abc() {
    yield 'a';
    yield 'b';
    return 'c';
}

const it = abc();
console.log(it.next());
console.log(it.next());
console.log(it.next());

for(let l of abc()){
    console.log(l);
}

// { value: 'a', done: false }
// { value: 'b', done: false }
// { value: 'c', done: true }
// a
// b
```

제너레이터를 사용할 때는 보통 done이 true이면 value 프로퍼티에 주의를 기울이지 않는다는 점을 염두해야 한다. 예를 들어 for...of 루프에서 사용하면 c는 출력되지 않는다.

그러므로 제너레이터가 반환하는 값을 사용하려 할 때는 yield, 중간에 종료하는 목적으로 사용하려 할 때는 return을 사용하도록 한다.

이터레이터로 할 수 있는 일은 ES6 이전에도 모두 할 수 있었지만 중요하면서도 자주 사용하는 패턴을 표준화했다는 점에서 의미가 있다.

# Chapter 13 함수와 추상적 사고

## 1) 서브루틴으로서의 함수
서브루틴(subroutine)은 아주 오래 된 개념이며 복잡한 코드를 간단하게 만드는 기초적인 수단이다. 프로시저(procedure), 루틴(routine), 서브프로그램(subprogram), 매크로(macro) 등 다양한 이름으로 불린다.

서브루틴은 대개 어떤 알고리즘을 나타내는 형태이다.

## 2) 값을 반환하는 서브루틴으로서의 함수
`return`을 사용해서 값을 반환할 수 있다.

## 3) 함수로서의 함수
입력은 모두 어떤 결과와 관계되어 있다. 함수의 수학적인 정의에 충실한 함수를 순수한 함수(pure function)이라고 부른다. 입력이 같으면 결과도 반드시 같다는 점과 부수 효과(side effect)가 없다는 특징, 즉 프로그램의 상태가 바뀌어서는 안된다는 특징을 갖고 있다. 

```javascript
const colors = ['red','orange','yellow','green',
    'blue','indigo','violet'];
let colorIndex = -1;
function getNextRainbowColor(){
    if(++colorIndex >= colors.length) colorIndex = 0;
    return colors[colorIndex];
}
```

위 함수는 순수한 함수의 두 가지 정의를 모두 어긴다. 입력이 같아도 결과가 항상 다르고, getNextRainbowColor 함수에 속하지도 않은 변수 colorIndex를 바꾸는 부수 효과가 있다. 이를 순수한 함수를 만드려면 다음과 같이 변경해야한다.

```javascript
function getRainbowIterator(){
    const colors = ['red','orange','yellow','green',
        'blue','indigo','violet'];
    let colorIndex = -1;
    return {
        next() {
            if(++colorIndex >= colors.length) colorIndex = 0;
            return colors[colorIndex];
        }
    };
}

const rainbowIterator = getRainbowIterator();
setInterval(function(){
    // 브라우저 코드 사용
    document.querySelector('.rainbow')
        .style['background-color'] = rainbowIterator.next().value;
},500);
```

next()는 함수가 아니라 멤서드라는 점에 주목할 필요가 있다. 메서드는 자신이 속한 객체라는 컨텍스트 안에서 동작하므로 메서드의 동작은 그 객체에 의해 좌우된다. 프로그램의 다른 부분에서 getRainbowIterator를 호출하더라도 독립적인 이터레이터가 생성되므로 다른 이터레이터를 간섭하지 않는다.

## 4) 그래서?
함수를 서브루틴이라는 관점에서 보면 반복을 없애는 점에서 장점이 있다. 자주 사용하는 동작을 하나로 묶을 수 있다는 점에 매우 분명한 장점이 있다.

순수한 함수는 사용하면 코드를 테스트하기 쉽고, 이해하기 쉽고, 재사용하기가 쉽다.

함수가 상황에 따라 다른 값을 반환하거나 부작용이 있다면 그 함수는 컨텍스트에 좌우되는 함수이다. 99%는 제대로 동작하다가 1% 상황에서 버그를 일으키는 상황은 심각하다. 가장 악질적인 버그는 숨어 있는 버그이므로 순수한 함수를 사용하길 권장한다.

### 4-1 함수도 객체다
JS 함수는 Function 객체의 인스턴스이다. v가 함수더라도 v instanceof Object는 여전히 true를 반환하므로, 변수가 함수인지 아닌지 확인하고 싶다면 먼저 typeof를 써보는 편이 좋다.

## 5) IIFE와 비동기적 코드
IIFE를 사용하는 사례 중 하나는 비동기적 코드가 정확히 동작할 수 있도록 새 변수를 새 스코프에 만드는 것이다. 

```javascript
var i;
for(i=5; i>=0; i--) {
    setTimeout(function() {
        console.log(i===0?'go!':i);
    },(5-i)*1000);
}
// -1이 6번 출력
```

setTimeout에 전달된 함수가 루프 안에서 실행되지 않고 루프가 종료된 뒤에 실행됐기 때문에 -1이 6번 출력됐다. -1이 되기 전에 콜백 함수는 전혀 호출되지 않았다. 따라서 콜백 함수가 호출되는 시점에서 i의 값은 -1이다.

```javascript
function loopBody(i) {
    setTimeout(function() {
        console.log(i===0?'go!':i);
    },(5-i)*1000);
}
var i;
for(i=5; i>=0; i--) {
    loopBody(i);
}
// 5
// 4
// 3
// 2
// 1
// go!
```

블록 스코프 변수가 도입되기 전에는 이런 문제를 해결하기 위해 함수를 하나 더 썼다. 함수를 하나 더 쓰면 스코프가 새로 만들어지고 각 단계에서 i의 값이 클로저에 캡처된다.

```javascript
// IIFE 사용
var i;
for(i=5; i>=0; i--) {
    (function(i) {
        setTimeout(function(){
            console.log(i===0?"go!":i);
        },(5-i)*1000);
    })(i);
}

// 블록 스코프 변수 사용
for(let i=5; i>=0; i--) {
    setTimeout(function(){
        console.log(i===0?"go!":i);
    },(5-i)*1000);
}
// 5
// 4
// 3
// 2
// 1
// go!
```

블록 스코프 변수를 사용함으로써 함수를 새로 만드는 일을 하지 않아도 된다. 이 경우 JS는 루프의 단계마다 변수 i의 복사본을 새로 만든다. 만약 let을 for 문 밖에 선언했다면 -1만 출력될 것이다.

## 6) 변수로서의 함수
함수도 다른 변수와 마찬가지로 이리저리 전달할 수 있다. 함수는 호출되었을 때는 능동적이며 호출하기 전에는 다른 변수와 마찬가지로 수동적이다. 변수가 있을 수 있는 곳에는 함수도 있을 수도 있다.

- 함수를 가리키는 변수를 만들어 별명을 정할 수 있다.
- 배열에 함수를 넣을 수 있다. 물론 다른 타입의 데이터와 섞일 수 있다.
- 함수를 객체의 프로퍼티로 사용할 수 있다.
- 함수를 함수에 전달할 수 있다.
- 함수가 함수를 반환할 수 있다.
- 함수를 매개변수로 받는 함수를 반환하는 것도 물론 가능하다.

```javascript
// require는 라이브러리를 불러오는 노드 함수
const Money = require('math-money');

// oneDollar와 twoDollar는 같은 타입의 인스턴스
const oneDollar = Money.Dollar(1);
const Dollar = Money.Dollar;
const twoDollars = Dollar(2);
```

### 6-1 배열 안의 함수
```javascript
const sin = Math.sin;
const cos = Math.cos;
const theta = Math.PI/4;
const zoom = 2;
const offset = [1,-3];

const pipeline=[
    function rotate(p) {
        return {
            x: p.x*cos(theta) - p.y*sin(theta),
            y: p.x*sin(theta) + p.y*cos(theta),
        };
    },
    function scale(p) {
        return {x:p.x*zoom, y:p.y*zoom};
    },
    function translate(p) {
        return {x:p.x+offset[0],y:p.y+offset[1]};
    },
];

const p = {x:1,y:1};
let p2 = p;
for (let i = 0; i<pipeline.length; i++) {
    p2 = pipeline[i](p2);
    console.log(p2);
}
// p2는 이제 p1을 좌표 원점 기준으로 45도 회전(rotate),
// 원점에서 2단위만큼 떨어뜨린 후(scale),
// 1단위 오른쪽, 3단위 아래쪽으로 움직인다.(translate)

// { x: 1.1102230246251565e-16, y: 1.414213562373095 }
// { x: 2.220446049250313e-16, y: 2.82842712474619 }
// { x: 1.0000000000000002, y: -0.17157287525381015 }
```

자주 하는 일을 한 셋으로 묶는 파이프라인이 좋은 예이다. 배열을 사용하면 작업 단계를 언제든 쉽게 바꿀 수 있다는 장점이 있다. 일정한 순서에 따라 함수를 실행해야 한다면 파이프라인을 사용하는 것이 좋다.

### 6-2 함수에 함수 전달
함수에 함수를 전달하는 다른 용도는 비동기적 프로그래밍이다. 이런 용도로 전달하는 함수를 보통 콜백(callback)이라고 부르며, 약자로 cb를 쓸 때가 많다.

```javascript
function sum(arr,f) {
    // 함수가 전달되지 않았으면 매개변수를 그대로 반환하는 null 함수를 쓴다.
    if(typeof f != 'function') f= x => x;
    return arr.reduce((a,x) => a += f(x));
}
sum([1,2,3]); // 6
sum([1,2,3], x => x*x); // 14
sum([1,2,3], x => Math.pow(x,3)); //36
```

함수는 동작이고, 함수를 받은 함수는 그 동작을 활용할 수 있다. 예제에서 에러를 방지하기 위해 함수가 아닌 것은 모두 'null 함수', 즉 아무 일도 하지 않은 것으로 바꾼다.

### 6-3 함수를 반환하는 함수
함수를 반환하는 함수는 아마 함수의 가장 난해한 사용법이지만 그만큼 유용하다. 

```javascript
function sum(arr,f) {
    // 함수가 전달되지 않았으면 매개변수를 그대로 반환하는 null 함수를 쓴다.
    if(typeof f != 'function') f= x => x;
    return arr.reduce((a,x) => a += f(x));
}
sum([1,2,3]); // 6
sum([1,2,3], x => x*x); // 14
sum([1,2,3], x => Math.pow(x,3)); //36

// function sumOfSquares(arr) {
//     return sum(arr,x => x*x);
// }

function newSummer(f) {
    return arr => sum(arr,f);
}

const sumOfSquares = newSummer(x => x*x);
const sumofCubes = newSummer(x => Math.pow(x,3));
sumOfSquares([1,2,3]); // return 14
sumofCubes([1,2,3]); // return 36
```

위 예제처름 매개변수 여러 개를 받는 함수를 매개변수 하나만 받는 함수로 바꾸는 것을 커링(currying)이라고 부른다.

## 7) 재귀
재귀(recursion)는 자기 자신을 호출하는 함수이다. 같은 일을 반복하면서 그 대상이 점차 줄어드는 상황에서 재귀를 유용하게 활용할 수 있다.

재귀 함수에는 종료 조건이 있어야한다. 종료 조건이 없다면 JS 인터프리에터에서 스택이 너무 깊다고 판단할 때까지 재귀 호출을 계속하다가 프로그램이 멈춘다.