# python 기초 문법


## 1. 식별자

파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름이다.

- 식별자의 이름은 영문알파벳, _, 숫자로 구성된다.
- 첫 글자에 숫자가 올 수 없다.
- 대소문자를 구별한다.
- 아래의 예약어는 사용할 수 없다. (`keyword`를 통해 확인 가능)

<img src="images/image 004.png">

- 내장함수나 모듈 등의 이름으로도 만들면 안된다.

- 실행이 되어도 해당 명의의 내장함수가 사용이 불가할 수도 있다.

- 만약 내장함수나 모듈 등의 이름으로 만들었다면 `del`을 이용해 해당 식별자를 삭제하면 제대로 작동이 된다.
<img src = "images/image 011.png">
<img src = "images/image 010.png">
  위와 같이 `del`로 지우고 나서 사용하면 된다.

## 2. 인코딩 선언

인코딩은 선언하지 않더라도 `UTF-8`로 기본 설정이 되어 있다.

만약, 인코딩을 설정하려면 코드 상단에 아래와 같이 선언한다. 주석으로 보이지만, Python `parser`에 의해 읽혀진다.

```python
# -*- coding: <encoding-name> -*- 
# -*- coding: utf-8 -*-
```

## 3. 주석(Comment)

- 주석은 `#`으로 표현한다.

- `docstring`은 `"""`으로 표현한다.

  : 여러 줄의 주석을 작성할 수 있으며, 보통 함수/클래스 선언 다음에 해당하는 설명을 위해 활용한다.

  `함수명.__doc__`를 입력하면 주석의 내용이 출력된다.

- `"""`다음에 바로 적어야 줄바꿈이 일어나지 않고 사용한다. 끝도 마찬가지로 `"""`를 문자열 끝에 바로 붙여적으면 줄바꿈이 일어나지 않는다.

## 4. 코드 라인

- 기본적으로 파이썬에서는 `;` 을 작성하지 않는다.
- 한 줄로 표기할 떄는 `;`를 작성하여 표기할 수 있다.
- 줄을 여러줄 작성할 때는 역슬래시`\`를 사용하여 아래와 같이 할 수 있다.
  - 그러나 되도록이면 한 줄 안으로 끝내는 것이 가독성에 좋다.
  - `[]` `{}` `()`는 `\` 없이도 가능하다.

<img src="images/image 007.png">

## 5. 변수(variable) 및 자료형

- 변수는 `=`을 통해 할당(assignment) 된다.

- 해당 자료형을 확인하기 위해서는 `type()`을 활용한다.

- 해당 변수의 메모리 주소를 확인하기 위해서는 `id()`를 활용한다.

- http://pythontutor.com 를 통해 시각화로 변수가 어떻게 할당하고 돌아가는지 볼 수 있다.

- 같은 값을 동시에 할당할 수 있다.
<img src="images/image 013.png">

- 다른 값을 동시에 할당 가능하다.
<img src="images/image 014.png">

- 입력은 `input` 함수를 쓰고 괄호 안에 입력받기 전에 출력하고 싶은 문자를 적을 수도 있다.
  - `input`함수의 리턴 값은 문자형이기 때문에 `int()`로 형변환을 해서 사용해야한다.



### 수치형(Numbers)

#### `int` (정수)¶
모든 정수는 `int`로 표현된다.
파이썬 3.x 버전에서는 `long` 타입은 없고 모두 `int` 형으로 표기 된다.
10진수가 아닌 8진수 : `0o`/ 2진수 : `0b` / 16진수: `0x`로도 표현 가능하다.

<img src="images/image 015.png">

#### `float`(부동소수점, 실수)

실수는 `float`로 표현된다.

다만, 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않는다. (floating point rounding error)

이는 컴퓨터가 2진수(비트)를 통해 숫자를 표현하는 과정에서 생기는 오류이며, 대부분의 경우는 중요하지 않으나 값을 같은지 비교하는 과정에서 문제가 발생할 수 있다.

<img src="images/image 008.png">

반올림을 하고 싶으면 `round(실수, 몇 자리 수 까지)`를 사용하면 된다.

<img src="images/image 016.png">

위와 같이 부동소수점 연산때문에 예상한 결과와 다르게 `false`로 나오는데 아래와 같은 방법으로 해결할 수 있다.

<img src="images/image 017.png">



#### `complex` (복소수)

복소수는 허수부를 `j`로 표현한다.

<img src="images/image 018.png">

#### `Bool`

파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있다.

비교/논리 연산을 수행 등에서 활용된다.

다음은 `False`로 변환됩니다.

```
0, 0.0, (), [], {}, '', None
```

#### `None`

파이썬에서는 값이 없음을 표현하기 위해 `None`타입이 존재합니다.



### 문자형(String)

#### 기본 활용법

문자열은 Single quotes(`'`)나 Double quotes(`"`)을 활용하여 표현 가능하다.

