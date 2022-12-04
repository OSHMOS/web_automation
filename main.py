'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
import requests
from bs4 import BeautifulSoup

url = 'https://workey.codeit.kr/ratings/index'
response = requests.get(url)
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

print(soup.select_one('img')['src'])  # 해당 속성만
print(soup.select_one('img').attrs)  # 해당 태그의 모든 속성
