import requests

### 코드를 작성하세요 ###
response = requests.get('https://workey.codeit.kr/ratings/index')
rating_page = response.text

# 출력 코드
print(rating_page)