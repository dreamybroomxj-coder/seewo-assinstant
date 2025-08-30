import requests
import csv
import time


headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
url =  'https://api.bilibili.com/x/space/wbi/arc/search?mid={mid}&ps=30&pn=1'

#只需更改这个参数，就能爬视频列表信息
mid = '373489046'


with open('{mid}_infos.csv'.format(mid=mid), 'w', encoding='utf-8', newline='') as csvf:
    
    fieldnames=['pic','description','title','created']
       #封面、简介、标题、发布时间
    writer = csv.DictWriter(csvf, fieldnames=fieldnames)
    writer.writeheader()

    resp = requests.get(url, headers=headers)
        
    record_num = resp.json()['data']['page']['count']
    max_page = int(record_num/30)+1

    resp = requests.get(url, headers=headers)
    vlist = resp.json()['data']['list']['vlist']

    for video in vlist:
        writer.writerow(video)
    
    time.sleep(1)
