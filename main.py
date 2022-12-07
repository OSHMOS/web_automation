'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
# Selenium 임포트
import time
from selenium import webdriver

# 크롬 드라이버 생성
driver = webdriver.Chrome()
driver.implicitly_wait(3)  # 최대 3초를 기다려준다. # 전체 코드에 계속 적용된다. # 상호작용에 영향 X

# 사이트 접속하기
driver.get('https://workey.codeit.kr/costagram/index')
time.sleep(1)  # 길게 설정하는만큼 실행 시간도 늘어난다. # 넣기 좋은 위치는 웹 페이지가 변할 때이다.

# 로그인 클릭
driver.find_element_by_css_selector('.top-nav__login-link').click()
time.sleep(1)

# 아이디와 비밀번호 입력
driver.find_element_by_css_selector(
    '.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector(
    '.login-container__password-input').send_keys('datascience')

# 로그인 시도
driver.find_element_by_css_selector('.login-container__login-button').click()

# 로그아웃 시도
# driver.find_element_by_css_selector('.top-nav__login-link').click()

# 크롬 드라이버 종료, 다 사용했으면 종료하는 것이 좋습니다!
# driver.quit()
