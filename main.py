'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
import requests
from bs4 import BeautifulSoup
import csv

# csv 파일 생성
csv_file = open('시청률_2010년1월1주차.csv', 'w')
csv_writer = csv.writer(csv_file)

# 행 추가
csv_writer.writerow(['순위', '채널', '프로그램', '시청률'])

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
    # 데이터 행 추가
    csv_writer.writerow(row)

# csv 파일 닫기
csv_file.close()
