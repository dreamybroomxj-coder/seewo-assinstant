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
    #if hwnd == 0:
    #    return None
    #if win32gui.GetWindowThreadProcessId(hwnd)[1] != pid:
    #    return None
    rect = get_window_rect(hwnd)
    #corners = [(rect[0], rect[1]), (rect[2], rect[1]), (rect[2], rect[3]), (rect[0], rect[3])]
    
    return rect

rectt=get_window_corners("无标题 - 画图",5756)
# 定义检测窗口和竖列的位置和大小
window_pos = (rectt[0],rectt[1],rectt[2],rectt[3]) 
# (left, top, right, bottom)
column_pos = (0,0,rectt[2]-rectt[0],rectt[3]-rectt[1]) 
# (x, y1, x, y2)

print(window_pos,column_pos)


while True:
    sleep(1)
    # 获取屏幕图像
    screen_img = ImageGrab.grab(bbox=window_pos)

    # 将图像转换为numpy数组
    np_img = np.array(screen_img)

    # 获取竖列区域的像素值
    column_pixels = np_img[column_pos[1]:column_pos[3], column_pos[0]]
    print(column_pixels)

    # 查找第一个符合条件的像素点
    color_to_find = (124,124,12)
    for i, pixel in enumerate(column_pixels):
        if all(pixel == color_to_find):
            # 计算符合条件像素点在屏幕上的位置
            x = column_pos[0]
            y = column_pos[1] + i
            print(f"找到符合条件的像素点：({x}, {y})")
            sleep(0.1)
            # 释放不再需要的资源
            del screen_img
            del np_img
            del column_pixels
            gc.collect()

            break
    else:
        print("未找到符合条件的像素点")

        # 释放不再需要的资源
        del screen_img
        del np_img
        gc.collect()
    break