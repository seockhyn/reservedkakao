import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
client_id = 'c215564dd1ad80a0e8aadf1a7892f041'
redirect_uri = 'https://example.com/oauth'
code = 'xd11F3HGEVrnnJcd09Kc8YKbqWRvXtkr04EpvVzfTis5THVeTez_M310bNoKKiWQAAABjBjbtkut1856Xp2T3g'

data = {
    'grant_type':'authorization_code',
    'client_id':client_id,
    'redirect_uri':redirect_uri,
    'code': code,
    }

response = requests.post(url, data=data, verify=False)
tokens = response.json()

#발행된 토큰 저장
with open("token.json","w") as kakao:
    json.dump(tokens, kakao)