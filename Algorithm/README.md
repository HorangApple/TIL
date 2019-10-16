# 알고리즘 정리

[TOC]

## 배열

### 01. 완전검색

- 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법

  - Brute-force 혹은 gernerate-and-test 기법이라고도 부름
  - 모든 경우의 수를 테스트한 후, 최종 해법을 도출

- 일반적으로 경우의 수가 상대적으로 작을 때 유용함

  - 모든 경우의 수를 생성하고 테스트하기 때문에 수행 속도는 느리지만, 해답을 못 찾는 경우는 없음

- (중복) 순열, (중복) 조합, 부분집합 등의 방법으로 경우의 수를 만들어 냄

- 완전 검색으로 접근하여 해답을 도출 한 후, 성능 개선을 위해 다른 알고리즘을 사용하는게 바람직

- 관련 문제

  - Baby-gin

  

### 02. 탐욕(Greedy) 알고리즘

- 최적해를 구하는데 사용되는 근시안적인 방법

  - 하나를 결정할 때마다 최적이라 생각되는 것을 선택해 나가는 방식으로 진행하여 해답 도출

- 각 선택의 시점에서는 최적이지만 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여, 그것이 최적이라는 보장은 없음

  - 그러나 성능이 좋기 때문에 반례까지 해결한 것을 증명해내면 안전하게 사용할 수 있음

- 일반적으로, 머릿속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근이 됨

- 동작과정

  ```
  1) 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합(Solution Set)에 추가한다.
  2) 실행 가능성 검사 : 새로운 부분해 집합이 실행 가능한지를 확인한다. 곧, 문제의 제약조건을 위반하지 않는지를 검사한다.
  3) 해 검사 : 새로운 부분해 집합이 문제의 해가 되는지를 확인한다. 아직 전체 문제의 해가 완성되지 않았다면 1)의 해 선택부터 다시 시작한다.
  ```

- 관련문제

  - 거스름돈 줄이기



### 03. 버블 정렬(Bubble Sort)

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

  - 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블정렬이라고 함

- 동작과정

  ```
  1) 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.
  2) 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
  ```

- 시간 복잡도

  - O(n^2)

- 코드

  ```python
  def BubbleSort(arr):
      for i in range(len(arr)):
          for j in range(len(arr)-i):
              if arr[j]>arr[j+1]:
                  arr[j],arr[j+1]=arr[j+1],arr[j]
  ```

  

### 04. 카운팅 정렬(Counting Sort)

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

- 제한사항

  ```
  1) 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 : 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문
  2) 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.
  ```

- 시간복잡도

  - O(n+k) : n은 리스트 길이, k는 정수의 최대값

- 코드

  ```python
  def CountingSort(arr,k): # arr:입력 배열, k:정수의 최대값
      length = len(arr)
      c=[0]*(k+1) # c:카운트 배열, 0도 넣기위해 +1
      b=[0]*length # b:정렬된 배열
      
      for i in range(0,length):
          c[arr[i]]+=1
      for i in range(1,k+1):
          c[i]+= c[i-1]
      for i in range(length):
          b[c[arr[i]]-1]=arr[i]
          c[arr[i]]-=1
    return b
  ```
  
  

### 05. 비트연산자

- << (shift) 연산자 

  - 1<<n : 2^n, 즉 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.
  -  i&(1<<j) : i의 j번째 비트가 1인지 아닌지 리턴한다.
- 관련문제

  - 부분집합 구하기

- 코드 (부분집합)

  ```python
  def PartsSet(n,arr): # n은 arr의 원소의 수
      result=[]
      for i in range(1<<n):
          part=[]
          for j in range(n):
              if i&(1<<j):
                  part.append(arr[j])
         	result.append(part)
      return result
  ```

- XOR(^)을 이용해서 `a=a^b; b=a^b; a=a^b`로 swap을 구현할 수 있다.



### 06. 순차 검색(Sequential Search)

- 일렬로 되어있는 자료를 순서대로 검색하는 방법

  - 가장 간단하고 직관적인 검색 방법
  - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
  - 구현이 쉬우나 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임

- 정렬되어 있지 않은 경우

  - 처음부터 끝까지 일일히 검사하기 때문에 찾고자 하는 원소의 순서에 따라 비교회수가 결정

  - 코드

    ```python
    def SequentialSearch1 (arr,n,key):
        i=0
        while i<n and arr[i]!=key:
            i+=1
        if i<n :
            return i
        else :
            return -1
    ```

- 정렬되어 있는 경우

  - 키 값을 비교하며 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없는 것으로 더 이상 검색하지 않고 검색을 종료함

  - 코드

    ```python
    def SequentialSearch2 (arr,n,key):
        i=0
      	while i<n and arr[i]<key:
            i+=1
        if i<n and arr[i]==key:
            return i
        else :
            return -1
    ```

