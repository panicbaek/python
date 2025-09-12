import requests
from bs4 import BeautifulSoup

keyword = input("검색:")

def blog_crwaling(page, keyword):
  response = requests.get(f'https://search.naver.com/search.naver?sm=tab_hty.top&ssc=tab.blog.all&query={keyword}&start={page}')
  soup = BeautifulSoup(response.content, 'html.parser')
  
  for i in range(30):
    print(f"{page + i}번째 블로그 제목 : {soup.select('.title_link')[i].text}")

blog_crwaling(1, keyword)