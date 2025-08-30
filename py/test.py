import pyautogui
import pyperclip
import time

# 设置待检测像素点位置和目标点击位置


pyperclip.copy("哦")

# 循环检测像素点颜色
while True:
    # 获取指定位置的像素颜色
    color = pyautogui.pixel(646,153)

    # 如果像素颜色不是白色则点击目标位置
    if color[1]<200 and color[2]<200:
        pyautogui.click(769,178, clicks=1, interval=0.25, button='left')
        time.sleep(0.5)
        pyautogui.click(769,236, clicks=1, interval=0.25, button='left')
        time.sleep(0.5)
        pyautogui.click(1544,814, clicks=1, interval=0.25, button='left')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        # 模拟键盘按键Enter
        pyautogui.press('enter')
        pyautogui.click(1490,151, clicks=1, interval=0.25, button='left')
        time.sleep(0.5)
        pyautogui.click(1530,387, clicks=1, interval=0.25, button='left')
        
    # 暂停一段时间后再次循环检测
    time.sleep(20)