- 시간복잡도

  - O(n)



### 07. 이진 검색(Binary Search)

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로줄여가면서 보다 빠르게 검색을 수행함

- 제한사항

  ```
  이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.
  ```

- 동작과정

  ```
  1) 자료의 중앙에 있는 원소를 고른다.
  2) 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
  3) 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
  4) 찾고자 하는 값을 찾을 때까지 1)~3)의 과정을 반복한다.
  ```

- 코드

  ```python
  # 반복문
  def BinarySearch1(arr,key):
      start=0
      end=len(arr)-1
      while start<=end:
          middle=(start+end)//2
          if arr[middle]==key:
              return True
          elif arr[middle]>key:
              end=middle-1
          else:
              start=middle+1
  	return false
  
  # 재귀
  def BinarySearch2(arr,start,end,key):
      if start>end:
          return False
      else :
          middle=(start+end)//2
          if arr[middle]==key:
              return true
          elif arr[middle]>key:
              return BinarySearch2(arr,start,middle-1,key)
          else:
              return BinarySearch2(arr,middle+1,end,key)
  ```
  


### 08. 인덱스

- 테이블에 대한 동작 속도를 높여주는 자료 구조를 말함
  - 대량의 데이터를 매번 정렬하면 프로그램의 반응이 느려지기에 이를 해결해줌
- 인덱스는 key-field만 갖고 있기에 저장 공간이 테이블보다 작음



### 09. 셀렉션 알고리즘(Selection Algorithm)

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법

  - 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 함

- 동작과정

  ```
  1) 정렬 알고리즘을 이용하여 자료 정렬하기
  2) 원하는 순서에 있는 원소 가져오기
  ```

- 코드

  ```python
  def SelectionAlgorithm(arr,k):
      for i in range(0,k):
      	minIdx=i
          for j in range(i+1,len(arr)):
              if arr[minIdx]>arr[j]:
              	minIdx=j
                  arr[minIdx],arr[j]=arr[j],arr[minIdx]
      return arr[k-1]
  ```

- 시간복잡도

  - O(k*n)



### 10. 선택 정렬(Selection Sort)

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

  - 셀렉션 알고리즘을 전체 자료에 적용

- 동작과정

  ```
  1) 주어진 리스트 중에서 최소값을 찾는다.
  2) 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
  3) 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.
  ```

- 시간복잡도

  - O(n^2)

- 코드

  ```python
  def SelectionAlgorithm(arr):
      for i in range(0,len(arr)-1):
      	minIdx=i
          for j in range(i+1,len(arr)):
              if arr[minIdx]>arr[j]:
              	minIdx=j
                  arr[minIdx],arr[j]=arr[j],arr[minIdx]
      return arr
  ```

  

## 문자열

### 01. 문자열

- 아스키 코드
  - A(65)~Z(90), a(97)~z(122)
  - 표준 아스키는 세계적으로 통용되어 있지만 확장 아스키는 디바이스가 그것을 해독할 수 있도록 설계되어 있어야함
- endian
  - big-endian
    - 값을 뒤 쪽에 작성
    - 워크스테이션에서 사용되며 디버깅이 편리하고 비교연산에서 빠름
  - little-endian
    - 값을 앞 쪽에 작성
    - 메모리에 저장된 하위 바이트들만 사용할 때 별도의 계산이 필요없음
    - 산술연산에서 빠름



### 02. 패턴 매칭

#### 01) 고지식한 패턴 검색 알고리즘(Brute Force)

- 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작

- 코드

  ```python
  def BruteForce(arr,search):
      m=len(arr)
      n=len(search)
      i=0
      j=0
      while i<m and j<n:
          if arr[i] != search[j]:
              i=i-j # j는 i가 움직인 거리로 백업변수를 사용하지 않고 구현
              j=-1
          i+=1
          j+=1
      if j==n:
          return i-n # 일지하는 문자열의 시작위치 리턴
      else:
          return -1
  ```

- 시간복잡도

  - O(m*n)

#### 02) 카프-라빈 알고리즘(Rabin-Karp Algorithm)

- 문자열을 수치로 변환시켜 탐색하는 일대일 매칭 알고리즘