단, 문자열을 묶을 때 동일한 문장부호를 활용해야하며, `PEP-8`에서는 **하나의 문장부호를 선택**하여 유지하도록 하고 있습니다. (Pick a rule and Stick to it)

- 다만 문자열 안에 문장부호(`'`, `"`)가 활용될 경우 이스케이프 문자(`\`)를 사용하는 것 대신 활용 가능 합니다.

- 여러줄에 걸쳐있는 문장은 다음과 같이 표현 가능합니다.
`PEP-8`에 따르면 이 경우에는 반드시 `"""`를 사용하도록 되어 있습니다.


#### 이스케이프 문자열

문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 활용하여 이를 구분한다.

| 예약문자 | 내용(의미)      |
| -------- | --------------- |
| \n       | 줄바꿈          |
| \t       | 탭              |
| \r       | 캐리지리턴      |
| \0       | 널(Null)        |
| `\\`     | `\`             |
| '        | 단일인용부호(') |
| "        | 이중인용부호(") |

#### String interpolation

1) `%-formatting`

2) [`str.format()`](https://pyformat.info/)

3) [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 버전 이후에 지원 되는 사항입니다.

본 슬라이드에서는 `f-strings`의 기본적인 활용법만 알려드리고 나머지 `.format()`는 해당 [링크](https://pyformat.info/)에서 확인바랍니다.

<img src="images/image 019.png">

<img src="images/image 020.png">

위에서 `{today:%Y}`로 작성하면 yyyy표기로 나오는 것과 같이 대소문자에 따라 표기가 다르다.

### 연산자

#### 산술 연산자

Python에서는 기본적인 사칙연산이 가능합니다.

| 연산자 | 내용           |
| ------ | -------------- |
| +      | 덧셈           |
| -      | 뺄셈           |
| *      | 곱셈           |
| /      | 나눗셈         |
| //     | 몫             |
| %      | 나머지(modulo) |
| **     | 거듭제곱       |

- `divmod`는 나눗셈과 관련된 함수이며 `(몫, 나머지)`로 반환된다.

#### 비교 연산자

우리가 수학에서 배운 연산자와 동일하게 값을 비교할 수 있습니다.

| 연산자 | 내용     |
| ------ | -------- |
| a > b  | 초과     |
| a < b  | 미만     |
| a >= b | 이상     |
| a <= b | 이하     |
| a == b | 같음     |
| a != b | 같지않음 |

#### 논리 연산자

| 연산자  | 내용                         |
| ------- | ---------------------------- |
| a and b | a와 b 모두 True시만 True     |
| a or b  | a 와 b 모두 False시만 False  |
| not a   | True -> False, False -> True |

우리가 보통 알고 있는 `&` `|`은 파이썬에서 비트 연산자이다.

- 단축평가
`a and b`를 예시를 들면 `a`가  `False`인지 확인하고 `False`면 b에 대해 살펴보지 않고 바로 결과를 내는 것을 단축평가 (short-circult evaluation)이라고 한다.

#### 복합 연산자

복합 연산자는 연산과 대입이 함께 이뤄진다.

가장 많이 활용되는 경우는 반복문을 통해서 갯수를 카운트하거나 할 때 활용된다.

| 연산자  | 내용       |
| ------- | ---------- |
| a += b  | a = a + b  |
| a -= b  | a = a - b  |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a // b |
| a %= b  | a = a % b  |
| a **= b | a = a ** b |

#### 기타 연산자

##### Concatenation

숫자가 아닌 자료형은 `+` 연산자를 통해 합칠 수 있다.

##### Containment Test

`in` 연산자를 통해 속해있는지 여부를 확인할 수 있다.

##### Identity

`is` 연산자를 통해 동일한 object (id)인지 확인할 수 있다.

(나중에 Class를 배우고 다시 학습)

##### Indexing/Slicing

`[]`를 통한 값 접근 및 `[:]`을 통한 슬라이싱

#### 연산자 우선순위

1. `()`을 통한 grouping
2. Slicing
3. Indexing
4. 제곱연산자 **
5. 단항연산자 +, - (음수/양수 부호)
6. 산술연산자 *, /, %
7. 산술연산자 +, -
8. 비교연산자, `in`, `is`
9. `not`
10. `and`
11. `or`

### 기초 형변환(Type conversion, Typecasting)

파이썬에서 데이터타입은 서로 변환할 수 있다.

### 암시적 형변환(Implicit Type Conversion)

사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우이다. 아래의 상황에서만 가능하다.

- bool
- Numbers (int, float, complex)

<img src="images/image 021.png">



### 시퀀스(sequence) 자료형

`시퀀스`는 데이터의 순서대로 나열된 형식을 나타낸다.

**주의! 순서대로 나열된 것이 정렬되었다라는 뜻은 아니다.**

파이썬에서 기본적인 시퀀스 타입은 다음과 같다.

1. 리스트(list)
2. 튜플(tuple)
3. 레인지(range)
4. 문자열(string)
5. 바이너리(binary) : 따로 다루지는 않습니다.

#### `list`

**활용법**

```python
[value1, value2, value3]
```

리스트는 대괄호`[]` 를 통해 만들 수 있습니다.

값에 대한 접근은 `list[i]`를 통해 합니다.

#### `tuple`

**활용법**

```python
(value1, value2)
```

튜플은 리스트와 유사하지만, `()`로 묶어서 표현합니다.

그리고 tuple은 수정 불가능(immutable)하고, 읽을 수 밖에 없습니다.

직접 사용하는 것보다는 파이썬 내부에서 사용하고 있습니다.

#### `range()`

레인지는 숫자의 시퀀스를 나타내기 위해 사용됩니다.

기본형 : `range(n)`

> 0부터 n-1까지 값을 가짐

범위 지정 : `range(n, m)`

> n부터 m-1까지 값을 가짐

범위 및 스텝 지정 : `range(n, m, s)`

> n부터 m-1까지 +s만큼 증가한다

#### 시퀀스에서 활용할 수 있는 연산자/함수

| operation  | 설명                    |
| ---------- | ----------------------- |
| x in s     | containment test        |
| x not in s | containment test        |
| s1 + s2    | concatenation           |
| s * n      | n번만큼 반복하여 더하기 |
| s[i]       | indexing                |
| s[i:j]     | slicing                 |
| s[i:j:k]   | k간격으로 slicing       |
| len(s)     | 길이                    |
| min(s)     | 최솟값                  |
| max(s)     | 최댓값                  |
| s.count(x) | x의 갯수                |

### set, dictionary

- `set`과 `dictionary`는 기본적으로 순서가 없습니다.



#### `set`

세트는 수학에서의 집합과 동일하게 처리됩니다.

세트는 중괄호`{}`를 통해 만들며, 순서가 없고 중복된 값이 없습니다.

**활용법**

```python
{value1, value2, value3}
```

| 연산자/함수       | 설명   |
| ----------------- | ------ |
| a - b             | 차집합 |
| a \| b            | 합집합 |
| a & b             | 교집합 |
| a.intersection(b) | 차집합 |
| a.union(b)        | 합집합 |
| a.intersection(b) | 교집합 |

- `set`을 활용하면 `list`의 중복된 값을 손쉽게 제거할 수 있습니다.


#### `dictionary`

**활용법**

```python
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```

- 딕셔너리는 `key`와 `value`가 쌍으로 이뤄져있으며, 궁극의 자료구조입니다.
- `{}`를 통해 만들며, `dict()`로 만들 수도 있습니다.
- `key`는 immutable한 모든 것이 가능하다. (불변값 : string, integer, float, boolean, tuple, range)
- `value`는 `list`, `dictionary`를 포함한 모든 것이 가능하다.
- 관련함수로 `keys`,`values` 등이 있다.



## 6. 입출력

## 입력
### 1) `input()` 

- 입력을 받는 함수
- sys에 비하면 속도가 느리다.

*1000_A+B.py*

```python
# 풀이1
a,b = [int(x) for x in input().split()]
print(a+b)
```


### 2) `import sys ` 

- 라이브러리 sys를 사용하여 직접 시스템 영역에 접근하는 방법이다.
- 시스템의 입력 쪽을 받는 방법으로 input 함수에 비해 빠르다.

*11718_그대로출력하기.py*

```python
import sys
for i in sys.stdin :
    print(i, end="")
```
## 출력
### 1) `print ()`

- 괄호 안의 내용을 출력하는 함수
- `print`함수를 이여서 한 줄로 사용하고 싶으면 `;`를 붙여서 사용하면 된다.
<img src="images/image 012.png">
- 괄호 안의 내용이 길면 역슬래쉬(`\`)를 입력하고 줄 바꿈하여 계속 사용할 수 있다.



## 조건 표현식(Conditional Expression)

**활용법**

```
true_value if <조건식> else false_value
```

와 같이 표현식을 작성할 수 있다. 이는 보통 다른 언어에서 활용되는 삼항연산자와 동일하다.

<img src = "images/image 022.png">

- enumerate()는 파이썬 표준 라이브러리의 내장함수 중 하나이며, 다음과 같이 구성되어 있다.

<img src = "images/image 023.png">

### `else`

`else`문은 끝까지 반복문을 시행한 이후에 실행됩니다.

(`break`를 통해 중간에 종료되지 않은 경우만 실행)

<img src = "images/image 024.png"><img src = "images/image 025.png">

## 함수(function) 기초

### 개요

**활용법**

```python
def func(parameter1, parameter2):
    code line1
    code line2
    return value
```

- 함수 선언은 `def`로 시작하여 `:`으로 끝나고, 다음은 `4spaces 들여쓰기`로 코드 블록을 만듭니다.
- 함수는 `매개변수(parameter)`를 넘겨줄 수도 있습니다.
- 함수는 동작후에 `return`을 통해 결과값을 전달 할 수도 있습니다. (`return` 값이 없으면, None을 반환합니다.)
- 함수는 호출을 `func(val1, val2)`와 같이 합니다.

### 함수의 return

앞서 설명한 것과 마찬가지로 함수는 반환되는 값이 있으며, 이는 어떠한 종류의 객체여도 상관없습니다.

단, 오직 한 개의 객체만 반환됩니다.

함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.

### 함수의 인자/인수

함수는 `인자(parameter)`를 받을 수 있습니다.

### 위치 인수

함수는 기본적으로 인수를 위치로 판단합니다.

### 기본 값(Default Argument Values)[¶](http://localhost:8890/notebooks/lesson2/03_Control_of_flow_function.ipynb#%EA%B8%B0%EB%B3%B8-%EA%B0%92(Default-Argument-Values))

함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있습니다.

**활용법**

```python
def func(p1=v1):
    return p1
```

- 호출시 인자가 없으면 기본 인자 값이 활용됩니다.

- 단, 기본 값이 있는 매개변수 이후에 기본 값이 없는 매개변수를 사용할 수는 없습니다.

### 키워드 인자(Keyword Arguments)

키워드 인자는 직접적으로 변수의 이름으로 특정 인자를 전달할 수 있습니다.

- 단, 키워드 인자를 활용한 뒤에 위치 인자를 활용할 수는 없습니다.

<img src = "images/image 026.png">

<img src = "images/image 027.png">

### 가변 인자 리스트

앞서 설명한 `print()`처럼 정해지지 않은 임의의 숫자의 인자를 받기 위해서는 가변인자를 활용합니다.

가변인자는 `tuple` 형태로 처리가 되며, `*`로 표현합니다.

**활용법**

```python
def func(*args):
```



### 정의되지 않은 인자들 처리하기

정의되지 않은 인자들은 `dict` 형태로 처리가 되며, `**`로 표현합니다.

주로 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있습니다.

**활용법**

```python
def func(**kwargs):
```



우리가 dictionary를 만들 때 사용할 수 있는 `dict()` 함수는 [파이썬 표준 라이브러리의 내장함수](https://docs.python.org/ko/3.6/library/functions.html)중 하나이며, 다음과 같이 구성되어 있다. 

<img src = "images/image 028.png">

<img src = "images/image 029.png">

### 이름공간 및 스코프(Scope)

파이썬에서 사용되는 이름들은 이름공간(namespce)에 저장되어 있습니다. 그리고, LEGB Rule을 가지고 있습니다.

변수에서 값을 찾을 때 아래와 같은 순서대로 이름을 찾아나갑니다.

- `L`ocal scope: 정의된 함수
- `E`nclosed scope: 상위 함수
- `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
- `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

- `str()` 코드가 실행되면
- str을 Global scope에서 먼저 찾아서 `str = 4`를 가져오고,
- 이는 함수가 아니라 변수이기 때문에 `not callable`하다라는 오류를 내뱉게 됩니다.
- 우리가 원하는 `str()`은 Built-in scope에 있기 때문입니다.

## 7. 각종 함수

## 문자열 메소드 활용하기

## 변형

### `.capitalize()`, `title()`, `.upper()`

`.capitalize()` : 앞글자를 대문자로 만들어 반환합니다.

`.title()` : 어포스트로피나 공백을 이후를 대문자로 만들어 반환합니다.

`.upper()` : 모두 대문자로 만들어 반환합니다.

### `lower()`, `swapcase()`

`lower()` : 모두 소문자로 만들어 반환합니다.

`swapcase()` : 대<->소문자로 변경하여 반환합니다

### `.join(iterable)`

특정한 문자열로 만들어 반환합니다.

### `.replace(old, new[, count])`

바꿀 대상 글자를 새로운 글자로 바꿔서 반환합니다.

count를 지정하면 해당 갯수만큼만 시행합니다.

### 글씨 제거 (`.strip([chars])`)

특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip) 오른쪽을 제거합니다(rstrip)

지정하지 않으면 공백을 제거합니다.

### `.split()`

문자열을 특정한 단위로 나누어 리스트로 반환합니다.

## 탐색 및 검증

### `.find(x)` : x의 첫 번째 위치를 반환합니다. 없으면, -1을 반환합니다.

### `.index(x)` : x의 첫번째 위치를 반환합니다. 없으면, 오류가 뜹니다.

### 다양한 확인 메소드 : 참/거짓 반환

```
.isaplha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .issuper(), .istitle(), .islower()
```

# 리스트 메소드 활용하기

## 값 추가 및 삭제

### `.append(x)`

리스트에 값을 추가할 수 있습니다.

### `.extend(iterable)`

리스트에 iterable(list, range, tuple, string*유의*) 값을 붙일 수가 있습니다.

### `.insert(i, x)`

정해진 위치 `i`에 값을 추가합니다.

### `.remove(x)`

리스트에서 값이 x인 것을 삭제합니다.

### `.pop(i)`

정해진 위치 `i`에 있는 값을 삭제하며, 그 항목을 반환합니다.

`i`가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줍니다.

## 탐색 및 정렬

### `.index(x)`

원하는 값을 찾아 index 값을 반환합니다.

### `.count(x)`

원하는 값의 갯수를 확인할 수 있습니다.

### `.sort()`

정렬을 합니다.

sorted()와는 다르게 원본 list를 변형시키고, None을 리턴합니다.

### `reverse()`

반대로 뒤집습니다. (정렬 아님)

## 복사

- 파이썬에서 모든 변수는 객체의 주소를 가지고 있을 뿐입니다.

```
num = [1, 2, 3]
```

- 위와 같이 변수를 생성하면 hong이라는 객체를 생성하고, 변수에는 객체의 주소가 저장됩니다.

- 변경가능한(mutable) 자료형과 변경불가능한(immutable) 자료형은 서로 다르게 동작합니다.

```python
# 복사 예시
import copy
c = {'a':1,'b':2}
copy_c = copy.deepcopy(c)
print(id(c))
print(id(copy_c))
c['c'] = 3
print(c)
print(copy_c)
```
- 따라서, 복사를 하고 싶을 때에는 위와  같이 `copy`모듈을 이용해야한다.

```python
# 복사 예시2
a = [1,2,[1,2]]
b = a[:]
b[1] = 3
print(a)
print(b)
b[2][0] = 3
print(a)
print(b)
```

- 하지만, 이렇게 하는 것도 일부 상황에만 서로 다른 얕은 복사(shallow copy)입니다.
- 만일 중첩된 상황에서 복사를 하고 싶다면, 깊은 복사(deep copy)를 해야합니다.
- 즉, 내부에 있는 모든 객체까지 새롭게 값이 변경됩니다.

## 삭제 `clear()`

리스트의 모든 항목을 삭제합니다.



# List Comprehension

List를 만들 수 있는 간단한 방법이 있습니다.

## 활용법

여러개의 `for` 혹은 `if`문을 중첩적으로 사용 가능합니다.

### 짝짓기 - 곱집합

> 주어진 두 list의 가능한 모든 조합을 담은 `pair` 리스트를 만들어주세요.

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']

pair = []
for i in girls:
    for j in boys:
        pair.append((i,j))
print(pair)

pair = [(x,y)for x in girls for y in boys]
print(pair)
```

### 피타고라스 정리

> 주어진 조건(x < y < z < 50) 내에서 피타고라스 방정식의 해를 찾아보세요.

```python
result = []
for x in range(1,50) :
    for y in range(1,50) :
        for z in range(1,50) :
            if x**2+y**2 == z**2 :
                result.append((x,y,z))
print(result)

result = [(x, y, z) for x in range(1,50) for y in range(1,50) for z in range(1,50) if x**2+y**2 == z**2 ]

print(result)
```

### 모음 제거하기

> 다음의 문장에서 모음(a, e, i, o, u)를 모두 제거하시오.

```python
words = 'Life is too short, you need python!'
vowel = 'aeiou'
result = [x for x in words if x not in vowel]
print("".join(result))
```



# 딕셔너리 메소드 활용

## 추가 및 삭제

### `.pop(key[, default])`

key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다.

default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생합니다.

### `.update()`

값을 제공하는 key, value로 덮어씁니다.

### `.get(key[, default])`

key를 통해 value를 가져옵니다.

절대로 KeyError가 발생하지 않습니다. default는 기본적으로 None입니다.



## dictionary comprehension

dictionary도 comprehension을 활용하여 만들 수 있습니다.

- 추후에 zip, map 등을 배우고 다시 다루도록 하겠습니다 :)



# 세트 메소드 활용

## 추가 및 삭제

### `.add(elem)`

elem을 세트에 추가합니다.

### `update(*others)`

여러가지의 값을 순차적으로 추가합니다.

여기서 반드시 iterable한 값을 넣어야합니다.

### `.remove(elem)`

elem을 세트에서 삭제하고, 없으면 KeyError가 발생합니다.

### `discard(elem)`

x를 세트에서 삭제하고 없어도 에러가 발생하지 않습니다.

### `pop()`

임의의 원소를 제거해 반환합니다. set은 내부적으로 정렬이 되어있지 않기 때문에 pop이 되는 대상은 정확히 무엇인지 예측하기 힘들다.

# 딕셔너리 메소드 활용

## 추가 및 삭제

### `.pop(key[, default])`

key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다.

default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생합니다.



### `.update()`

값을 제공하는 key, value로 덮어씁니다.



### `.get(key[, default])`

key를 통해 value를 가져옵니다.

절대로 KeyError가 발생하지 않습니다. default는 기본적으로 None입니다.



## dictionary comprehension

dictionary도 comprehension을 활용하여 만들 수 있습니다.

```python
# 숫자와 세제곱의 결과로 이뤄진 딕셔너리를 만들어봅시다.
cubic_list = [x**3 for x in range(1,11)]
print(cubic_list)

cubic_d = {x:x**3 for x in range(1,11)}
print(cubic_d)
```

```python
# 다음의 딕셔너리에서 미세먼지 농도가 80초과는 나쁨 80이하는 보통으로 하는 value를 가지도록 바꿔봅시다.
# 예) {'서울': '나쁨', '경기': '보통', '대전': '나쁨', '부산': '보통'}
dusts = {'서울': 72, '경기': 82, '대전': 29, '중국': 200}
dics = {key : '매우나쁨' if value>150 else '나쁨' if value>80 else '보통' for key, value in dusts.items()}
print(dics)
```

## 정리! `map()`, `zip()`, `filter()`

### `map(function, iterable)`

- Iterable의 모든 원소에 function을 적용한 후 그 결과를 돌려줍니다.
- 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range
- return은 map_object 형태로 됩니다.

### `zip(*iterables)`

- 복수 iterable한 것들을 모아준다.
- 결과는 튜플의 모음으로 구성된 zip object를 반환한다.
- zip은 반드시 길이가 같을 때 사용해야한다. 가장 짧은 것을 기준으로 구성한다.

- 물론 `zip_longest`를 이용해 길이가 긴 것을 맞춰서 할 수도 있지만, 기억 저 멀리 넣어놓자.

### `filter(function, iterable)`

- iterable에서 function의 반환된 결과가 참인 것들만 구성하여 반환한다.