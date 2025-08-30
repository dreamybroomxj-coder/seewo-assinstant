import requests
import csv
import time

def check(a):
    b=len(str(a))
    if b<30:
        print(a)
    else:
        print(b,"啊")

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}


#只需更改这个参数，就能爬视频列表信息
mid = '14482033'

url =  f'https://api.bilibili.com/x/space/wbi/arc/search?mid={mid}&ps=30&pn=1'

with open('{mid}_infos.csv'.format(mid=mid), 'w', encoding='utf-8', newline='') as csvf:
    fieldnames = ['comment', 'typeid', 'play', 'pic', 'subtitle', 'description', 'copyright', 'title', 'review', 'author', 'mid', 'created', 'length', 'video_review', 'aid', 'bvid', 'hide_click', 'is_pay', 'is_union_video', 'is_steins_gate', 'is_live_playback', 'meta', 'is_avoided', 'attribute']
    writer = csv.DictWriter(csvf, fieldnames=fieldnames,extrasaction="ignore")
    writer.writeheader()    
    resp = requests.get(url, headers=headers)
    vlist = resp.json()['data']['list']['vlist']
    for video in vlist:
        writer.writerow(video)
    time.sleep(1)

    
