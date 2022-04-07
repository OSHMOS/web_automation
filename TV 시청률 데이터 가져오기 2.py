import requests

years = [2010, 2011, 2012]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
weeks = [0, 1, 2, 3, 4]
rating_pages = []
### 코드를 작성하세요 ###
for year in years:
    for month in months:
        for week in weeks:
            url = f'https://workey.codeit.kr/ratings/index?year={year}&month={month}&weekIndex={week}'
            response = requests.get(url)
            rating_page = response.text
            rating_pages.append(rating_page)
# 출력 코드
print(len(rating_pages)) # 가져온 총 페이지 수 
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드