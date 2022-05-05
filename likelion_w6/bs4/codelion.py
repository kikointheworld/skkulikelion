# 크롤링: 크롤러를 사용해 웹 페이지의 데이터를 추출해주는 행위
# 크롤러:  를 도와주게 해주는~

# 크롤링 하기 위해서 외부 모듈 필요. 다른 사람이 만들어 놓은 기능을 사용하기 위해 우리 컴퓨터에서 설치해야함~

# 모듈 : 자주쓰는 함수를 모아두는 파일

import requests
from bs4 import BeautifulSoup # bs4라는 모듈에서 beautifulsoup을 이용하겠다. 
from datetime import datetime # 오늘 날짜 확인 가능

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# requests.get -> GET 요청을 보내는 기능

# requests.get(url)
# --> return : requests.response
url = "https://finance.naver.com/"

response = requests.get(url, headers = headers)
# response.text -> html코드 모두 볼 수 있음. / str타임임.

# Response [200] : 요청이 성공적으로 받아졌다는 것을 의미

# BeautifulSoup (데이터, 파싱방법)
# 데이터는 html과 xml이 올 수 있음.
# Parsing : 우리의 데이터를 의미있는 값으로 변환하는 것.

soup = BeautifulSoup(response.text, 'html.parser')
# file = open("daum.html", "w")
# file.write(response.text)
# file.close()


print(datetime.today().strftime("%Y년 %m월 %d일의 주식 인기 검색 종목 순위입니다.\n"))

tmp = soup.find('div', 'aside_popular')

results = tmp.findAll('a')
rank = 1

search_rank_file = open("rankresult.txt", "w")

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    if rank  == 5:
        break
    rank += 1
# print(soup.title)
# print(soup.title.string)
# print(soup.span)


# print(soup.findAll('a')) # 리스트 형태로 모든 스팬태그 뱉는다.

