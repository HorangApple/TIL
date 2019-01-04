# API (Application Programming Interface)

## 네이버 파파고

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

## 네이버 얼굴 인식

'papago.py'와 구조가 유사하다.
https://developers.naver.com/docs/clova/api/CFR/API_Guide.md#UsingAPI

```python
# 인식시킬 사진을 clova API를 통해 요청을 보내, 인식 결과를 받아온다.
# req(파일)

# 1. requests를 통해 clova API 주소에 요청을 보낸다.
# 2. 응답 받은 json을 파싱하여 원하는 결과를 출력한다.

import requests
from pprint import pprint as pp

naver_id = "값"
naver_secret = "값"

url = "https://openapi.naver.com/v1/vision/celebrity"
headers = {
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_secret
}

# 1. 해당하는 image_url에 요청을 보내서
image_url = "이미지 주소"
# 2. 파일데이터를 받아 저장한다.
image_res = requests.get(image_url, stream = True) # 파일 스트림에서 가져오기위해 steam = True로 설정한다.

files = {
    'image': image_res.raw.read() # python에서 파일을 열 때 사용하는 함수, read binary
}

res = requests.post(url, headers=headers, files=files)
jres = res.json() # json => dictionary

for i in jres.get('faces'):
    print("{}% 확률로 {}입니다.".format(round(100*i.get('celebrity').get('confidence')),\
    i.get('celebrity').get('value')))

```

python에서 하위 메소드의 목록을 보고 싶으면 `dir('알아보고 싶은 것')`을 입력한다.
```python
>>> dir("hello")
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
'__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith',
'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

예를 들어 여기서 `"hello".capitalize()`를 입력하면 `Hello`로 출력시켜주는 첫 글자를 대문자로 만들어주는 메소드이다. 
반면에 `'__XXX__'`식으로 되어 있는 것은 함수이다. 예를 들면 `sizeof(변수)` 를 입력하면 변수에 대한 용량을 확인할 수 있다.

```python
print(dir(image_res))

['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 
'__weakref__', '_content', '_content_consumed', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding',
'headers', 'history', 'iter_content', 'iter_lines', 'json', 'links', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 
'status_code', 'text', 'url']
```

```python
print(dir(image_res.raw))

['CONTENT_DECODERS', 'REDIRECT_STATUSES', '__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', 
'__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__iter__', 
'__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', 
'_body', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_connection', '_decoder', '_fp', '_original_response', 
'_pool', 'close', 'closed', 'data', 'decode_content', 'fileno', 'flush', 'from_httplib', 'get_redirect_location', 'getheader', 
'getheaders', 'headers', 'isatty', 'read', 'readable', 'readline', 'readlines', 'reason', 'release_conn', 'seek', 'seekable', 'status', 
'stream', 'strict', 'tell', 'truncate', 'version', 'writable', 'writelines']
```

이런식으로 생소한 값을 `dir`를 통해 단계적으로 접근한다. 그래서 결과적으로 `image_res.raw.read()` 를 통해 이미지 url을 요청하여 파일을 변수에 담아 POST로 보낼 수 있다.

