# Basic JavaScript

## 1) array

앞 쪽 추가 및 제거 : .unshift(), .shift()

뒷 쪽 추가 및 제거 : .push(), .pop()

python 처럼 arr+[i]로 추가되지 않는다.

## 2) Object

```javascript
var myDog = {
  "name": "Happy Coder",
  "legs": 4,
  "tails": 1,
  "friends": ["freeCodeCamp Campers"]
};

// Only change code below this line.
myDog.bark = "bark";
delete myDog.bark;
```

요소 추가



```javascript
let temp = {1:"sdfsd"};
console.log(temp[4]);

// undefined
```

정의되지 않은 것을 검색하면 undefined 출력

## 3) Random

Math.random() : 0부터 1사이의 난수, 1은 포함하지 않음

Math.floor() : 소숫점 버림

Math.floor(Math.random() * (max - min + 1)) + min : 최소, 최대 사이의 난수, 최대 값이 포함됨

## 4) parseInt()

첫 번째 매개변수를 숫자로 이루어진 문자열을 받아 두 번째 매개변수로 해당 문자열이 몇 진수인지 알려주면 십진수로 바꿔주는 함수이다.

```javascript
function convertToInteger(str) {
  return parseInt(str,2);
}

console.log(convertToInteger("10011"));
// 19
```