- 해시 함수를 통해 나온 결과를 인덱스로 하여 해시테이블에 저장하는 해싱(Hashing)방식을 기반으로 함

  - 충돌이 편향적으로 심각하게 발생하면 군집화(clustering)이 일어나 효율이 떨어짐

  - 충돌하는 값이 많으면 해당 인덱스 값을 모두 찾는데에 시간이 많이 소요됨

  - 해시 함수를 잘 만드는 것이 가장 중요

  - 주로 `Rabin fingerprint`가 사용됨 (함수 S는 아스키 코드 변환 함수인  `ord` 사용)
    $$
    f(x)=m_0+m_1x+...+m_{n-1}x^{n-1}
    $$

    $$
     H[i]=S[i]*2^{M-1}+S[i+1]*2^{M-2}+...+S[i+M-2]*2^1+S[i+M-1]*2^0
    $$

    $$
    H[i+1]=2*(H[i]-S[i]*2^{M-1})+S[i+M]*2^0
    $$

- 동작과정

  ```
  1) 비교 대상 문자열에서 찾을 문자열의 길이만큼 한 칸씩 옮기며 해시함수를 이용해 숫자로 변환
  2) 찾을 문자열의 해시값과 일치한 값이 있는지 확인
  ```

- 시간복잡도

  - 해시 함수에 따라 다름

#### 03) KMP 알고리즘

- 불일치가 발생한 문자열 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행하는 알고리즘

- 패턴을 전처리하여 불일치가 발생할 경우 이동할 다음 위치를 구해서 잘못된 시작을 최소화함

  <img src="images/image 001.png"/>

  <img src="images/image 002.png"/>

- 코드

  ```python
  def getPi(search):
      pi = [0]*len(search)
      
      j = 0
      for i in range(1,len(search)):
          while j > 0 and search[i] != search[j]:
              j = pi[j-1]
              
          if search[i] == search[j]:
              j+=1
              pi[i] = j
              
      return pi
  
  def kmp(arr, search):
      pi = getPi(search)
      
      j = 0
      for i in range(len(arr)):
          while j>0 and arr[i] != search[j]:
              j = pi[j-1]
              
          if arr[i] == search[j]:
              if j == len(search) - 1:
                  return i-len(search)+1
              else:
                  j+=1
      
      return -1
  ```
  
- 시간복잡도

  - O(n)

#### 04) 보이어-무어 알고리즘

- 패턴 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 패턴의 길이만큼 되는 알고리즘

  - 다른 알고리즘과 달리 텍스트 문자를 다 보지 않아도 됨

  <img src="images/image 003.png"/>
- 시간복잡도

  - 최선 : O(n), 최악 : O(m*n)



### 03. 문자열 암호화

#### 01) 시저 암호 (Caesar cipher)

- 평문에서 사용되고 있는 알파벳을 일정한 문자 수만큼 평행이동시킴으로써 암호화를 행함

#### 02) 단일 치환 암호

- 별도의 문자 변환표를 이용해 암호화

#### 03) bit열의 암호화

- 배타적 논리합(xor) 연산 사용



### 04. 문자열 압축

#### 01) Run-length encoding

- 같은 값이 몇 번 반복되는가를 나타냄으로써 압축
- 이미지 BMP 포맷의 압축방법

#### 02) 허프만 코딩 알고리즘



## 스택

### 01. 스택의 특성

- 1대1 관계를 갖는 선형 구조로 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 후입선출(LIFO, Last-In-First-Out)
- 연산
  - 삽입 : push, 저장소에 자료를 저장함
  - 삭제 : pop, 저장소에서 사입한 자료의 역순으로 꺼냄
  - 공백 확인, isEmpty
  - 스택의 top에 있는 item(원소)을 반환하는 연산, peek
- 고려사항
  - 구현이 용이하나 스택의 크기를 변경하기 어려움
  - 동적 연결리스트로 효율적인 동적 할당이 가능하나 구현이 복잡함

- 응용

  - 괄호검사

  - Function call

    <img src="images/image 004.png"/>



### 02. 재귀호출

- 자기 자신을 호출하여 순환 수행되는 것

- 프로그램의 크기를 줄이고 간단하게 작성할 수 있음



### 03. Memoization

<img src="images/image 005.png"/>

  - 재귀호출은 많은 중복 호출이 존재하기에 성능을 높이기 위해 미리 저장한 이미 계산된 값을 불러오도록 함



### 04. DP(Dynamic Programming)

- 동적 계획, 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘
- 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

<img src="images/image 006.png"/>



### 05. DFS(깊이우선탐색)

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 스택을 이용해 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법

- 동작과정

  ```
  1) 시작 정점 v를 결정하여 방문한다.
  2) 정점 v에 인접한 정점 중에서
  	(1) 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2)를 반복한다.
  	(2) 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2)를 반복한다.
  3) 스택이 공백이 될 때까지 2)를 반복한다.
  ```

