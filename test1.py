from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time

# 웹드라이버 설정 (Chrome 드라이버를 사용하는 예시)
driver = webdriver.Chrome()

# 네이버로 이동
driver.get('https://www.naver.com')

# 검색창 찾기
search_box = driver.find_element(By.NAME, 'query')

# 검색어 입력 및 검색
search_keyword = '가볼만한 곳'
search_box.send_keys(search_keyword)
search_box.send_keys(Keys.RETURN)

# 잠시 대기 (페이지 로딩 시간)
time.sleep(2)

# 페이지의 모든 텍스트 데이터를 가져오기
page_text = driver.find_element(By.TAG_NAME, 'body').text

# 결과 저장을 위한 리스트 초기화
data = [{'content': page_text}]

# 데이터프레임으로 변환
df = pd.DataFrame(data)

# CSV 파일로 저장
df.to_csv('naver_search_all_data.csv', index=False, encoding='utf-8-sig')

# 브라우저 종료
driver.quit()

print("CSV 파일로 저장이 완료되었습니다.")
