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
  - 문자열 병합에서 자동으로 순자를 문자열로 변환하므로, 숫자를 문자열로 바꿀일이 많이 없음
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

