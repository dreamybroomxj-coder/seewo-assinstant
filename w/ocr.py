import win32gui
import pytesseract
from PIL import ImageGrab
import numpy as np
import pyautogui
import pyperclip
from time import sleep

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

def find(name,id,mode,j,color):
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
        else:
            continue

def find_msg(name,id,mode,j,color):
    for i in range(5):
        k=find(name,id,mode,j,color)
        if k==None:
            sleep(3)
            continue
        else:
            return(k)
            
        


def see_what_say(name,id,who,wl):
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
    #如果识别不出就丢给微信
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
