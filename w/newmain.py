
from time import sleep,localtime
import pyautogui

from ask_ai import init_driver
from reply import relpy
from weather import tellweather

screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")
init_driver()

wl=[(1530, 141), (1530, 238), (1055, 787), (996, 119), (1041, 361), (1487, 874), (1298, 522), (1731, 862), (1631, 772), (1885, 830), (822, 172), (1460, 223), (1712, 179)]

# 读取配置文件中点位信息
wl = []
with open('config.txt', 'r') as file:
    for line in file:
        line = line.strip()  # 去掉行末尾的换行符和空格
        line = eval(line)
        wl.append(line)


co=wl[0]
hedtwo=wl[1]
bac=wl[3]
retu=wl[4]

tt=5
i=0
sleep(5)
# 循环检测像素点颜色

while True:
    sleep(2)
    #pyautogui.click(804,247, clicks=1, interval=0.25, button='left')
    #pyautogui.click(1919,1, clicks=1, interval=0.25, button='left')

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

        relpy(wl)
        tt=3
        print("ok")
    #敏感期
    if tt==3:
        i+=1
        if i>20:
            i=0
            tt=5
            
    t=localtime()
    if t.tm_hour == 16 and t.tm_min == 47:
        tellweather(wl)

    # 暂停一段时间后再次循环检测
    sleep(tt)