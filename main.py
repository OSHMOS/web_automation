'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
# Selenium 임포트
from selenium import webdriver

# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 사이트 접속하기
driver.get('https://codeit.kr')

# 크롬 드라이버 종료, 다 사용했으면 종료하는 것이 좋습니다!
driver.quit()
