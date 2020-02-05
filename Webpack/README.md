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

**ProvidePlugins**
- 모든 모듈에서 사용할 수 있도록 해당 모듈을 변수로 변환한다.

```javascript
// jquery를 $로 전역변수화 (라이브러리의 전역변수화)
new webpack.ProvidePlugin({
  $: "jquery"
})
```

**DefinePlugin**
- Webpack 번들링을 시작하는 시점에 사용 가능한 상수들을 정의한다.
- 일반적으로 개발계 & 테스트계에 따라 다른 설정을 적용할 때 유용하다.

```javascript
new webpack.DefinePlugin({
  PRODUCTION: JSON.stringify(true),
  VERSION: JSON.stringify("5fa3b9"),
  BROWSER_SUPPORTS_HTML5: true,
  TWO: "1+1",
  "typeof window": JSON.stringify("object")
})
```

**ManifestPlugin**
- 번들링시 생성되는 코드 (라이브러리)에 대한 정보를 json 파일로 저장하여 관리

```javascript
new ManifestPlugin({
  fileName: 'manifest.json',
  basePath: './dist/'
})
```

## 7. Webpack Resolve
- Webpack 의 모듈 번들링 관점에서 봤을 때, 모듈 간의 의존성을 고려하여 모듈을 로딩해야 한다.
- 따라서, 모듈을 **어떤 위치에서 어떻게 로딩할지**에 관해 정의를 하는 것이 바로 Module Resolution

**절대경로를 이용한 로딩**
- 파일의 경로를 모두 입력해준다.

**상대경로를 이용한 로딩**
- 해당 모듈이 로딩되는 시점의 위치에 기반하여, 상대 경로를 절대 경로로 인식하여 로딩한다.

### 1) Resolve Option
config 파일에 `resolve` 를 추가하여 모듈 로딩에 관련된 옵션 사용

**alias**
- 특정 모듈을 로딩할 때 별칭으로 더 쉽게 로딩이 가능하다.

```javascript
alias: {
  Utilities: path.resolve(__dirname, 'src/path/utilities/')
}

// alias 미사용시
import Utility from '../../src/path/utilities/utility';

// alias 사용시
import Utility from 'Utilities/utility';
```

**modules**
- `require()`, `import ''` 등의 모듈 로딩시에 어느 폴더를 기준할 것인지 정하는 옵션

```javascript
modules: ["node_modules"] // default
modules: [path.resolve(__dirname, "src"), "node_modules"] // src/node_modules
```

## 8. Webpack 빌드를 위한 서버 구성

- 페이지 자동고침을 제공하는 Webpack 개발용 node.js 서버
- `webpack-dev-server` : Webpack 자체에서 제공하는 개발 서버이고 빠른 리로딩 기능 제공 (개인 프로젝트에서 사용)
- `webpack-dev-middleware` : 서버가 이미 구성된 경우에는 webpack 을 미들웨어로 구성하여 서비스와 연결

**설치 및 실행**
- 설치
```bash
npm install --save-dev webpack-dev-server
```

- 실행
```bash
webpack-dev-server --open
```

- 또는 package.json 에 명령어 등록
```json
"scripts": { "start": "webpack-dev-server"}
```

추가 옵션 [참고](https://webpack.js.org/configuration/dev-server/)

**Options**
- `publicPath` : Webpack 으로 번들한 파일들이 위치하는 곳. default 값은 `/`
```json
// 항상 `/` 를 앞뒤에 붙여야 한다.
publicPath: "/assets/"
```

- `contentBase` : 서버가 로딩할 static 파일 경로를 지정. default 값은 `working directory`
```json
// 절대 경로를 사용할 것
contentBase: path.join(__dirname, "public")
// 비활성화
contentBase: false
```

- `compress` : gzip 압축 방식을 이용하여 웹 자원의 사이즈를 줄인다.
```json
compress: true
```