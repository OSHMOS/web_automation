import requests
from bs4 import BeautifulSoup

# 여기에 코드를 작성하세요
url = 'https://workey.codeit.kr/orangebottle/index'
response = requests.get(url)
orangebottle = response.text

soup = BeautifulSoup(orangebottle, 'html.parser')
branch_infos = []
branch_tag = soup.select('div.branch')[0]
branch_name = branch_tag.select('p.city')
branch_address = branch_tag.select('p.address')
branch_phoneNum = branch_tag.select('span.phoneNum')
# select는 list 형식을 반환해서 get_text() 함수를 사용할 수 없다.
print(branch_name.get_text())
