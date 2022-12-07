'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
# Selenium 임포트
from selenium import webdriver

# 크롬 드라이버 생성
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 사이트 접속하기
driver.get('https://workey.codeit.kr/costagram/index')

# 로그인 클릭
driver.find_element_by_css_selector('.top-nav__login-link').click()

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
