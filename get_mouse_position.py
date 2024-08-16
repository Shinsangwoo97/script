# pip install pyautogui

import pyautogui

# 현재 마우스 포인터의 위치를 출력하는 코드
while True:
    x, y = pyautogui.position()
    print(f"현재 좌표: ({x}, {y})")
    pyautogui.sleep(1)  # 1초마다 좌표 출력
