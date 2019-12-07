# Webpack

## 1. Webpack이란?
- 서로 연관 관계가 있는 웹 자원(.js,.css 등)을 .js, css, img 와 같은 최적화된 정적 자원으로 변환, 즉 번들링하는 모듈 번들러
- minification 과 같은 압축기법을 수행하여 최적화함

## 2. 왜 사용할까?
### 1) 새로운 형태의 Web Task Manager
- 기존 Gulp, Grunt와 같은 자동화 도구, 즉 Web Task Manager의 기능에 모듈 의존성 관리가 추가된 통합 도구

### 2) JS Code based Modules 관리
- JS 모듈 로더들을 통합해서 사용하며 모듈 간의 관계를 chunk 단위로 나누게 만들어줌
- 현대의 웹에서 JS 역할이 커짐에 따라, Client Side 에 들어가는 코드량이 많아지고 복잡해져 이를 쉽게 관리할 필요성이 생김
- 가독성이나 다수 모듈 미병행 처리 등의 약점을 보완해줌

*cf) JS 모듈화 문제*
- HTML 에서 여러 JS 파일을 로드했을 때 전역변수 충돌, 스크립트 로딩 순서, 복잡도에 따른 관리상의 문제가 발생함
- AMD 및 기타 모듈 로더들, Webpack 이 등장하게 된 계기가 됨

## 3. Webpack의 철학
### 1) Everything is Module
모든 웹 자원 (js, css, html)이 모듈 형태로 로딩 가능 (loader 사용))

### 2) Load only "what" you need and "when" you need
초기에 불필요한 것들을 모두 로딩하지 않고, 필요할 때 필요한 것만 로딩하여 사용 (lazy loading 지원)

## 4. 실습
### 1) 설치

```bash
$npm i -g webpack
```

### 2) 설정 파일
프로젝트의 상위 디렉터리에 `webpack.config.js`를 아래와 같이 생성하면 cli에 `webpack app/index.js dist/bundle.js`에서 `webpack`만 입력해도 알아서 작업하게끔 만들어준다.

*webpack.config.js*
```javascript
// `webpack` command will pick up this config setup by default
var path = require('path');

module.exports = {
  entry: './app/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  }
};
```

`bundle.js`를 살펴보면 `index.js`와 그 안에서 사용된 `lodash`와 같은 라이브러리가 번들링되어 minifiy 된 것을 볼 수 있다.

## 5. npm (Node Package Manager)
- JS 개발자들이 편하게 개발할 수 있도록 JS 라이브러리들을 모아놓은 열린 공간으로 재사용 가능한 code 단위를 module, package 라고 부름
- package.json : 해당 package 에 대한 파일 정보가 들어가 있음

## 6. Webpack 주요 속성
### 1) Entry
- webpack 으로 묶는 모든 라이브러리들을 로딩할 시점을 설정

```javascript
var config = {
  // 1. 간단한 entry 설정
  entry: './path/to/my/entry/file.js',
  // 2. 앱 로직용, 외부 라이브러리용
  entry: {
    app: './src/app.js',
    vendors: './src/vendors.js'
  },
  // 3. 페이지당 불러오는 JS 설정
  entry: {
    pageOne: './src/pageOne/index.js'
    pageTwo: './src/pageTwo/index.js'
    pageThree: './src/pageThree/index.js'
  }
}
```

### 2) Output
- entry 에서 설정하고 묶은 파일의 결과값을 설정

```javascript
var path = require('path');
module.exports = {
  entry: {
    // ...
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
    
  }
};
```

- output의 Name Options는 다음과 같다.

```javascript
output: {
  filename: '[name].js', // entry 이름에 따른 파일명 생성
  filename: '[hash].js', // 특정 webpack build에 따른 파일명 생성
  filename: '[chunkhash].js', // 특정 webpack chunk에 따른 파일명 생성 (추천)
}
```

#### 참고) [path](https://nodejs.org/api/path.html)
**path.join([...paths])**
- 해당 API 가 동작되는 OS 의 파일 구분자를 이용하여 파일 위치를 조합한다.

**path.resolve([...paths])**
- join()의 경우 그냥 문자열을 합치지만, resolve 는 오른쪽에서 왼쪽으로 파일 위치를 구성해가며 유효한 위치를 찾는다.

- 만약 결과 값이 유효하지 않으면 현재 디렉토리가 사용된다. 반환되는 위치 값은 항상 절대경로이다.

### 3) Loader
- 웹팩은 JS 파일만 처리가 가능하도록 되어 있기 때문에 다른 형태의 웹 자원들(img, css 등)을 js 로 변환하여 로딩

- 상세한 설정은 [공식 문서](https://webpack.js.org/concepts/loaders/)를 확인해보자.

```javascript
module.exports = {
  entry: {
    // ...
  },
  output: {
    // ...
  },
  module: {
    rules: [
      // 모듈 로딩 순서는 배열의 요소 오른쪽에서 왼쪽으로 진행된다.
      { test: /\.css$/, use: ['style-loader', 'css-loader'] }
    ]
  }
};
```

### 4) Plugins
- 플러그인은 파일별 커스텀 기능을 사용하기 위해서 사용한다.
- [플러그인의 종류](https://webpack.js.org/plugins/)

```javascript
module.exports = {
  entry: {},
  output: {},
  module: {},
  plugins: [
    new webpack.optimize.UglifyJsPlugin()
    // ...
  ]
};
```