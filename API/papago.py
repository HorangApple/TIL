# 네이버(파파고)야 내가 단어하나 전달할테니, 번역해줘

# 0. 사용자에게 단어를 입력 받는다.
# 1. papago API 요청 주소에 요청을 보낸다.
# 2. 응답을 받아 번역된 단어를 출력한다.

import requests
from pprint import pprint as pp


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