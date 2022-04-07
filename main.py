'''
파이썬으로 서버에게 요청 보내고 응답 확인하기
'''
import requests

response = requests.get('https://google.com')
print(response)
print(response.text)