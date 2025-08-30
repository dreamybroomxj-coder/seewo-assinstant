from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pyautogui
import pyperclip
import ctypes


driver = webdriver.Chrome()

# 访问页面
url = "https://chat2.jinshutuan.com/#/chat/1685926698700"
driver.get(url)

def ask_ai(ques):
    time.sleep(5)
    pyautogui.click(533,943, clicks=1, interval=0.25, button='left')
    time.sleep(1)
    pyperclip.copy(ques)

    # 模拟按下Ctrl+V组合键将文本粘贴到输入框中
    pyautogui.hotkey('ctrl', 'v')
    # 模拟键盘按键Enter
    pyautogui.press('enter')
    time.sleep(10)
    #清空剪贴板
    ctypes.windll.user32.OpenClipboard(None)
    ctypes.windll.user32.EmptyClipboard()
    ctypes.windll.user32.CloseClipboard()
    # 获取最后一个 <div class="markdown-body"> 标签的文本内容
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    divs = soup.find_all('div', class_='markdown-body')
    last_div_text = divs[-1].get_text()
    return(last_div_text)

for i in range(3):
    print(ask_ai("你好"))