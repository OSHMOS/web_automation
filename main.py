'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
import requests
from bs4 import BeautifulSoup

url = f'https://workey.codeit.kr/ratings/index'
response = requests.get(url)
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

tr_tag = soup.select('tr')[1]
# td_tags = tr_tag.select('td')
td_tags = tr_tag.select('*')
print(td_tags)
for tag in td_tags:
    print(tag.get_text())
