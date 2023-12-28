import requests
import json

# 발행한 토큰 불러오기
with open("token.json", "r") as kakao:
    tokens = json.load(kakao)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {
    "Authorization": "Bearer " + tokens["access_token"]
}

data = {
    'object_type': 'text',
    'text': '테스트입니다',
    'link': {
        #'web_url': 'https://developers.kakao.com',
        #'mobile_web_url': 'https://developers.kakao.com'
    },
    'button_title': '키워드'
}

data = {'template_object': json.dumps(data)}
response = requests.post(url, headers=headers, data=data, verify=False)
print(response)
print(response.text)

url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 목록 가져오기
header = {"Authorization": 'Bearer ' + tokens["access_token"]}
result = json.loads(requests.get(url, headers=header, verify=False).text)
friends_list = result.get("elements")
print(friends_list)