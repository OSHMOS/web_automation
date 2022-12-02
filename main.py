'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
import requests
from bs4 import BeautifulSoup

url = f'https://workey.codeit.kr/music'
response = requests.get(url)
music_page = response.text

soup = BeautifulSoup(music_page, 'html.parser')

popular_artists = []

# for tag in soup.select('ul.popular__order li'):
# popular_artists.append(tag.get_text().strip())

for tag in soup.select('ul.popular__order li'):
    # print(list(tag.strings))
    # print(list(tag.stripped_strings))
    # print(list(tag.stripped_strings)[1])
    popular_artists.append(list(tag.stripped_strings)[1])

print(popular_artists)
