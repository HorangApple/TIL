## 1. reduce

```python
from functools import reduce
print(reduce(lambda x, y: x+y, [1,2,3,4,5])) # 15
```

값을 누적시키며 작동한다.

## 2. collections 라이브러리

```python
from collections import deque, OrderedDict, defaultdict, counter
```

OrderedDict

-  순서가 있는 dict

defaultdict

- key가 없어도 에러없이 default 값이 출력

counter

- sequence type의 data element들의 갯수를 dict 형태로 반환



## 2. Linear algebra codes

### 1) Vector의 계산

```python
u = [2, 2]
v = [2, 3]
z = [3, 5]

# 2*의 스칼라 계산
result = [2*sum(t) in zip(u, v, z)]
print(result)
# [14, 20]
```

### 2) Matrix addition

<img src = 'images/image 001.png'>

```python
matrix_a  = [[3, 6], [4, 5]]
matrix_b  = [[5, 8], [6, 7]]

result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]

print(result) # [[8, 14], [10, 12]]
```

### 3) Scalar-Matrix Product

```python
matrix_a = [[3, 6], [4, 5]]
alpha = 4
result = [[alpha * element for element in t] for t in matrix_a]

print(result) # [[12, 24], [16, 20]]
```

### 4) Matrix Transpose

<img src = 'images/image 002.png'>

```python
matrix_a = [[1, 2, 3], [4, 5, 6]]
result = [[element for element in t] for t in zip(*matrix_a)]

print(result) # [[1, 4], [2, 5], [3, 6]]
```

### 5) Matrix Product

<img src = "images/image 003.png">

```python
matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a * b for a, b in zip(row_a, column_b))
          for column_b in zip(*matrix_b)] for row_a in matrix_a]

print(result) # [[5, 8], [5, 6]]
```



## 3. Case Study - News Categorization

컴퓨터는 문자를 그대로 이해하지 못하기 때문에 문자를 숫자로 바꾼다. 숫자로 유사하다는 것을 표현하기 위해 좌표평면에서 점 사이의 거리를 통해 가까운 정도를 파악한다. 즉, 숫자를 벡터로 바꿔줘야 한다.

<img src = 'images/image 004.png'>

하나의 단어를 Vector의 Index로 인식시키며 단어가 존재하면 1, 없으면 0으로 하는 **One-hot Encoding**을 만든다. **Bag of words**는 단어별로 인덱스를 부여해서, 한 문장(또는 문서)의 단어의 개수를 Vector로 표현한다.

### 1) 유사성

- Euclidian distance (피타고라스 정리) 

  data set이 적을 때 사용한다.

<img src = 'images/image 006.png'>

- Consine distance (두 점 사이의 각도)

  문서끼리 비교할 때 자주 사용한다.

<img src = 'images/image 005.png'>

### 2) Process

- 파일 불러오기
- 파일을 읽어서 단어사전 (corpus) 만들기
- 단어별로 Index 만들기
- 만들어진 인덱스로 문서별로 Bag of words vector 생성
- 비교하고자 하는 문서 비교하기
- 얼마나 맞는지 측정하기

