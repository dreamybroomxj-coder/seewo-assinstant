import ctypes
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import pyautogui
import pyperclip

def init_driver():
    global driver
    driver = webdriver.Chrome()
    # 访问页面
    url = "https://c.binjie.fun/"
    driver.get(url)
    sleep(3)

def ask_ai(ques,aia,t):
    
    aia=(418,970)
    aia=(523,941)
    pyautogui.click(aia[0],aia[1], clicks=1, interval=0.25, button='left')
    sleep(1)
    pyperclip.copy(ques)

    # 模拟按下Ctrl+V组合键将文本粘贴到输入框中
    pyautogui.hotkey('ctrl', 'v')
    # 模拟键盘按键Enter
    pyautogui.press('enter')
    sleep(t)
    #清空剪贴板
    ctypes.windll.user32.OpenClipboard(None)
    ctypes.windll.user32.EmptyClipboard()
    ctypes.windll.user32.CloseClipboard()
    # 获取最后一个 <div class="markdown-body"> 标签的文本内容
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    divs = soup.find_all('div', class_='markdown-body')
    last_div_text = divs[-1].get_text()
    return(last_div_text)

init_driver()
print(ask_ai('hello',1,10))
