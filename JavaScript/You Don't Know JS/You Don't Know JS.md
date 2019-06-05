# You Don't Know JS

## 1. this

this는 작성 시점이 아닌 런타임 시점에 바인딩 되며 함수 호출 당시 상황에 따라 콘텍스트가 결정된다. 함 수 선언 위치와 상관없이 this 바인딩은 오로지 어떻게  함수를 호출했느냐에 따라 정해진다.

어떤 함수를 호출하면 활성화 레코드 (Activation Record), 즉 실행 콘텍스트 (Execution Context)가 만들어진다. 여기엔 함수가 호출된 근원(Call-Stack)과 호출 방법, 전달된 인자 등의 정보가 담겨있다. this 레퍼런스는 그중 하나로, 함수가 실행되는 동안 이용할 수 있다. 

### 1.2 this 바인딩

#### 1.2.1 기본 바인딩(Default Binding)

가장 평범한 함수 호출인 '단독 함수 실행 (Standalone Function Invocation)'에 관한 규칙으로 나머지 바인딩 규칙에 해당하지 않을 경우 적용되는 this의 기본 규칙이다.

```javascript
function foo() {
    console.log(this.a); // this는 window/global을 가리킨다.
}
let a = 2;
foo(); // 2
```

만약 foo() 함수 안에 `"use strict"`을 사용하게 되면 `TypeError: 'this' is 'undefined'` 오류가 발생한다. 보통 this 바인딩 규칙은 오로지 호출부에 의해 좌우되지만 비엄격 모드에서 foo() 함수의 본문을 실행하면 전역 객체만이 기본 바인딩의 유일한 대상이라는 점이다.

#### 1.2.2 암시적 바인딩(Implicit Binding)

호출부에 콘텍스트 객체가 있는지, 즉 객체의 소유(Owning) / 포함 (Containing) 여부를 확인하는 것이다.

```javascript
function foo() {
    console.log(this.a); // this는 객체 obj2를 가리킨다.
}
let obj2 = {
    a: 42,
    foo: foo
}
let obj1 = {
    a: 2, // 중간단계인 obj1.a는 무시된다.
    obj2: obj2
}
obj1.obj2.foo(); // 42
```

**암시적 소실**

```javascript
function foo() {
    console.log(this.a);
}
let obj = {
    a:2,
    foo: foo
};
let bar = obj.foo; // 기존의 this 바인딩이 사라짐
let a = "웃우";
bar(); // "웃우", 기본 바인딩 적용
```

bar는 obj의 foo를 참조하는 변수처럼 보이지만 실은 foo를 직접 가리키는 또 다른 레퍼런스다. 그러므로 호출시 기본 바인딩이 적용된다.

```javascript
function foo() {
    console.log(this.a);
}
function doFoo(fn){
    // 'fn'은 'foo'의 또 다른 레퍼런스일 뿐이다.
    fn();
}
let obj = {
    a: 2,
    foo: foo
};
let a = "웃우";
doFoo(obj.foo); // "웃우", 기본 바인딩 적용
```

인자로 전달하는 것은 일종의 암시적인 할당이며 예제처럼 함수를 인자로 넘기면 암시적으로 레퍼런스가 할당된다.

```javascript
function foo() {
    console.log(this.a);
}
let obj = {
    a:2,
    foo: foo
};
let a = "웃우";
setTimeout(obj.foo,100); // "웃우", 기본 바인딩 적용
```

내장 함수도 마찬가지로 기본 바인딩이 적용 된다. 이런 콜백 과정에서 this 바인딩의 행방이 묘연해지는 경우가 많다. 콜백 호출 시 this를 개발자가 의도적으로 변경하면 미궁에 더 깊이 빠질 수 있다.

#### 1.2.3 명시적 바인딩(Explicit Binding)

call()과 apply() 메서드를 이용하여 어떤 객체를 this 바인딩에 이용하겠다고 명시할 수 있다.

```javascript
function foo() {
    console.log(this.a);
}
let obj = {
    a: 2
};
foo.call(obj); // 2
```

