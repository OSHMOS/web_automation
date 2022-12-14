'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
# Selenium 임포트
import time
from selenium import webdriver
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet('플레이 리스트')
ws.append(['제목', '해시태그', '좋아요 수', '곡 수'])

# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 사이트 접속하기
driver.get('https://workey.codeit.kr/music')
time.sleep(3)

# 현재 scrollHeight 가져오기
last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    # scrollHeight 스크롤
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    # 새로운 내용 로딩될 때까지 기다림
    time.sleep(0.5)

    # 새로운 내용 로딩 됐는지 확인
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

playlists = driver.find_elements_by_css_selector('div.playlist__meta')

for playlist in playlists:
    title = playlist.find_element_by_css_selector('h3.title').text
    hashtags = playlist.find_element_by_css_selector('p.tags').text
    like_count = playlist.find_element_by_css_selector(
        'span.data__like-count').text
    music_count = playlist.find_element_by_css_selector(
        'span.data__music-count').text
    ws.append([title, hashtags, like_count, music_count])

# scrap 작업 후에 브라우저 닫기 가능
driver.quit()
wb.save('플레이리스트_정보.xlsx')
