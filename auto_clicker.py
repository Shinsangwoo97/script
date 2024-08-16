# pip install keyboard
# pip install pyautogui


import pyautogui
import time
import keyboard  # 키보드 입력을 감지하기 위해 추가

# 특정 위치 (x, y) 좌표 설정
x, y = 100, 200  # 원하는 위치의 x, y 좌표로 변경

# 무한 루프를 통해 클릭 수행, 'q' 키를 누르면 중지
while True:
    if keyboard.is_pressed('q'):  # 'q' 키가 눌리면 루프 종료
        print("스크립트가 종료되었습니다.")
        break
    pyautogui.click(x, y)  # 설정된 좌표 클릭
    print(f"Clicked at ({x}, {y})")
    time.sleep(0.01)  # 0.01초 대기