객체 대신 문자열, 불리언, 숫자와 같은 단순 원시 값을 인자로 전달하면 원시 값에 대응되는 객체 (각각 new String(), new Boolean(), new Number())로 래핑(Wrapping) 된다. 이 과정을 '박싱(Boxing)'이라고 한다.

그러나 앞에서 언급한 this 바인딩이 도중에 소실되거나 프레임워크가 임의로 덮어써 버리는 문제는 해결할 수 없다.

**하드 바인딩**

```javascript
function foo() {
    console.log(this.a);
}
let obj = {
    a: 2
};
let bar = function(){
    foo.call(obj);
};
bar(); // 2
setTimeout(bar,100); // 2

// 하드 바인딩 된 'bar'에서 재정의된 'this'는 의미 없다.
bar.call(obj); // 2
```

함수 bar()는 내부에서 foo.call(obj)로 foo를 호출하면서 obj를 this에 강제로 바인딩하도록 하드 코딩한다. 따라서 bar를 어떻게 호출하든 이 함수는 항상 obj를 바인딩 하며 foo를 실행한다.

또 다른 방법은 bind() 메서드를 이용하여 하드바인딩하는 방법이 있다.

**API 호출 콘텍스트**

많은 라이브러리 함수와 자바스크립트 언어 및 호스트 환경에 내장된 여러 새로운 함수는 대개 '콘텍스트'라 불리는 선택적인 인자를 제공한다. 이는 bind()를 써서 콜백 함수의 this를 지정할 수 없는 경우를 대비한 일종의 예비책이다.

```javascript
function foo(el){
    console.log(el, this.id);
}
let obj = {
    id: "호우"
};

// foo() 호출 시 obj를 this로 사용한다.
[1,2,3].forEach(foo,obj);
// 1 "호우" 
// 2 "호우"
// 3 "호우"
```

#### 2.2.4 new 바인딩

클래스 지향(Class-Oriented)언어의 '생성자(Constructor)'는 클래스에 붙은 특별한 메서드로, 클래스 인스턴스 생성시 new 연산자로 호출된다.

자바스크립트 생성자는 앞에 new 연산자가 있을 때 호출되는 일반 함수에 불과하다. 클래스에 붙은 것도 아니고 클래스 인스턴스화(Instantiation) 기능도 없다. 심지어 특별한 형태의 함소도 아닌 단지 new를 사용하여 호출할 때 자동으로 붙들려 실행되는 그저 평범한 함수다. 이 같은 동작은 결국 '생성자 호출(Constructor Call)'이나 다름없다. '생성자 함수'가 아닌 '함수를 생성하는 호출'이라고 해야 옳다.

함수 앞에 new를 붙여 생성자 호출을 하면 다음과 같은 일들이 저절로 일어난다.

```
1. 새 객체가 툭 만들어진다.
2. 새로 생성된 객체의 [[Prototype]]이 연결된다.
3. 새로 생성된 객체는 해당 함수 호출 시 this로 바인딩 된다.
4. 이 함수가 자신의 또 다른 객체를 반환하지 않는 한 new와 함께 호출된 함수는 자동으로 새로 생성된 객체를 반환한다.
```

```javascript
function foo(a) {
    this.a = a; // foo를 this로 사용
}
let bar = new foo(2);
console.log(bar.a); // 2
```

### 2.3 바인딩 순서

> new 바인딩 > 명시적 바인딩  > 암시적 바인딩 > 기본 바인딩

new 바인딩은 this 하드 바인딩을 무시하는 함수를 생성하기 때문에 우선순위가 높다.

### 2.4 바인딩 예외

기본 바인딩 규칙이 적용되는 예외 사례는 다음과 같다.

#### 2.4.1 this 무시

call, apply, bind 메서드에 첫 번째 인자로 null 또는 undefined를 넘기면 this 바인딩이 무시되고 기본 바인딩 규칙이 적용된다.

```javascript
function foo(){
    console.log(this.a);
}
let a = 2;
foo.call(null); // 2
```

apply()는 함수 호출 시 다수의 인자를 배열 값으로 죽 펼쳐 보내는 용도로 자주 쓰인다. bind()도 유사한 방법으로 인자들(미리 세팅된 값들)을 커링하는 메서드로 많이 사용한다.

