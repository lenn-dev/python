# replit
# beautifulsoup 4 download (screen scraping library)
# https://www.crummy.com/software/BeautifulSoup/bs3/
# install requests
import requests
# 설치명령어 : sudo pip3 install beautifulsoup4 입력
# from bs4 import BeautifulSoup
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", bs4])

from bs4 import BeautifulSoup
# ctrl + 클릭하면 해당 패키지 내장함수의 코드 파일로 이동함
# BeautifulShop은 class 로 이루어짐

# url 주소는 ""로 감쌀것
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

response = requests.get(url)

print(response.content)# 웹페이지 소스코트 나옴 => 데이터가 html과 섞여있음

# beautifulsoup4 패키지 사용하면 이 html에서 원하는 것을 검색할 수 있게됨
# requests로 받은 content로 beautifulsoup을 initialize 해보자
# 첫번째 인자: 데이터 주고, 두번째인자 : 데이터포맷 (다른 format에서도 작동하기 때문에 문서타입 지정해줘야함)
soup = BeautifulSoup(
    response.content,
    "html.parser",
)