# Batch Script 

*hello.py*

```python
# 자동화할 기능들을 파이썬으로 구현
import webbrowser
url = "https://search.naver.com/search.naver?&query=미세먼지"
webbrowser.open(url)
```

네이버에 미세먼지를 검색하게 만드는 코드이다. 이 파일을 실행시키는 방법은 다음과 같다.



1) bash

```bash
$ python 파일명.py
```

bash에서 위와 같이 입력하면 실행이 된다.



2) 윈도우 run
`윈도우키+R`을 누르고 다음을 입력하여 실행시킨다.
`python c:\Users/student/scripts/hello.py`



3) 윈도우 batch script 
`파일명.bat`을 생성해 다음과 같이 입력한다.

*hello.bat*

```
:: 윈도우즈 명령어 모음
:: 1. python 파이썬
:: 2. 잠시 멈춰라
:: 윈도우즈 커맨드들을 모아서 한꺼번에 실행해주는 스크립트
:: @를 입력하면 해당 코드와 관련된 출력이 가려짐

@python c:\Users/student/scripts/hello.py %*
:: %*는 args로 python 파일에 넘겨줄 수 있게 해준다.
@pause
```

<img src = "images/image 002.png">

*위는 `@`를 붙이지 않았을 때, 아래는 `@`를 붙였을 때

이후 `윈도우키+R`을 누르고 batch 파일 위치를 실행시키면 된다.

`C:\Users\student\scripts\hello.bat`

이 batch 파일을 간단하게 실행시키기 위해 환경변수를 설정해보자

`시스템-> 고급시스템설정-> 고급-> 환경변수`

여기서 `시스템 변수`에 있는 `Path`에 batch 파일이 있는 폴더 경로를 추가한다

<img src = "images/image 001.png">

그러면 이제 `윈도우키+R` 누르고 batch 파일명인 `hello`만 입력해도 실행되는 것을 볼 수 있다.

<img src = "images/image 003.png">

cf) 주석을 위 코드처럼 최상단에 달면 커맨드 창에 글씨가 깨져서 출력되고 실행되는 것을 볼 수 있다.

*hello.py*

```python
# 자동화할 기능들을 파이썬으로 구현
import webbrowser
import sys
keyword = sys.argv[1]
url = "https://search.naver.com/search.naver?&query={}".format(keyword)
webbrowser.open(url)

# sys.argv 우리가 입력한 명령어들이 다 들어가 있음
# => 'hello 미세먼지'를 입력하면
# => sys.argv는 ["hello 파일 경로", "미세먼지"]와 같이 리스트 형식으로 초기화 된다.
```

실행 창에 `hello 미세먼지`를 입력하여 실행시키면 바로 네이버에 미세먼지를 검색한 페이지가 실행된다.