- 코드

  ```python
  #1
  road=주어진 인접행렬
  
  visited=[False]*length
  stack=[0]
  def dfs(v):
      visited[v]=True
      while(v):
          w=search(v)
          if w:
              stack.append(v)
          while(w):
              visited[w]=True
              stack.append(w)
              v=w
              w=search(v)
          v=stack.pop()
          
  def search(v):
      for i in road[v]:
          if i>0 and not visited[i]:
      		return i
          
  #2
  def dfs(v): # v: 시작점
      stack = [] # 스택
      visited = [False] * (n+1)
      visited[v] = True
      print(v, end=' ')
      stack.append(v)
      while len(stack) > 0: # 빈 스택이 아닐 동안
          # v: 현재 방문 정점
          # v의 방문 하지 않은 인접 정점(w) 하나 찾는다.
          for w in G[v]:
              if not visited[w]:
                  visited[w]=True
                  print(w, end=' ')
                  stack.append(v)
                  v = w
                  break
          else:
              v = stack.pop()
  
  # 재귀 ver, 방문 순서를 저장, 즉 스택을 사용할 필요가 없어서 간단하다.
  def dfs2(v): # v: 현재 방문 정점
      visited[v] = True
      print(v,end=' ')
      # 방문하지 않은 인접 정점을 찾아서 방문
      for w in G[v]:
          if not visited[w]:
              dfs2(w)
  
  
  # 인접 리스트 구현
  n, e = map(int, input().split())
  G=[[] for _ in range(n+1)]
  for _ in range(e):
      u,v = map(int,input().split())
      G[u].append(v)
      G[v].append(u)
  
  dfs(1)
  ```

  

### 06. 계산기

- 중위표기법(infix notation)

  - 연산자를 피연산자의 가운데 표기하는 방법

- 후위표기법(postfix notation)

  - 연산자를 피연산자 뒤에 표기하는 방법

- 동작과정

  <img src="images/image 007.png"/>

  ```
  1) 중위 표기법의 수식을 후위 표기법으로 변경한다. (스택 이용)
  2) 후위 표기법의 수식을 스택을 이용하여 계산한다.
  ```

  

### 07. 백트래킹

