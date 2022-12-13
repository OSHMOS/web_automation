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

driver.execute_script('window.scrollTo(0, 200);')

scroll_height = driver.execute_script('return document.body.scrollHeight')
print(scroll_height)
# scrap 작업 후에 브라우저 닫기 가능
# driver.quit()
