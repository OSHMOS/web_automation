'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
import requests
from bs4 import BeautifulSoup

url = f'https://workey.codeit.kr/ratings/index'
response = requests.get(url)
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

# select => 리스트 형식으로 출력
program_title_tags = soup.select('td.program')

program_titles = []
for tag in program_title_tags:
    program_titles.append(tag.get_text())

print(program_title_tags)

print(program_titles)

# select_one => 리스트 중 첫 번째 요소를 출력
print(soup.select_one('td.program'))
