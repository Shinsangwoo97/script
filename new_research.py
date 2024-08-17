# pip install selenium pandas

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
time.sleep(3)

# 검색 결과 가져오기
# 검색 결과는 보통 네이버 블로그나 카페, 웹사이트 링크로 제공됩니다.
results = driver.find_elements(By.CSS_SELECTOR, '.lst_total .total_tit')

# 결과 저장을 위한 리스트 초기화
data = []

# 결과 파싱
for result in results:
    title = result.text
    link = result.get_attribute('href')
    data.append({'title': title, 'link': link})

# 데이터프레임으로 변환
df = pd.DataFrame(data)

# CSV 파일로 저장
df.to_csv('naver_search_results.csv', index=False, encoding='utf-8-sig')

# 브라우저 종료
driver.quit()

print("CSV 파일로 저장이 완료되었습니다.")