- 해를 찾는 도중에 '막히면' (즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법

- 최적화(optimization) 문제와 결정 (decision) 문제를 해결할 수 있음

- 결정 문제: 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no'로 답하는 문제

  - 미로찾기
  - n-Queen 문제
  - Map coloring
  - 부분 집합의 합(Subset Sum) 문제 등

- DFS와의 차이

  - 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임(Prunning, 가지치기)
  - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능

- 동작과정

  ```
  1) 상태 공간 트리의 깊이 우선 검색을 실시
  2) 각 노드가 유망한지를 점검
  3) 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속 진행함
  ```

  

### 08. 부분집합 구하기

- 어떤 집합의 공잡합과 자기자신을 포함한 모든 부분집합을 powerset이라고 하며 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 2^n이 나온다.

  <img src="images/image 008.png"/>

- 부분집합 코드

  ```python
  def backtrack(a, k, inp): # k는 깊이 inp는 자릿수
      global MAXCANDIDATES
      c=[0]*MAXCANDIDATES
      if k==inp:
          process_solution(a,k) # 답이면 원하는 작업을 한다
      else:
          k+=1
          ncandidates=construct_candidates(a,k,inp,c) # 자리에 올 후보군을 추린다.
          for i in range(ncandidates):
              a[k]=c[i]
              backtrack(a,k,inp)
              
  def construct_candidates(a,k,inp,c):
      c[0]=True
      c[1]=False
      return 2
  
  MAXCANDIDATES=100
  NMAX=100
  a=[0]*NMAX
  backtrack(a,0,3)
  ```

  

  <img src="images/image 009.png"/>

- 순열 코드

  ```python
  def backtrack(a, k, inp): # k는 깊이 inp는 자릿수
      global MAXCANDIDATES
      c=[0]*MAXCANDIDATES
      if k==inp:
          for i in range(1,k+1):
              print(a[i],end=" ")
          print()
      else:
          k+=1
          ncandidates=construct_candidates(a,k,inp,c) # 자리에 올 후보군을 추린다.
          for i in range(ncandidates):
              a[k]=c[i]
              backtrack(a,k,inp)
              
  def construct_candidates(a,k,inp,c):
      in_perm=[False]*NMAX
      for i in range(1,k):
          in_perm[a[i]]=True
          
      ncandiates=0
      for i in range(1,inp+1):
          if in_perm[i]==False:
              c[ncandiates]=i
              ncandiates+=1
      return ncandiates
  
  MAXCANDIDATES=100
  NMAX=100
  a=[0]*NMAX
  backtrack(a,0,3)
  ```

  

### 09. 분할 정복 알고리즘

<img src="images/image 010.png"/>

- 설계전략
  - 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눔
  - 정복(Conquer) : 나눈 작은 문제를 각각 해결함
  - 통합(Combine) : (필요하다면) 해결된 해답을 모음



### 10. 퀵정렬

- 합병정렬과 달리 기준 아이템(pivot item) 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킴

- 합병정렬과 달리 합병하는 후처리 작업이 필요하지 않음

- 코드

  ```python
  def quickSort(a,begin,end):
      if begin<end:
          p=partition1(a,begin,end)
          quickSort(a,begin,p-1)
          quickSort(a,p+1,end)
  
  # 일반
  def partition1(a,begin,end):
      pivot=(begin+end)//2
      l=begin
      r=end
      while l<r :
          while(a[l]<a[pivot] and l<r) : l+=1
          while(a[r]>=a[pivot] and l<r) : r-=1
          if l<r:
              # l이 먼저 pivot에 도달하면 교환하면 안되므로 같게 만들어줌
              if l==pivot : pivot=r 
              a[l],a[r]=a[r],a[l]
      a[pivot],a[r]=a[r],a[pivot]
      return r
  
  # Hoare-Partition 알고리즘
  def partition1(a,l,r):
      p=a[l]
      i,j = l,r
      while i<j:
          while i<len(a) and a[i] <= p: i+=1
          while j>l and a[j] >= p: j-=1
          if i < j : a[i],a[j] = a[j],a[i]
      
      a[l],a[j] = a[j],a[l]
      return j
  
  # Lomuto partition 알고리즘
  def partition2(a,p,r):
      x=a[r]
      i=p-1
      for j in range(p,r):
          if a[j]<=x:
              i+=1
              a[i],a[j] = a[j],a[i]
      a[i+1],a[r] = a[r],a[i+1]
      return i+1
  ```

- 시간복잡도
  - O(n^2)
  - 평균복잡도는 nlogn



## 큐(Queue)

### 01. 큐의 특성

- 선입선출 (FIFO, First In First Out)

* 참고 : pop(0)의 경우 가장 앞의 요소를 pop하는 대신에 전체 리스트를 전부 왼쪽으로 이동(shift)시키는 작업이 동반되는 O(N)의 작업이기에 빠른 속도를 내기 위해서는 직접 구현하는 것이 좋음

### 02. 선형 큐

- 초기 상태: front=rear=-1

- 포화 상태: rear=n-1

- 마지막엔 공간이 있음에도 불구하고 포화상태로 인식하여 더 이상 삽입을 수행하지 않게 됨

- 코드

  ```python
  class LineQueue:
      def __init__(self):
          self.front=-1
          self.rear=-1
          self.queue=[0]*n
          
      def enQueue(self,item): # 삽입
          if self.isFull() : print("Queue_Full")
          else :
              self.rear+=1
              self.queue[self.rear]=item
              
      def deQueue(self): # 삭제
          if self.isEmpty() : print("Queue_Empty")
          else :
              self.front+=1
              return self.queue[self.front]
          
      def isEmpty(self): # 공백상태
          return self.front==self.rear
      
      def isFull(self): # 포화상태
          return self.rear==len(self.queue)-1
      
      def Qpeek(self): # 가장 앞에 있는 원소 출력
          if self.isEmpty(): print("Queue_Empty")
          else : return self.queue[self.front+1]
  ```

    

### 03. 원형 큐

  - 초기 상태: front=rear=0
  - Index의 순환

    - front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후, 나머지 연산자를 이용한 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동함

  - front 변수

    - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고  항상 빈자리로 둠
    - `deQueue()`가 수행되고 나서 front가 앞으로 움직임

    <img src="images/image 011.png"/>

  - 코드

    ```python
    class CircleQueue:
        def __init__(self):
            self.front = 0
            self.rear = 0
            self.queue= [0] * (n + 1)
    
        def isEmpty(self):  # 공백상태
            return self.front == self.rear
    
        def isFull(self):  # 포화상태
            return (self.rear + 1) % len(self.queue) == self.front
    
        def enQueue(self,item):  # 삽입
            if self.isFull():
                print("Queue_Full")
            else:
                self.rear = (self.rear + 1) % len(self.queue)
                self.queue[self.rear] = item
    
        def deQueue(self):  # 삭제
            if self.isEmpty(): print("Queue_Empty")
            else:
                self.front = (self.front + 1) % len(self.queue)
                return self.queue[self.front]
    ```



### 04. 연결 큐

  - 큐의 원소: 단순 연결 리스트의 노드
  - front: 첫 번째 노드를 가리키는 링크
  - rear: 마지막 노드를 가리키는 링크
  - 초기 상태: front=rear=None
  - 공백 상태: front=rear=None
  - 코드

    ```python
    class LinkedQueue:
        def __init__(self,front,rear,item):
            self.front=front
            self.rear=rear
            self.item=item
            self.next=n
        
        def enQueue(self,item): # 삽입
            newNode = Node(item)
            if self.isEmpty():
                self.front=newNode
            else:
                self.rear.next=newNode
            self.rear=newNode
                
        def deQueue(self): # 삭제
           if self.isEmpty() : 
                print("Queue_Empty")
                return None
            self.item=self.front.item
            self.front=self.front.next
            if self.isEmpty():
                self.rear=None
            return self.item
            
        def isEmpty(self): # 공백상태
            return self.front==None
        
        def Qpeek(self): # 가장 앞에 있는 원소 출력
            return self.front.item
        
        def printQ(self):
            f=self.front
            s=""
            while f:
                s+=f.item+" "
                f=f.next
            return s
    ```

  

### 04. 우선순위 큐
  - FIFO 순서가 아닌 우선순위가 높은 순서대로 먼저 나가게 됨
  - 적용 분야
    - 시뮬레이션 시스템
    - 네트워크 트래픽 제어
    - 운영체제의 테스크 스케줄링

- 활용

  - 버퍼(Buffer)

    - 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리 영역

      
### 05. BFS(Breadth First Search)

- 너비우선탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문 후에, 큐를 통해 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

- 코드

  ```python
  def BFS(g,v):
      visited=[0]*n
      queue=[]
      queue.append(v)
      while queue:
          t=queue.pop(0)
          if not visited[t]:
              visited[t]=True
              visit(t)
          for i in G[t]:
              if not visited[i]:
                  queue.append(i)
  ```




## 리스트(List)

### 01. 리스트의 성질

- 순서를 가진 데이터의 집합을 가리키는 추상자료형(abstract data type)
- 동일한 데이터를 가지고 있어도 상관없음
- 구현방법
  - 순차리스트: 배열을 기반으로 구현된 리스트
    - 배열 중간에 데이터를 삽입/삭제시키는 과정이 많은 연산량을 요구
    - 배열의 크기가 정해져 있어 실제 사용될 메모리보다 크게 할당되는 경우가 존재
  - 연결리스트: 메모리의 동적할당을 기반으로 구현된 리스트
    - 물리적인 순서를 맞추기 위한 작업이 필요하지 않음
    - 효율적인 메모리 사용

### 02. 단순 연결 리스트(Singly Linked List)

<img src="images/image 027.png">

- 헤드가 가장 앞의 노드를 가리키고, 노드의 링크 필드가 연속적으로 다음 노드를 가리킴
- 최종적으로 NULL을 가리키는 노드가 리스트의 가장 마지막 노드

#### 1) 삽입연산

```
1) 메모리를 할당하여 새로운 노드 생성
2) 새로운 노드의 데이터 필드에 데이터 저장
3) 삽입될 위치의 바로 앞에 위치한 노드의 링크 필드를 새로운 노드에 복사
4) 새로운 노드의 주소를 앞 노드의 링크 필드에 저장
```

- 코드

  ```python
  class Node:
      def __init__(self,data,link):
          self.data=data
          self.link=link
  
  # 첫번째 노드로 삽입
  def addtoFirst(data):
  	global Head
      Head=Node(data,Head)
  
  # 가운데 노드로 삽입
  def add(pre,data):
      if pre==None:
          print('error')
      else:
          pre.link=Node(data,pre.link)
  
  # 마지막 노드로 삽입
  def addtoLast(data): # 마지막에 데이터 삽입
      global Head
      if Head==None: # 빈 리스트이면
          Head=Node(data,None)
      else:
          p=Head
          while p.link!=None: # 마지막 노드 찾을 때까지
              p=p.link
          p.link=Node(data,None)
  ```

  

#### 2) 삭제연산

```
1) 삭제할 노드의 앞 노드(선행노드) 탐색
2) 삭제할 노드의 링크 필드를 선행노드의 링크 필드에 복사
```

- 코드

  ```python
  def delete(pre):
      if pre==None or pre.link==None:
          print('error')
      else:
          pre.link=pre.link.link
  ```

  

### 3. 이중 연결 리스트(Doubly Linked List)

<img src="images/image 028.png">

- 양쪽 방향으로 순회할 수 있도록 노드를 연결한 리스트
- 두 개의 링크 필드와 한 개의 데이터 필드로 구성

#### 1) 삽입연산

<img src="images/image 029.png">

```
1) 메모리를 할당하여 새로운 노드를 생성하고 데이터 필드에 데이터를 저장
2) 삽입될 위치의 바로 앞에 위치한 노드의 오른쪽 링크 필드를 새로운 노드의 오른쪽 링크 필드에 복사, 그 반대로 삽입될 위치의 뒤에 위치한 노드의 왼쪽 링크 필드에 새로운 노드와 연결
3) 새로운 노드의 왼쪽 링크 필드에 삽입될 위치의 바로 앞에 위치한 노드와 연결, 삽입될 위치의 바로 앞에 위치한 노드의 오른쪽 링크 필드에 새로운 노드와 연결
```

#### 2) 삭제연산

<img src="images/image 030.png">

```
1) 삭제할 노드의 오른쪽 노드의 주소를 삭제할 노드의 왼쪽 노드의 오른쪽 링크 필드에 복사, 그 반대로 삭제할 왼쪽 노드의 주소를 삭제할 노드의 오른쪽 노드의 왼쪽 링크 필드에 복사
```



### 04. 삽입 정렬(Insertion Sort)

- 정렬 과정
  - 정렬되지 않은 부분집합 U의 원소를 하나씩 꺼내서 이미 정렬되어있는 부분집합 S의 마지막 원소부터 비교하면서 위치를 찾아 삽입함
  - 삽입정렬을 반복하면서 부분집합 S의 원소는 하나씩 늘리고 부분집합 U의 원소는 하나씩 감소하게 함, 부분집합 U가 공집합이 되면 삽입정렬이 완성
- 시간 복잡도
  - O(n^2)



### 05. 병합 정렬(Merge Sort)

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘 활용
  - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
  - top-down 방식
- 시간 복잡도

  - O(nlogn)

- 코드

  ```python
  def merge(left,right):
      result=[]
      while len(left)>0 and len(right)>0:
          # append로 하는 것 보다 index로 값을 넣는 것이 더 빠르다.
          if left[0]<=right[0]:
              result.append(left.pop(0))
          else:
              result.append(right.pop(0))
      if len(left)>0:
          result.extend(left)
      if len(right)>0:
          result.extend(right)
      return result
  
  def merge_sort(m):
      if len(m)<=1:
          return m
      mid=len(m)//2
      left=m[:mid]
      right=m[mid:]
      left=merge_sort(left)
      right=merge_sort(right)
      return merge(left,right)
  ```



### 06. 리스트를 이용한 스택

<img src="images/image 031.png">

- 스택 내의 순서는 리스트의 링크를 통해 연결됨
- 초기 상태에서 top=Null
- 


## 트리(Tree)

### 01. 트리의 개념

- 비선형 구조
  - 원소들 간에 1:n 관계를 가지는 자료구조
  - 원소들 간에 계층관계를 가지는 계층형 자료구조
  - 상위 원소에서 하위 원소로 내려가면서 확장되는 나무모양의 구조

- 한 개 이상의 노드로 이루어진 유한 집합
  - 노드 중 최상위 노드를 루트(root)라 함
  - 나머지 노드들은 n(>=0)개의 분리집합 T1,...,TN으로 분리될 수 있으며 이를 subtree라 함

    

### 02. 이진 트리(Binary Tree)

- 모든 노드들이 최대 2개의 서브트리를 갖는 특별한 형태의 트리
- 특성
  - 레벨 i에서의 노드의 최대 개수는 2^i개
  - 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1)개가 되며, 최대 개수는 (2^(h+1)-1)개

