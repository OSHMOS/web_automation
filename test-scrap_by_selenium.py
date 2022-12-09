import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://workey.codeit.kr/orangebottle/index')
time.sleep(2)

branch_infos = []
for branch_tag in driver.find_elements_by_css_selector('div.branch'):
    branch_name = branch_tag.find_element_by_css_selector('p.city').text
    address = branch_tag.find_element_by_css_selector('p.address').text
    phone_number = branch_tag.find_element_by_css_selector(
        'span.phoneNum').text
    branch_infos.append([branch_name, address, phone_number])

# 테스트 코드
print(branch_infos)

driver.quit()
