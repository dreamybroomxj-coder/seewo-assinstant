from time import sleep
import pyautogui
import pyperclip

def send(msg,wl):
    rep=wl[0]
    pyperclip.copy(msg)
    pyautogui.click(rep[0],rep[1], clicks=1, interval=0.25, button='left')
    sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    # 模拟键盘按键Enter
    pyautogui.press('enter')

#def send_img(wl):
def send_img(wl):
    b=wl[1]
    c=wl[2]
    pyautogui.click(b[0],b[1], clicks=1, interval=0.25, button='left')
    sleep(1)
    pyautogui.click(c[0],c[1], clicks=1, interval=0.25, button='left')
    sleep(1)
    pyautogui.press('enter')
    sleep(2)
    
def reply(answer,wl):
    ll=len(answer)
    #若字数太多就200一段，一段一段发
    if ll>200:
        a=ll//200
        b=ll%200
        for aa in range(a):
            sent=""
            for i in range(200):
                sent=sent+answer[i+aa*200]
            send(sent,wl)
        sent=""
        for i in range(b):
            sent=sent+answer[a*200+i]
        send(sent,wl)
    else:
        send(answer,wl)
