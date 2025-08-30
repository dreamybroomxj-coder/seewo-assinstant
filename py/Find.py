import gc
from PIL import ImageGrab
import numpy as np
from time import sleep
import win32gui

def get_window_rect(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    return (rect[0], rect[1], rect[2], rect[3])

def get_window_corners(window_name, pid):
    hwnd = win32gui.FindWindowEx(0, 0, None, window_name)
    rect = get_window_rect(hwnd)
    
    return rect

def find_msg(name,id,mode):

    rectt=get_window_corners(name,id)

    # 定义检测窗口和竖列的位置和大小
    window_pos = (rectt[0]/0.8, rectt[1]/0.8+100, rectt[2]/0.8, rectt[3]/0.8-100)

    # 截图并保存为1.png
    screen_img = ImageGrab.grab(bbox=window_pos)
    screen_img.save("1.png")

    # 将图像转换为numpy数组
    np_img = np.array(screen_img)

    # 查找符合条件的像素点
    color_to_find = (37,110,255)
    rows, cols, _ = np_img.shape
    if mode=="up":
        ran=range(rows-1,-1,-1)
    elif mode=="down":
        ran=range(rows)
    for i in ran:
        j=400
        if all(np_img[i][j] == color_to_find):
            x = j
            y = i
            print(f"找到符合条件的像素点：({x}, {y})")
            break 
        

    # 释放不再需要的资源
    del screen_img
    del np_img
    gc.collect()
    

find_msg("希沃云班",11968,"up")

find_msg("希沃云班",11968,"down")