```javascript
function foo(a,b){
    console.log("a: "+a+", b: "+b);
}

// 인자들을 배열 형태로 죽 펼친다.
foo.apply(null,[2,3]); // a:2, b:3

// 'bind()'로 커링한다.
let bar = foo.bind(null,2);
bar(3); // a:2, b:3
```

apply와 bind 모두 반드시 첫 번째 인자로 this 바인딩을 지정해야 한다. 하지만 this가 로직상 아무래도 좋다면 null을 넣어도 괜찮다. ES6부터는 펼침 연산자 `'...'` 가 있어서 apply()에 null 넣는 경우는 없어졌다.

그러나 호출 시 null을 전달했는데 마침 그 함수가 내부적으로 this를 레퍼런스로 참조하면 기본 바인딩이 적용되어 전역 변수를 참조하거나 최악으로는 변경하는 예기치 못한 일이 발생할 수 있다. 그래서 null 대신에`Object.create(null)`을 사용하면 이러한 오류 가능성에서 벗어 날 수 있다.

#### 2.4.2 간접 레퍼런스

간접 레퍼런스는 할당문에서 가장 빈번하게 발생하는데 함수를 호출하면 무조건 기본 바인딩 규칙이 적용되어 버린다.

```javascript
function foo() {
    console.log(this.a);
}
let a = 2;
let o = {a:3,foo:foo};
let p = {a:4};
o.foo(); // 3
(p.foo = o.foo)(); // 2
```

할당 표현식 p.foo = o.foo의 결괏값은 원 함수(Underlying Function) 객체의 레퍼런스이므로 실제로 호출부는 처음 예상과는 달리 p.foo(), o.foo()가 아니고 foo()다. 그래서 기본 바인딩 규칙이 적용된다.

#### 2.4.3 소프트 바인딩

하드 바인딩은 함수의 유언성을 크게 떨어뜨리기 때문에 소프트 바인딩(Soft Binding)을 고안했다. 호출 시점에 this를 체크하는 부분에서 주어진 함수를 래핑하여 전역 객체나 undefined일 경우엔 미리 준비한 대체 기본 객체(obj)로 세팅한다. 그 외의 경우 this는 손대지 않는다.

```javascript
function foo() {
    console.log("name: "+this.name);
}
let obj = {name:"obj"},
    obj2 = {name:"obj2"},
    obj3 = {name:"obj3"};
let fooOBJ = foo.softBind(obj);
fooOBJ(); // name: obj
obj2.foo = foo.softBind(obj);
obj2.foo(); // name: obj2
fooOBJ.call(obj3)); // name: obj3
setTimeout(obj2.foo, 10);
// name: obj, 소프트 바인딩 적용
```

### 2.5 어휘적 this

ES6에서 추가된 화살표 함수는 4가지 this 바인딩 규칙 대신 에두른 스코프(Enclosing Scope, 함수 또는 전역)를 보고 this를 알아서 바인딩 한다.

다음은 화살표 함수의 렉시컬 스코프를 나타낸 예제이다.

```javascript
function foo() {
    // 화살표 함수를 반환한다.
    return (a) => {
        // 여기서 'this'는 어휘적으로 'foo()'에서 상속된다.
        console.log(this.a); // this는 obj1을 가리킴
    };
}
let obj1 = {
    a:2
};
let obj2 = {
    a:3
};
let bar = foo.call(obj1);
bar.call(obj2); // 2
```

foo() 내부에서 생성된 화살표 함수는 foo() 호출 당시 this를 무조건 어휘적으로 포착한다. foo()는 obj1에 this가 바인딩 되므로 bar(반환된 화살표 함수를 가리키는 변수)의 this 역시 obj1로 바인딩 된다. 화살표 함수의 어휘적 바인딩은 절대로 오버라이드할 수 없다.

```javascript
function foo() {
    let self = this; // 'this'를 어휘적으로 포착한다.
    setTimeout(function(){
        console.log(self.a);
    },100);
}
let obj = {
    a:2
};
foo.call(obj); // 2
```

`self = this`나 화살표 함수 모두 bind() 대신 사용 가능한 좋은 해결책이지만 this를 제대로 이해하고 수용하기보단 그것에서 도망치려는 꼼수라 할 수 있다.

