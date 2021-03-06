파이썬 기본 문법 익히기

- 01장 파이썬 프로그래밍의 기초, 자료형
  - 00 기초문법
    - 인코딩 선언
      - 인코딩은 선언하지 않더라도 UTF-8로 기본 설정
      - \# -*- coding: <encoding-name> -*-  로 별도 선언, 파이썬 parser에 의해 읽힘
    - 주석(Comment)
      - \#
      - """ : docstring
    - 코드 여러줄 작성
      - 역슬래시( \ ) 사용
      - 리스트, 딕셔너리, 튜플, 집합에서는 \ 없이도 사용 가능
    - 연산자 우선순위
      1) ()을 통한 grouping
      2) Slicing
      3) Indexing
      4) 제곱연산자 **
      5) 단항연산자 +, - (음수/양수 부호)
      6) 산술연산자 *, /, %
      7) 산술연산자 +, -
      8) 비교연산자 in, is, <, >, ==, <=, >=
      9) not
      10) and
      11) or
    - 형변환(Type conversion, Typecasting)
      - 암시적 형변환(Implicit Type Conversion)
        - 파이썬 내부적으로 자동으로 형변환
        - bool, numbers (int, float, complex)
      - 명시적 형변환(Explicit Type Conversion)
        - int(), float(), str(), list(), tuple() 등을 사용하여 형변환
  - 01 숫자형
    - 종류
      - 정수형
      - 실수형
        - 표현 방식으로 부동소수점 사용
        - floating point rounding error
          -  2진수(비트)를 통해 표현하기 때문에 발생하는 오류로 항상 같은 값으로 일치하지 않는다.
      - 복소수형
        - .imag : 허수만
        - .real : 실수만
        - .conjugate() : 켤레복소수
      - 2진수, 8진수, 16진수 : 0b / 0o / 0x
    - 연산자
      - 사칙연산
      - 제곱 : **
      - 나눗셈 나머지 : %
      - 나눗셈 몫 : //
        - 4와 5에 //를 계산하면 2로 같이 나오고 1씩 뺀 3과 4에 //를 계산하면 1과 2가 나오는 특성을 활용할 수 있음 (ex. 문자열의 가운데 문자 출력 문제)
        - 1세기는 1년~100년 처럼 구분할 때 -1을 하거나 99를 더해서 //100으로 연산, 전자는 +1를 추가적으로 더해 구할 수 있음
  - 02 문자열 자료형
    - 문자열 연산
      - \+ : 더해서 연결하기 (Concatenation)
        - formatting을 이용하여 연결할 수 있다.
      - \* : 문자열 곱하기
      - len () : 문자열 길이
      - in : 해당 요소가 문자열에 있는지 여부를 확인 (Containment Test)
    - 문자열 인덱싱과 슬라이싱
      - 인덱싱 (a[i], i는 정수)
      - 슬라이싱 (a[i:j], i,j는 정수 또는 빈칸, i <= a < j, |i|+|j|<len(a)) 
      - 인덱싱을 통한 글자 변경은 안되므로 슬라이싱해서 더해야한다.
    - 이스케이프 문자열
      - \n, \t, \r, \0, \\, \', \"
    - 포매팅 (%-formatting, str.format(), f-strings)
      - %-formatting : %s, %c, %d, %f, %o, %x, %%
      - str.format(), f-strings : { :c<n }, { :c^n }, { :c>n }, { :n.n'f}, { :0nd}
    - 관련 함수
      - .count(x) : 문자 개수 세기
      - .find(x), .rfind(x) : 왼쪽/오른쪽부터 처음으로 나온 문자의 위치 알려줌, 없으면 -1 반환
      - .index(x) : 왼쪽부터 처음으로 나온 문자의 위치 알려줌, 없으면 오류 발생
      - .join(iterable) : 인수로 받은 문자열 사이사이에 해당 문자열 삽입
      - .upper(), .lower()  : 전체 대/소문자
      - .swapcase() : 대<->소문자로 변경
      - .lstrip([chars]), .rstrip([chars]), strip([chars]) : 여백 제거, 바로 인접한 문자열 삭제
      - .replace(old, new[, count]) : 인수에 해당하는 문자열 바꾸기, count 수만큼 시행
      - .split([x]) : 공백 기준으로 나누기, 인수로 받는 문자열 기준으로 나누기, 리스트로 출력
      - .capitalize() : 앞글자를 대문자로 만들어 리턴
      - .title() : 어포스트로피나 공백 이후 처음나오는 문자를 대문자로 만들어 리턴
      - 확인 메소드 : True/False 리턴
        - .isaplha() : 문자열을 감지
        - .isdigit() : 숫자로만 구성된 문자열 탐지
        - .isdecimal() : 유니코드 객체로 소수점 문자가 포함되었는지 탐지
        - .isnumeric() : 유니코드 객체로 숫자로만 구성된 문자열 탐지
        - .isspace() : 공백만 포함되었는지 탐지
        - .issuper() : 모든 문자열이 대문자 여부를 탐지
        - .istitle() : 단어 마디마다의 첫글자가 대문자인지 탐지
        - .islower() : 소문자 문자열 감지
  - 03 리스트 자료형
    - 리스트 선언
      - 리스트명 = [요소1, 요소2, 요소3, ...]
      - 비어 있는 리스트 : a = list() or a = []
    - 리스트 인덱싱과 슬라이싱
      - 인덱싱 (a[i] [j]..., i, j...는 정수)
      - 슬라이싱 (a[i:j], i,j는 정수 또는 빈칸, i <= a < j, |i|+|j|<len(a)) 
      - 인덱싱을 통한 글자 변경 가능
    - 리스트 연산
      - \+ : 리스트 합
      - \* : 리스트 반복
      - len() : 리스트 길이
      - in : 해당 요소가 리스트에 있는지 여부를 확인 (Containment Test)
    - 리스트 수정과 삭제
      - 인덱싱으로 초기화 (a[i] = n)
      - del 함수와 인덱싱으로 삭제 (del a[i])
    - 리스트 관련 함수
      - index, pop을 제외한 함수를 사용하면 None을 반환하므로 변수에 바로 초기화 시키면 안된다. 즉 원본이 변한다.
      - .append(x) : 요소 추가
      - .sort() : 정렬, 원본이 변경됨
      - .reverse() : 역순으로 뒤집기, 원본이 변경됨
      - .index(x) : 해당 값 위치 리턴
      - .remove(x) : 첫 번째로 나오는 x 삭제
      - .pop([i]) : 해당 인덱스 요소나 리스트의 마지막 요소 없애면서 그 요소 반환
      - .count(x) : 리스트 내의 해당 요소 갯수
      - .extend(iterable) : iterable 객체를 인수로 받아 그 리스트를 추가시킴, 문자열은 문자 하나하나로 추가됨
      - .insert(i, x) : 정해진 위치 i에 x를 추가
  - 04 튜플 자료형
    - 튜플 특징
      - (와 )로 둘러 쌓임
      - 값을 바꿀 수 없음
    - 튜플 연산
      - \+ : 튜플 합
      - \* : 튜플 반복
      - len() : 튜플 길이
      - in : 해당 요소가 튜플에 있는지 여부를 확인 (Containment Test)
    - 튜플의 인덱싱과 슬라이싱
      - 인덱싱 (a[i] [j]..., i, j...는 정수)
      - 슬라이싱 (a[i:j], i,j는 정수 또는 빈칸, i <= a < j, |i|+|j|<len(a)) 
  - 05 딕셔너리 자료형
    - 딕셔너리 선언
      - {Key1:Value1, Key2:Value2, Key3:Value3, ...}
      - Key는 변하지 않는 값, Value는 변하지 않는 값, 변하는 값 모두 (변수 포함)
      - 변수 = dict([Key1=Value1, Key1=Value1, ...)
      - 변수 = dict.fromkeys(Key로 사용할 리스트, Value)
      - {arr[i] : i for i range(a)} 식으로도 선언 가능
    - 딕셔너리 쌍 추가, 삭제
      - 쌍 추가 : a = {Key : Value}, a[Key] = Value
        - 반복문에서 바로바로 해당 요소에 값을 변경시킬 수 있음
      - 쌍 삭제 : del a[Key]
      - Key가 중복되면 마지막에 선언된 것만 남는다.
      - Key를 리스트로 사용할 수 없다.
    - comprehension
      - { key : value for key, value in 반복 가능한(iterable) 자료형 if  조건문 }
    - 반복문에서 사용할 때
      - 딕셔너리 객체를 그냥 사용할 때 key 값으로 초기화 됨
    - 딕셔너리 관련 함수
      - .keys() : Key로만 구성된 dict_keys 리스트
      - .values() : Value로만 구성된 dict_values 리스트
      - .items() : (Key, Value) 쌍으로 구성된 dict_items 리스트
      - .clear() : 모두 지워 빈 딕셔너리로 만들기
      - .get(key[, default]) : a['Key']와 같지만 없으면 None을 리턴함
      - Key in a : 해당 키가 딕셔너리 안에 있는지 조사함
      - .pop(key[, default]) : key가 딕셔너리에 있으면 제거하고 그 값을 리턴, 그렇지 않으면 default를 리턴
      - .update(key1=value1[, key2=value2] [, ...]) : 딕셔너리 추가, key에는 따옴표를 사용하지 않음
  - 06 집합 자료형
    - 집합의 선언
      - set(리스트 or 문자열)을 사용하여 선언
    - 집합의 특징
      - 중복을 허용하지 않는다. -> 중복을 제거하기 위한 필터로 사용
      - 순서가 없다. -> 인덱싱 이용 불가
        - 요소가 하나 밖에 없다면 .pop()을 이용
    - 집합의 연산
      - & : 교집합 ( .intersection() )
      - | : 합집합 ( .union() )
      - \- : 차집합 ( .difference() )
    - 집합 관련 함수
      - .add(x) : 값 1개 추가
      - .update(*args) : 값 여러 개 추가
      - .remove(x) : 특정 값 제거, 없으면 에러 발생
      - .discard(x) : 특정 값 제거, 없어도 에러가 발생하지않음
      - .pop() : 임의의 원소를 제거해 반환
  - 07 불 자료형
    - bool
      - True
        - False를 제외한 비어 있지 않은 객체
      - False
        - "", [], {}, (), 0, None
    - 불 연산
      - bool() : 해당 인수에 대해 True, False를 알아봄
  - 08 자료형의 값을 저장하는 공간, 변수
    - 시퀀스(sequence) 자료형
      - 리스트, 튜플, 문자열, 바이너리, range가 해당
      - 집합과 딕셔너리는 해당하지 않음
      - 기준을 잡고 정렬이 되어있지 않고 요소가 입력된 순서대로 유지되어 있음
      - in, not in, +, *, [i] (indexing), [i:j:k] (slicing), len, min, max, .count 사용 가능
    - 객체를 가리키는 것
      - id 함수로 주소값을 알아낼 수 있음
      - is를 이용해 두 변수가 가리키는 객체가 같은지 여부를 알 수 있음
    - 복사
      - 얕은 복사
        - 리스트안에 리스트 mutable객체 안에 mutable객체인 경우 문제가 됨
        - [:], copy 모듈의 copy 메서드 사용
      - 깊은 복사
        - 내부에 객체들까지 모두 새롭게 복사 되는 것
        - copy 모듈의 deepcopy 메서드 사용
    - 변수를 만드는 여러 가지 방법
      - a, b = ('python', 'life')
      - (a, b) = 'python', 'life'
      - [a, b] = ['python', 'life']
      - a = b = 'python'
      - a, b = b, a : Swap
    - 변경불가능 / 변경가능
      - immutable : 리스트, 딕셔너리, 집합을 제외한 모든 객체
      - mutable : 리스트, 딕셔너리, 집합
        - 복사를 위해 단순한 변수끼리의 초기화가 아닌 얇은 복사, 깊은 복사가 필요함
    - 반복 가능 / 값을 차례대로 사용 가능
      - Iterable : 리스트, 딕셔너리, 집합, 문자열, 튜플, range, bytes
        - collections 모듈을 이용해 isinstance(객체, collections.Iterable )로 확인 가능
      - Iterator : Iterable 객체를 iter 로 형변환 하여 사용
        - .__next__()로 맨 앞의 요소부터 값을 꺼내어 사용할 수 있음, 다 꺼네면 'StopIteration'이라는 예외가 발생함
    - namespace 및 scope
      - 파이썬에서 사용되는 이름들은 이름공간(namespace)에 저장되어 있음
      - 변수에서 값을 찾을 때 다음 순서로 이름을 찾아나감
        - Local scope (정의된 함수) > Enclosed scope (상위 함수) > Global scope (함수 밖의 변수 혹은 import된 모듈) > Built-in scope (파이썬안에 내장되어 있는 함수 또는 속성)
        - 이름 공간의 수명주기
          - built-in scope : 파이썬이 실행된 이후부터 끝까지
          - Global scope : 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 끝까지
          - Local/Enclosed scope : 함수가 실행된 시점 이후부터 리턴할때 까지
- 02장 프로그램의 구조를 쌓는다! 제어문
  - 01 if문
    - x in s, x not in s
      - s 자리에 리스트, 튜플, 문자열을 받는다.
    - Conditional Expression
      - 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
  - 02 while문
    - while len(r) <1 처럼 반복할 수록 r의 길이가 변하는 방법으로 반복문을 돌릴 수 있음
  - 03 for문
    - [표현식 for 항목 in 반복가능객체 if 조건문]
    - for-else 문
      - for문을 끝까지 실행하고 나서 else 실행
      - for문에서 break 되면 else까지 실행하지 않음
- 03장 프로그램의 입력과 출력은 어떻게 해야 할까?
  - 01 함수
    - 재귀 함수
      - 함수 내부에서 자기 자신을 호출하는 함수이며 파이썬에서 2953번의 깊이까지 들어갈 수 있도록 제한됨
    - 함수 선언
      - def 함수이름(매개변수1,..) : body
      - lambda 매개변수1.. : body
    - 매개변수
      - Packing
        - 함수 선언시 입력 : 여러 개를 받아 리스트로 변환
      - Unpacking
        - 매개변수로 입력 : 리스트에서 각각의 인수로 나눠서 입력
      - *args : 리스트 형식
      - **kwargs : 딕셔너리 형식, 매개변수로 입력 될 때 Key=Value 형식으로 입력함
    - 함수 안에서 함수 밖의 변수를 변경하는 방법
      - return 이용
      - global 변수명 이용
    - 기타 사항
      - return은 무조건 하나만
      - 함수 선언시 매개변수에 초기화시키면 default 값 설정
  - 02 사용자 입력과 출력
    - 사용자 입력
      - input() 사용
      - sys 모듈의 stdin 변수 사용
    - print
      - 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
      - 문자열 띄어쓰기는 콤마로 한다
      - end = 문자열 : print의 문자열이 끝날 때 end에 저장된 문자열 출력, default는 '\n'
  - 03 파일 읽고 쓰기
    - open
      - 파일 객체 = open(파일 이름, 파일 열기 모드)
      - 파일 열기 모드 : 'r', 'w', 'a' [+ 'b']
      - 파일 이름만 쓰면, 동일 디렉터리에서 검색, 다른 곳에서 읽을 때는 주소 전체 입력
      - 파일 객체.close()로 마지막에 닫아줘야함
        - ' with open(파일 이름, 파일 열기 모드) as 파일 객체: '로 작성할 시 따로 close()를 사용할 필요가 없음
    - 파일 객체 함수
      - 읽기
        - .readline() : 한 줄씩 읽기
        - .readlines() : 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트로 리턴
        - .read() :  파일의 내용 전체를 문자열로 리턴
      - 쓰기
        - 쓰기모드 'w'로 하면 기존에 있던 내용이 없어지고 새로 기록한다. 반면 추가모드 'a'로 하면 기존에 있는 내용에 이어서 기록한다.
        - .write(x) : 받은 인수를 파일에 기록
- 04장 파이썬 날개 달기
  - 01 파이썬 프로그래밍의 핵심, 클래스
    - self
      - def 메서드(self, 매개변수1,...):
      - 메서드를 호출한 인스턴스 객체가 자동으로 전달됨
      - 그 인스턴스 객체가 갖고 있는 인스턴스 변수를 만들어 가질 수 있음
    - \__init__ (생성자)
      - 인스턴스 객체를 생성할 때 실행되는 함수
    - \__del__ (소멸자)
      - 인스턴스 객체가 소멸할 때 실행되는 함수
    - 인스턴스 -> 클래스순으로 namespace를 탐색
    - 상속
      - 자식 클래스에서 못 찾는 것을 부모 클래스에서 찾아 사용함
      - 오버라이딩
        - 부모 클래스 메서드의 실행 대신에 자식 클래스에서 재정의 된 메서드를 호출함
        - 연산자 오버라이딩으로 기존에 사용했던 연산자 기능과 다르게 설정할 수 있음
          - \__add__ (+), \_\_sub__ (-), \_\_mul__ (*), \_\_lt__ (<), \_\_le__ (<=), \_\_eq__ (==), \_\_ne__ (!=), _\_ge__ (>=), _\_gt__ (>)
        - super()
          - 자식 클래스에서 부모 클래스의 메서드 내용을 가지고 올 수 있음
          - 그러나 부모 클래스의 메서드 내 변수 등이 자식 클래스에서 공유가 되지 않음
      - 생성자, 소멸자, 오버라이딩 된 연산자들도 같이 상속되므로 자식 클래스에서 따로 오버라이딩을 하지 않는 이상 자식 클래스에서도 적용되는 것을 주의해야함
      - 상속관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스 -> 전역순으로 namespace가 확장됨
    - 클래스 변수
      - 인스턴스 변수와 다르게 클래스 변수는 모든 인스턴스 객체에 같은 주소값으로 공유되는 변수임
      - 수정을 하려면 클래스에 직접 접근하여 변경해야하며 인스턴스 객체를 통해 수정하려고 하면 클래스 변수명과 같은 인스턴스 변수가 생성됨.
    - isinstance
      - 인스턴스, 클래스 이름을 받아 해당 인스턴스가 그 클래스의 인스턴스인지 확인하여 True 또는 False를 리턴
      - 상속관계를 파악하는데도 사용할 수 있음
      - if not isinstance(total, (int, float)) or total <0 : return 0 처럼 입력값 확인으로 사용 할 수 있음
    - 메서드
      - 인스턴스 메서드
        - 첫 번째 인자로 인스턴스(self)를 받는 메서드
        - '클래스.인스턴스메서드'로 접근하면 오류, 단 인스턴스 객체를 인수로 넣는다면 억지로 사용 가능
      - 클래스 메서드
        - 첫 번째 인자로 클래스(cls)를 받는 메서드, 클래스 변수를 조작할 때 사용
        - 함수 선언 def 바로 앞 줄에 @classmethod 입력
        - 인스턴스 객체, 클래스로부터 접근하여 사용 가능
      - 정적 메서드
        - 인자로 아무것도 받지 않는 메서드, 데이터 조작을 하지 않을 때 사용
        - 함수 선언 def 바로 앞 줄에 @staticmethod 입력
        - 인스턴스 객체, 클래스로부터 접근하여 사용 가능
  - 02 모듈
    - import 모듈
    - from 모듈 import 모듈함수1,..
    - from 모듈 import *
      - 메모리 상에 모든 모듈함수들이 load가 되고 잘못하면 오버라이드로 인해 의도치않게 작동될 수 있다.
    - if \__name__ == "\_\_main__ " :
      - 이하의 코드는 이 파일이 모듈로 사용될 때 실행되지 않음
      - 파일이 직접 실행될 때는 \__name\_\_는 \_\_main__으로 초기화 됨
      - 모듈로 사용될 때는 \__name__는 모듈이름으로 초기화 됨
    - 모듈 추가
      - sys모듈의 sys.path.append(모듈을 저장한 디렉터리) 사용
      - bash에서 set PYTHONPATH=모듈을 저장한 디렉터리 사용
  - 03 패키지
    - 패키지로 사용할 폴더의 최상단부터 이하의 모든 폴더 안에 __init__.py명의로 저장
    - 해당 패키지가 저장된 디렉터리를 PYTHONPATH 환경변수에 추가
    - \_\_init_\_.py 에 __all__ = [추가시킬 모듈명]을 저장하면 from .. import * 로 사용가능 (단, 최하위 디렉터리를 from으로 부를 땐 상관없이 * 사용 가능)
    - 상대경로는 ..sound.echo 처럼 부모 디렉터리를 생략해 작성할 수 있다. 단, 불러올 모듈이 사용하는 파일이 있는 곳과 동일한 깊이이여야 한다.
  - 04 예외 처리
    - try: ... except [발생 오류[as 오류 메시지 변수]]: ...
      - try를 실행 시켰는데  except에 정의한 오류가 발생하면 except절을 실행시킴
      - except절에 pass를 입력하면 특정 오류를 회피할 수 있음
    - try: ... finally: ...
      - 예외 발생 여부에 상관없이 finally절을 실행
    - raise 오류명
      - NotImplementedError 처럼 일부러 오류를 발생시킬 때 사용함
    - 예외 만들기
      - Exception 클래스를 상속시킨 클래스를 만든다.
        - 예외 처리 기법으로 메세지를 출력하고 싶으면 def \__str__(self) : .. 메서드를 선언해야함
      - 'raise 상속받은 클래스' 형식으로 사용한다.
      - 'try: ... except 상속받은 클래스명: ...'형식으로 사용한다.
  - 05 내장 함수
    - abs(x)
      - 숫자의 절대값을 리턴
    - all(x)
      - 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며, 이 x의 모든 요소가 참이면 True, 거짓이 하나라도 있으면 False를 리턴
    - any(x)
      - 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며, 이  x 중 하나라도 참이 있을 경우 True를 리턴하고, x가 모두 거짓일 경우에만 False를 리턴
    - chr(x)
      - 아스키(ASCII) 코드값을 입력으로 받아 그 코드에 해당하는 문자를 출력
    - dir(x)
      - 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌
    - divmod(a, b)
      - 숫자 두 개를 받아 a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴
    - enumerate(iterable)
      - 리스트, 튜플, 문자열과 같은 순서가 있는 자료형을 입력으로 받아 (idx, 요소) 형식으로 짝지여진 enumerate 객체를 리턴, 형변환이 필요함
    - eval(x)
      - 'divmod(4, 3)'같은 실행 가능한 문자열을 입력을 받아 문자열을 실행
    - filter(fnc, x) 
      - True, False를 리턴하는 함수와 반복 가능한(iterable) 자료형을 인수로 받아 True인 인수만 묶어서 리턴
    - hex(x)
      - 정수값을 입력받아 16진수(hexadecimal)로 변환하여 리턴
    - id(x)
      - 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 리턴
      - is 연산자를 사용하여 동일한 object인지 확인할 수 있음
    - input([x])
      - 사용자 입력을 받는 함수, 입력받기 전 출력할 문자열을 x로 받음
    - int(x)
      - 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 리턴
      - int(숫자 문자열, n진수)는 n진수인 숫자 문자열을 10진수 정수로 리턴
    - isinstance(x, y)
      - 인스턴스, 클래스 이름을 받아 해당 인스턴스가 그 클래스의 인스턴스인지 확인하여 True 또는 False를 리턴
      - 상속관계를 파악하는데도 사용할 수 있음
      - if not isinstance(total, (int, float)) or total <0 : return 0 처럼 입력값 확인으로 사용 할 수 있음
    - len(x)
      - 입력값 s의 길이(요소의 전체 개수)를 리턴
    - list(iterable)
      - 반복 가능한(iterable) 자료형을 입력받아 리스트로 만들어 리턴
    - map(fnc, iterable)
      - 함수와 반복 가능한(iterable) 자료형을 받아 자료형의 각 요소마다 함수를 수행한 결과를 묶어서 리턴
    - max(x)
      - 반복 가능한(iterable) 자료형을 입력받아 그 최대값을 리턴, 문자열은 아스키코드 값이 높은 것이 출력됨
    - min(x)
      - 반복 가능한(iterable) 자료형을 입력받아 그 최소값을 리턴, 문자열은 아스키코드 값이 낮은 것이 출력됨
    - oct(x)
      - 정수 형태의 숫자를 8진수 문자열로 바꾸어 리턴
    - open(x, 모드[, encoding=인코딩] [, newline=""] )
      - "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 리턴
      - 모드는 w, r, a, b가 있으며 b는 w, r, a과 함께 사용된다.
    - ord(x)
      - 문자의 아스키 코드값을 리턴
    - pow(x,y)
      - x의 y 제곱한 결과값을 리턴
    - range([start,] stop [,step])
      - 입력받은 숫자에 해당되는 범위의 값을 반복 가능한 객체로 만들어 리턴
    - round(number[, ndigits])
      - 숫자를 입력받아 반올림을 리턴
    - sorted(iterable)
      - 반복 가능한(iterable) 자료형을 받아 입력값을 정렬한 후 그 결과를 리스트로 리턴, .sort()와 다르게 원본을 건들지 않음
    - reversed(iterable)
      - 반복 가능한(iterable) 자료형을 받아 입력값을 거꾸로 정렬하나 이후 별도의 형변환이 필요함, .reverse()와 다르게 원본을 건들지 않음
    - str(x)
      - 문자열 형태로 객체를 변환하여 리턴
    - sum(x)
      - 리스트나 튜플의 모든 요소의 합을 리턴
    - tuple(x)
      - 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 리턴
    - type(x)
      - 입력값의 자료형을 리턴
    - zip(*iterable)
      - 동일한 개수로 이루어진 여러 자료형을 묶어 리턴, 길이가 다르면 짧은 쪽을 기준으로 잡음
    - bin(x)
      - 양의 정수를 받아서 '0b'가 붙어 있는 2진수로 표현
  - 06 외장 함수
    - sys
    - pickle
    - os
    - shutil
    - glob
    - tempfile
    - time
    - calendar
    - random
    - webbrowser
- 05장 파이썬 정규 표현식과 XML
  - 01 정규 표현식 살펴보기
  - 02 정규 표현식 시작하기
  - 03 강력한 정규 표현식의 세계로
  - 04 파이썬으로 XML 처리하기