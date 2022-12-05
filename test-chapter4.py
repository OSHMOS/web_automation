'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet()
ws.append(['기간', '순위', '프로그램', '시청률'])
for year in range(2010, 2019):
    for month in range(1, 13):
        for weekIndex in range(0, 5):
            url = 'https://workey.codeit.kr/ratings/index?year=2011&month=1&weekIndex=0'
            response = requests.get(url)
            rating_page = response.text
            soup = BeautifulSoup(rating_page, 'html.parser')

            for tr_tag in soup.select('tr')[1:]:  # [1:] 덕분에 빈 테이블 걸러짐. 이런 식으로
                td_tags = tr_tag.select('td')
                if td_tags[1].get_text() == 'SBS':
                    period = f'{year}년 {month}월 {weekIndex + 1}주차'
                    row = [
                        period,
                        td_tags[0].get_text(),  # 순위
                        td_tags[2].get_text(),  # 프로그램
                        td_tags[3].get_text(),  # 시청률
                    ]
                    ws.append(row)
wb.save('SBS_데이터.xlsx')
