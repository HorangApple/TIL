```bash
$ npm i -d @babel/cli @babel/core @babel/preset-react babel-loader webpack webpack-cli
```

`@babel/preset-react`는 presets를 다음과 같이 설정한다.

```json
{
  //...
  "scripts": {
	//...
    "build": "./node_modules/.bin/webpack -w",
    "i": "rm -rf ./node_modules && npm cache clean && npm install"
  },
  //...
  "babel": {
    "presets": [
      "@babel/preset-react"
    ]
  },
  //...
}
```

