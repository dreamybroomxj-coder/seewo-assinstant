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
rl=['第一个头像红点处','第二个','希悦输入框','希悦退出','希悦进入对话','wxsend','wxchoose','wxchoosecom','wxsend','wximg','wxsee','wxteturn','wxexit','chatGPT的输入框']

for i in range(13):
    print(rl[i])
    with keyboard.Listener(on_press=on_press, on_release=on_release) as llistener:
        llistener.join()
    sleep(1)
#写入文本文件

#wl=[(1530, 141), (1530, 238), (1055, 787), (996, 119), (1041, 361), (1487, 874), (1298, 522), (1731, 862), (1631, 772), (1885, 830), (822, 172), (1460, 223), (1712, 179)]

with open('config.txt', 'w') as file:
    for item in wl:
        item=str(item)
        file.write(item + '\n')        