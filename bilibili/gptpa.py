import requests
import csv
from datetime import datetime

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

# 只需更改这个参数，就能爬视频列表信息
mid = '14482033'

def bili(mid):
    url = f'https://api.bilibili.com/x/space/wbi/arc/search?mid={mid}&ps=30&pn=1'

    with open('{mid}_infos.csv'.format(mid=mid), 'w', encoding='utf-8', newline='') as csvf:
        fieldnames = ['pic', 'description', 'title', 'created','author']
        writer = csv.DictWriter(csvf, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()    
        resp = requests.get(url, headers=headers)
        #print(resp)
        vlist = resp.json()['data']['list']['vlist']
        for i in range(2):
            video = vlist[i]
            # 只将需要保存的字段写入CSV文件中
            row = {k: video[k] for k in fieldnames}
            writer.writerow(row)
        print("1")

def bi(mid,currenttime):
    url = f'https://api.bilibili.com/x/space/wbi/arc/search?mid={mid}&ps=30&pn=1'
    with open('{mid}_infos.csv'.format(mid=mid), 'w', encoding='utf-8', newline='') as csvf:
        fieldnames = ['pic', 'description', 'title', 'created','author']
        writer = csv.DictWriter(csvf, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()    
        resp = requests.get(url, headers=headers)
        print(resp)
        print(resp.json())

        vlist = resp.json()['data']['list']['vlist']
        for i in range(4):
            video = vlist[i]
            if abs(video['created'] - currenttime)<24*60*60:
            # 只将需要保存的字段写入CSV文件中
                row = {k: video[k] for k in fieldnames}
                writer.writerow(row)

crt=int(datetime.timestamp(datetime.now()))

bi('3513275',crt)