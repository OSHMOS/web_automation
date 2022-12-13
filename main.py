'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
# Selenium 임포트
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# scrap 작업 후에 브라우저 닫기 가능
# driver.quit()
