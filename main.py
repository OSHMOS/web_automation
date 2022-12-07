'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
# Selenium 임포트
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 크롬 드라이버 생성
driver = webdriver.Chrome()
# driver.implicitly_wait(3) explicitly wait와 함께 쓰는 것 권장 X

# 사이트 접속하기
driver.get('https://workey.codeit.kr/costagram/index')
time.sleep(3)  # 이 코드는 explicitly wait와 같이 써도 무방하다.

# 로그인 클릭
login_link = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.top-nav__login-link')))
login_link.click()

# 공통된 WebDriverWait
wait = WebDriverWait(driver, 3)

# 아이디와 비밀번호 입력
id_box = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '.login-container__login-input')))
id_box.send_keys('codeit')
pw_box = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '.login-container__password-input')))
pw_box.send_keys('datascience')

# 로그인 시도
login_button = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, '.login-container__login-button')))
login_button.click()

# 로그아웃 시도
# driver.find_element_by_css_selector('.top-nav__login-link').click()

# 크롬 드라이버 종료, 다 사용했으면 종료하는 것이 좋습니다!
# driver.quit()
