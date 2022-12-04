'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)  # 엄청 많은 데이터를 다룰 때는 write_only 필수
ws = wb.create_sheet('TV Ratings')  # 워크시트 생성
ws.append(['순위', '채널', '프로그램', '시청률'])  # 행 추가

url = 'https://workey.codeit.kr/ratings/index'
response = requests.get(url)
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')
for tr_tag in soup.select('tr')[1:]:
    td_tags = tr_tag.select('td')
    row = [
        td_tags[0].get_text(),  # 순위
        td_tags[1].get_text(),  # 채널
        td_tags[2].get_text(),  # 프로그램
        td_tags[3].get_text(),  # 시청률
    ]
    ws.append(row)

wb.save('시청률_2010년1월1주차.xlsx')  # 워크북 저장
