from datetime import datetime
from time import sleep
from random import random

def thistime(hour):
    current_time = datetime.now()
    h=current_time.hour
    d=current_time.day
    if h>=hour:
        target_time = current_time.replace(day=d+1,hour=hour, minute=0, second=0)
        #target_time = current_time.replace(day=d,hour=hour, minute=18, second=0)
    else:
        target_time = current_time.replace(hour=hour, minute=0, second=0)
    return target_time

def reachtime(hour):
    current_time = datetime.now()
    target_time = thistime(hour)
    time_difference = target_time - current_time
    t = time_difference.total_seconds()
    print(f"睡{t}秒")
    sleep(t)

def wait():
    #t=2+random()
    t=0.5
    sleep(t)

