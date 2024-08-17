# pip install selenium pandas

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time

# # 웹드라이버 설정 (Chrome 드라이버를 사용하는 예시)
# driver = webdriver.Chrome()

# # 네이버로 이동
# driver.get('https://www.naver.com')

# # 검색창 찾기
# search_box = driver.find_element(By.NAME, 'query')

# # 검색어 입력 및 검색
# search_keyword = '가볼만한 곳'
# search_box.send_keys(search_keyword)
# search_box.send_keys(Keys.RETURN)

# # 잠시 대기 (페이지 로딩 시간)
# time.sleep(2)

# # '플레이스' 탭 클릭
# place_tab = driver.find_element(By.LINK_TEXT, '플레이스')
# place_tab.click()

# # 잠시 대기 (플레이스 페이지 로딩 시간)
# time.sleep(2)

# # 플레이스 탭에서 장소 제목들 가져오기
# place_titles = driver.find_elements(By.CSS_SELECTOR, 'span.place_bluelink')

# # 결과 저장을 위한 리스트 초기화
# data = []

# # 결과 파싱
# for place in place_titles:
#     title = place.text
#     data.append({'title': title})

# # 데이터프레임으로 변환
# df = pd.DataFrame(data)

# # CSV 파일로 저장
# df.to_csv('naver_place_titles.csv', index=False, encoding='utf-8-sig')

# # 브라우저 종료
# # driver.quit()

# print("CSV 파일로 저장이 완료되었습니다.")

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

# '플레이스' 탭 클릭
place_tab = driver.find_element(By.LINK_TEXT, '플레이스')
place_tab.click()

# 잠시 대기 (플레이스 페이지 로딩 시간)
time.sleep(2)

# # 플레이스 탭에서 장소 제목들 가져오기
place_titles = driver.find_elements

# # 결과 저장을 위한 리스트 초기화
# data = []

# # 결과 파싱
# for place in place_titles:
#     title = place.text
#     data.append({'title': title})

# # 데이터프레임으로 변환
# df = pd.DataFrame(data)

# # CSV 파일로 저장
# df.to_csv('naver_place_titles.csv', index=False, encoding='utf-8-sig')

# # 브라우저 종료
# driver.quit()

print("CSV 파일로 저장이 완료되었습니다.")

