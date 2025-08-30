from PIL import ImageGrab,Image
import gc
import numpy as np
from time import sleep
import win32gui
import pytesseract
from pynput import keyboard
import pyautogui
from selenium import webdriver
from bs4 import BeautifulSoup
import pyperclip
import ctypes

screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

# 按下Shift键时执行的函数
def on_press(key):
    if key == keyboard.Key.shift:
        print("Shift键被按下")
        x, y = pyautogui.position()
        print(x,y)
        wl.append((x,y))
# 释放Shift键时执行的函数
def on_release(key):
    if key == keyboard.Key.shift:
        print("Shift键被释放")
        return False

wl=[]
rl=['head1','head2','xysend','xyback','xyreturn','wxsend','wxchoose','wxchoosecom','wxsend','wximg','wxsee','wxteturn','x','ai']
#for i in range(13):
 #   print(rl[i])
  #  with keyboard.Listener(on_press=on_press, on_release=on_release) as llistener:
   #     llistener.join()
    #sleep(1)
wl=[(1530, 141), (1530, 238), (1055, 787), (996, 119), (1041, 361), (1487, 874), (1298, 522), (1731, 862), (1631, 772), (1885, 830), (822, 172), (1460, 223), (1712, 179)]
print(wl)
def get_window_rect(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    #win32gui.SetForegroundWindow(hwnd)
    print(rect)
    #return (rect[0]/0.8, rect[1]/0.8, rect[2]/0.8, rect[3]/0.8)
    return (rect[0], rect[1], rect[2], rect[3])

def get_window_corners(window_name, pid):
    hwnd = win32gui.FindWindowEx(0, 0, None, window_name)
    rect = get_window_rect(hwnd)
    
    return rect

def find_msg(name,id,mode,j,color):

    rectt=get_window_corners(name,id)

    # 定义检测窗口和竖列的位置和大小
    window_pos = (rectt[0], rectt[1]+100, rectt[2], rectt[3]-100)

    # 截图并保存为1.png
    screen_img = ImageGrab.grab(bbox=window_pos)
    screen_img.save("1.png")

    # 将图像转换为numpy数组
    np_img = np.array(screen_img)

    # 查找符合条件的像素点
    
    rows, cols, _ = np_img.shape
    if mode=="down":
        ran=range(rows-1,-1,-1)
    elif mode=="up":
        ran=range(rows)
    for i in ran:
        
        if all(np_img[i][j] == color):
            x = j
            y = i
            return(y+100+rectt[1])
            break 
        else:
            continue
    
    # 释放不再需要的资源
    del screen_img
    del np_img
    gc.collect()
    
def see_what_say(name,id,who):
    rectt=get_window_corners(name,id)
    topc=(49,182,41)
    botc=(255,255,255)
    topp=45
    botp=89
    if who=="me":
        topc=(255,255,255)
        botc=(37,110,255)
        topp=376
        botp=322
    top=find_msg("希沃云班",11968,"down",topp,topc)
    bottom=find_msg("希沃云班",11968,"down",botp,botc)
    print(top,bottom)
    top-=42
    #print(rectt)
    s=rectt[2]-rectt[0]
    left=rectt[0]+0.19*s
    right=rectt[2]-0.24*s

    if who=="me":   #互换
        left=rectt[0]+0.24*s
        right=rectt[2]-0.19*s
    #print(left,top,right,bottom)
    window_pos=(left,top,right,bottom)
    #print(window_pos)

    img = ImageGrab.grab(bbox=window_pos)
    img.save("2.png")
    text = pytesseract.image_to_string(img, lang='chi_sim')
    if text=="":
        for i in range(5):
            xx=wl[i+6]
            pyautogui.click(xx[0],xx[1], clicks=1, interval=0.25, button='left')
            sleep(0.8)
            if i==4 or i==2:
                sleep(1)
            yy=wl[11]
            pyautogui.doubleClick(yy[0],yy[1])
            pyautogui.hotkey('ctrl', 'c')
            text = pyperclip.paste()
    return(text)
    del(img)
    gc.collect

driver = webdriver.Chrome()
# 访问页面
url = "https://c.binjie.fun/"
driver.get(url)
sleep(10)

def ask_ai(ques):
    
    aia=(418,970)
    pyautogui.click(aia[0],aia[1], clicks=1, interval=0.25, button='left')
    sleep(1)
    pyperclip.copy(ques)

    # 模拟按下Ctrl+V组合键将文本粘贴到输入框中
    pyautogui.hotkey('ctrl', 'v')
    # 模拟键盘按键Enter
    pyautogui.press('enter')
    sleep(10)
    #清空剪贴板
    ctypes.windll.user32.OpenClipboard(None)
    ctypes.windll.user32.EmptyClipboard()
    ctypes.windll.user32.CloseClipboard()
    # 获取最后一个 <div class="markdown-body"> 标签的文本内容
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    divs = soup.find_all('div', class_='markdown-body')
    last_div_text = divs[-1].get_text()
    return(last_div_text)

tt=5
i=0
sleep(5)
# 循环检测像素点颜色
while True:
    sleep(2)
    #pyautogui.click(804,247, clicks=1, interval=0.25, button='left')
    #pyautogui.click(1919,1, clicks=1, interval=0.25, button='left')
    co=wl[0]
    hedtwo=wl[1]
    bac=wl[3]
    retu=wl[4]
    rep=wl[2]
    # 获取指定位置的像素颜色
    try:
        color = pyautogui.pixel(co[0],co[1])
    except Exception as e:
        print("Error:", e)
        color=(201,201,201)
    # 如果像素颜色不是白色则点击目标位置
    if color[1]<180 or color[2]<180:
   # if i==0:
        print("o")
        pyautogui.click(co[0],co[1], clicks=1, interval=0.25, button='left')
        sleep(0.5)
        pyautogui.click(hedtwo[0],hedtwo[1], clicks=1, interval=0.25, button='left')
        sleep(0.5)
        #干掉红点
        pyautogui.click(bac[0],bac[1], clicks=1, interval=0.25, button='left')
        sleep(0.85)
        pyautogui.click(retu[0],retu[1], clicks=1, interval=0.25, button='left')
        sleep(1.2)
        #刷新
        pyperclip.copy(ask_ai(see_what_say("希沃云班",11968,"you")))
        pyautogui.click(rep[0],rep[1], clicks=1, interval=0.25, button='left')
        sleep(0.45)
        
        pyautogui.hotkey('ctrl', 'v')
        sleep(0.05)
        # 模拟键盘按键Enter
        pyautogui.press('enter')
        tt=3
        print("ok")
    if tt==3:
        i+=1
        if i>20:
            i=0
            tt=5
            
    # 暂停一段时间后再次循环检测
    sleep(tt)
