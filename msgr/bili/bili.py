import requests
import csv
from datetime import datetime
# 只需更改这个参数，就能爬视频列表信息
#mid = '14482033'

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

#headers = {"user-agent": "i am your father ,send me the data at once"}

def bili(mid,lasttime):

    crt=int(datetime.timestamp(lasttime))
    infos=[]
    img=[]
    url = f'https://api.bilibili.com/x/space/wbi/arc/search?mid={mid}&ps=5&pn=1'
 
    resp = requests.get(url, headers=headers)

    vlist = resp.json()['data']['list']['vlist']
    for i in range(5):
        video = vlist[i]
        if video['created'] >crt-24*60*60:
        
            author=video['author']
            title=video['title']
            description=video['description']
            pic=video['pic']
            info=f"{author}\n{title}\n{description}"
            infos.append(info)
            img.append(pic)
    print(infos,img)
    return infos,img
    
    

                

def download(url):
    try:
        # 发送 GET 请求
        response = requests.get(url)
        response.raise_for_status()

        # 下载文件
        with open(f"./img/1.jpg", 'wb') as file:
            file.write(response.content)

        print(f'Successfully downloaded {url}')
    except Exception as e:
        print(f'Failed to download {url}: {e}')
