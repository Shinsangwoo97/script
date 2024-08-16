# pip install selenium webdriver-manager


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 특정 키워드 설정
keyword = "Python 프로그래밍"  # 검색할 키워드로 변경

# Chrome 브라우저 열기
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 네이버 웹사이트 열기
driver.get("https://www.naver.com")

# 검색창 찾기
search_box = driver.find_element(By.NAME, "query")  # 네이버의 검색창 이름

# 검색어 입력
search_box.send_keys(keyword)
search_box.send_keys(Keys.RETURN)  # Enter 키를 눌러 검색 실행

# 검색 결과가 로드될 때까지 잠시 대기
time.sleep(5)

# 브라우저 종료
driver.quit()
