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