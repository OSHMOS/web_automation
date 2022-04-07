'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
import requests

rating_pages = []
# https://workey.codeit.kr/ratings/index?year=2010&month=1%weekIndex={i}
for i in range(5):
    url = f'https://workey.codeit.kr/ratings/index?year=2010&month=1%weekIndex={i}'
    response = requests.get(url)
    rating_page = response.txt
    rating_pages.append(rating_page)

print(len(rating_pages))
print(rating_pages[0])