# 주식정보 가져오기
import requests
from bs4 import BeautifulSoup
import urllib.request


code = (input("코드번호 입력란 : "))
response = requests.get(f'https://finance.naver.com/item/sise.naver?code={code}')

# print( response.content )
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
print(f"현재량 = {soup.find_all('strong', id='_nowVal')[0].text}")

# 속성값을 이용하더라도 동일한 속성을 가진 태그가 여러개면
# 정확하게 원하는 데이터만 추출하기가 힘들어짐
# print( soup.find_all('span', class_='tah p11')[0].text )

# css의 선택자를 이용해서 추출도 가능함
print( f"거래량 = {soup.select('#_quant')[0].text}")

img_url = soup.select('#img_chart_area')[0]['src']

urllib.request.urlretrieve(img_url, '하이닉스.png')

def select(code):
      response = requests.get(f'https://finance.naver.com/item/sise.naver?code={code}')
      soup = BeautifulSoup(response.content, 'html.parser')
      a = print(f"현재량 = {soup.find_all('strong', id='_nowVal')[0].text}")
      b = print( f"거래량 = {soup.select('#_quant')[0].text}")
      return a, b

f = open('주식정보.csv', 'w')
f.write('a\n b\n')
