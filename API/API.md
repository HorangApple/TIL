## API (Application Programming Interface)

요즘 회원가입을 하여 Key를 발급 받고 API를 사용하는 식으로 사용하게 된다.

c9에서 share버튼을 눌러 Application 주소를 이용해 네이버 api 등록을 한다.

c9에서 requests 모듈을 설치하고 파이썬 코드를 작성한다.

```python
# 네이버(파파고)야 내가 단어하나 전달할테니, 번역해줘

# 0. 사용자에게 단어를 입력 받는다.
# 1. papago API 요청 주소에 요청을 보낸다.
# 2. 응답을 받아 번역된 단어를 출력한다.

import requests
from pprint import pprint as pp

# 다음과 같이 함수명을 줄여나갈 수 있다.
# import pprint => pprint.pprint()
# from pprint import pprint => pprint()
# from pprint import pprint as pp => pp()

keyword = input("Please type any english word or phrase : ")
naver_id = "값"
naver_secret = "값"

url = "https://openapi.naver.com/v1/papago/n2mt"
headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_secret
}

data ={
    'source' : 'en',
    'target' : 'ko',
    'text' : keyword
}

res = requests.post(url, headers=headers, data=data)

result = res.json()

pp(result["message"]["result"]["translatedText"]) # 값이 없으면 에러 발생
# pp(result.get('message').get('result').get('translatedText')) # 값이 없으면 NULL 출력
```
<img src = "images/image 002.png">
pprint는 print와 다르게 json을 이쁘게 출력해준다. (위 pprint, 아래 print)

파파고 개발 문서 : https://developers.naver.com/docs/nmt/reference/

<img src = "images/image 011.png">
네이버에게 발급받은 키를 네이버에 전송하여야 한다. 이를 `headers`라는 변수에 딕셔너리 형태로 담는다.
<img src = "images/image 012.png">

마찬가지로 요청할 데이터를 보내기 위해 `data`라는 변수에 위의 `source, target, text`를 딕셔너리 형태로 담는다.



<img src = "images/image 013.png">
GET 방식은 정보를 가져올 때 사용하는 방식이고 POST는 정보를 입력, 게시할 때 사용하는 방식이다. 파파고를 이용하는 방식은 그림과 같이 작동이 되는데 여기서 POST 방식으로 요청이 간다.  키 값이나 번역할 단어 등의 데이터를 전하고 응답을 받아야하기 때문에 POST를 사용하게 되었다.
