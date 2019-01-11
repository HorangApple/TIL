# 01. Packing, Unpacking

https://python.bakyeono.net/chapter-5-5.html

`*변수` 로 함수의 매개변수에 전달하면 그 변수 시퀸스의 요소를 하나씩 꺼내어 전달이 된다. 이 때가 'Unpacking'

반면에 함수를 정의할 때 매개변수를 `*변수`로 선언하면 입력되는 여러 변수들을 리스트로 만들어 전달한다. 이 때가 'Packing'이다.

`*변수`와 `**변수` 차이는 전자는 리스트, 후자는 딕셔너리를 받거나 전달한다고 생각하면 된다.



# 02. filter 함수

https://wikidocs.net/32#filter

걸러내는 함수로 첫 번째 인수로 함수 이름, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 첫 번째 인수의 함수에 두 번째 인수의 요소가 하나씩 대입이 되고 그 함수가 `True`로 값이 리턴이 되면 대입한 값을 묶어주는 역할을 하고 있다. 그 결과를 리스트로 사용하고 싶으면 `filter`의 결과물을 리스트로 형변환해서 사용해야한다.



# 03. 재귀함수

재귀함수의 궁극적인 목적은 문제를 작게 만들어 해결한다는 점이다.

python에서 재귀함수의 최대 깊이는 1000번이라고 한다.



# 04. Comprehensions

```python
def reverse_letter(n):
    result = []
    for i in n :
        if i.isalpha() :
            result.append(i)
    return "".join(result[::-1])
```

위의 코드와 같이 `for문-if문-수식 한 줄`로 되어 있는데 이렇게 있으면 다음과 같이 한 줄로 줄일 수 있다.

```python
def reverse_letter(n):
    a = [c for c in n if c.isalpha()]
    return "".join(a[::-1])
```

한 줄로 줄일 수 있는 전제조건은 for문과 if문 사이에 어떠한 식이 오면 안되고 수식은 한 줄로 구성되어 있어야 가능하다. 

```python
dusts = {'서울': 72, '경기': 82, '대전': 29, '중국': 200}
dics = {key : '매우나쁨' if value>150 else '나쁨' if value>80 else '보통' for key, value in dusts.items()}
print(dics)
```

if문만 구성하거나 for문만 구성할 수 있다.



# 05. 정규표현식

