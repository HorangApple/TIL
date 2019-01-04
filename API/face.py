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
# 2. 파일데이터를 받아 저장한다.
image_url = "https://pds.joins.com/news/component/htmlphoto_mmdata/201704/20/1115bcf3-0ed8-4ec7-89b4-728c4df65434.jpg"

image_res = requests.get(image_url, stream = True) # 파일 스트림에서 가져오기위해 steam = True로 설정한다.

files = {
    'image': image_res.raw.read() # python에서 파일을 열 때 사용하는 함수, read binary
}

res = requests.post(url, headers=headers, files=files)
jres = res.json() # json => dictionary

for i in jres.get('faces'):
    print("{}% 확률로 {}입니다.".format(round(100*i.get('celebrity').get('confidence')),\
    i.get('celebrity').get('value')))