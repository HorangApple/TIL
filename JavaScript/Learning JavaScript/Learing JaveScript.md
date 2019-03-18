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

리터럴(literal)은 직접 값을 만들어 식별자에 사용한다. 즉, 값을 만드는 방법이라 할 수 있다. 숫자형 리터럴과 문자열 리터럴이 있다.