from time import sleep
import pyautogui
import pyperclip
from ask_ai import ask_ai
from ocr import see_what_say


def send(msg,wl):
    rep=wl[2]
    pyperclip.copy(msg)
    pyautogui.click(rep[0],rep[1], clicks=1, interval=0.25, button='left')
    sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    sleep(0.1)
    # 模拟键盘按键Enter
    pyautogui.press('enter')


def reply(wl):
    
    requ=see_what_say("希沃云班",11968,"you",wl)
    #if requ=....:
        #answer=...
        #etc
    answer=ask_ai(requ,wl[13],10)
    
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
