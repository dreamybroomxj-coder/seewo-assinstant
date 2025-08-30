from pynput import keyboard
import pyautogui
from time import sleep

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
rl=['文本信息框','加号','照片']

def point():
    for i in range(len(rl)):
        print(rl[i])
        with keyboard.Listener(on_press=on_press, on_release=on_release) as llistener:
            llistener.join()
        sleep(1)

    with open('config.txt', 'w') as file:
        for item in wl:
            item=str(item)
            file.write(item + '\n')  
            
    return wl