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