#### 1) 포화 이진 트리(Full Binary Tree)

<img src="images/image 012.png">

- 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
- 높이가 h일 때, 최대의 노드 개수인 (2^(h+1)-1)의 노드를 가진 이진 트리
  - 높이 3일 때 2^(3+1)-1=15개의 노드
- 루트를 1번으로 하여 2^(h+1)-1까지 정해진 위치에 대한 노드 번호를 가짐

#### 2) 완전 이진 트리(Complete Binary Tree)

<img src="images/image 013.png">

- 높이가 h이고 노드 수가 n개 일 때 (단, h+1<=n<2^(h+1)-1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리

#### 3) 편향 이진 트리(Skewed Binary Tree)

<img src="images/image 014.png">

- 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리
  - 왼쪽 편향 이진 트리
  - 오른쪽 편향 이진 트리

#### 4) 수식 이진 트리(Expression Binary Tree)

<img src="images/image 018.png">

- 수식을 표현하는 이진 트리
- 연산자는 루트 노드이거나 가지 노드
- 피연산자는 모두 잎 노드
- 순회의 종류에 따라 전위, 후위, 중위 표기법을 표현할 수 있음



### 03. 순회(Traversal)

<img src="images/image 015.png">

- 트리의 노드들을 체계적으로 방문하는 것

- 전위순회(preorder traversal):VLR

  - 코드

    ```python
    def preorder_traverse(node):
        if node:
            visit(node)
            preorder_traverse(node.left)
            preorder_traverse(node.right)
    ```

- 중위순회(inorder traversal):LVR

  - 코드

    ```python
    def inorder_traverse(node):
        if node:
            inorder_traverse(node.left)
            visit(node)
            inorder_traverse(node.right)
    ```

- 후위순회(postorder traversal):LRV

  - 코드

    ```python
    def postorder_traverse(node):
        if node:
            postorder_traverse(node.left)
            postorder_traverse(node.right)
            visit(node)
    ```



### 04. 이진트리의 표현

#### 1) 배열

<img src="images/image 016.png">

- 루트의 번호를 1로 함
- 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2^n부터 2^n-1 까지 번호를 차례로 부여

- 노드 번호를 배열의 인덱스로 사용
- 높이가 h인 이진 트리를 위한 배열의 크기는 2^(h+1)-1
- 단점
  - 메모리 공간 낭비 발생
  - 노드 삽입 또는 노드 삭제를 할 시 배열의 크기 변경이 어려움

#### 2) 연결리스트

<img src="images/image 017.png">

- `left`, `data`, `right`로 노드를 구성하여 단순 연결 리스트 구현



### 05. 이진탐색트리

<img src="images/image 019.png">

- 탐색작업을 효율적으로 하기 위한 자료구조
- 모든 원소는 서로 다른 유일한 키를 갖음
- 왼쪽 서브트리의 key < 루트 노드의 key < 오른쪽 서브트리의  key
- 왼쪽 서브트리와 오른쪽 서브트리도 이진 탐색 트리
- 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있음

#### 1) 탐색연산

<img src="images/image 020.png">

- 루트에서 시작
- 탐색할 키 값 x를 루트 노드의 키 값과 비교
  - (x==루트 노드의 키 값)인 경우 : 원하는 원소를 찾았으므로 성공
  - (x<루트 노드의 키 값)인 경우 : 루트 노드의 왼쪽 서브트리에 대해서 탐색연산 수행
  - (x>루트 노드의 키 값)인 경우 :  루트 노드의 오른쪽 서브트리에 대해서 탐색연산 수행
- 서브트리에 대해서 순환적으로 탐색 연산을 반복

#### 2) 삽입연산

<img src="images/image 021.png">

- 먼저 탐색 연산을 수행
  - 삽입할 원소와 같은 원소가 트리에 있으면 삽입할 수 없으므로, 같은 원소가 트리에 있는지 탐색하여 확인
  - 탐색에서 탐색 실패가 결정되는 위치가 삽입 위치
- 탐색 실패한 위치에 원소를 삽입

#### 3) 삭제연산

- 먼저 탐색 연산을 수행

- 세 가지 경우에 대해 각각 고려하여 수행

  - 삭제하려는 노드가 단말노드일 경우 (자식 노드가 없을 경우)

    - 부모 노드를 찾아서 부모 노드 안의 해당 링크 필드를 NULL로 만들어서 끊어줌

  - 삭제하려는 노드가 하나의 서브트리만 가지는 경우 (왼쪽 혹은 오른쪽 둘 중 하나만)

    - 삭제하려는 노드의 부모가 서브트리의 루트 노드를 대신에 가리키게 만듬

  - 삭제하려는 노드가 두 개의 서브트리를 모두 가지고 있는 경우

    - 왼쪽 서브트리에 있는 값 중 가장 큰 값, 혹은 오른쪽 서브트리에 있는 값 중 가장 작은 값을 가지고 있는 노드를 연결시킴

    

### 06. 힙(heap)

- 완전 이진 트리에 있는 노드 중에서 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위해서 만든 자료구조
- 힙의 키를 우선순위로 활용하여 우선순위 큐를 구현할 수 있음

<img src="images/image 022.png">

- 최대 힙(max heap)

  - 키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리
  - 부모 노드의 키 값 > 자식 노드의 키 값
  - 루트 노드 : 키 값이 가장 큰 노드

- 최소 힙(min heap)

  - 키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리
  - 부모 노드의 키 값 < 자식 노드의 키 값
  - 루트 노드 : 키 값이 가장 작은 노드

#### 1) 삽입

<img src="images/image 023.png">

#### 2) 삭제

<img src="images/image 024.png">

- 루트 노드의 원소만 삭제 가능
- 루트 노드의 원소를 삭제하여 반환
- 힙의 종류에 따라 최대값 또는 최소값을 구하거나 오름차순, 내림차순 정렬을 구현할 수 있음

