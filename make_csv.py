# pip install pandas

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 장소 목록을 CSV 파일에서 읽어오기
places_df = pd.read_csv('places.csv')
places = places_df['Place'].tolist()

# 검색 결과를 저장할 리스트
results = []

# Chrome 브라우저 열기
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 네이버 웹사이트 열기
driver.get("https://www.naver.com")

for place in places:
    # 검색창 찾기
    search_box = driver.find_element(By.NAME, "query")
    
    # 검색어 입력
    search_box.clear()  # 이전 검색어를 지웁니다.
    search_box.send_keys(place)
    search_box.send_keys(Keys.RETURN)  # Enter 키를 눌러 검색 실행
    
    # 검색 결과가 로드될 때까지 잠시 대기
    time.sleep(5)
    
    # 결과 페이지에서 정보 추출
    # 예를 들어, 뉴스 검색 결과의 제목과 링크를 가져올 수 있습니다.
    search_results = driver.find_elements(By.CSS_SELECTOR, 'ul.list_news > li > div > a')
    
    for result in search_results:
        title = result.text
        link = result.get_attribute('href')
        results.append({'Place': place, 'Title': title, 'Link': link})
    
    # 다음 장소 검색을 위해 잠시 대기
    time.sleep(2)

# 브라우저 종료
driver.quit()

# 결과를 데이터프레임으로 변환
results_df = pd.DataFrame(results)

# CSV 파일로 저장
results_df.to_csv('search_results.csv', index=False, encoding='utf-8-sig')
