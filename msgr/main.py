from datetime import datetime

from reachtime import reachtime,wait
from init import point
from bili.bili import bili,download
from weather import weather
from send import send,send_img

hour=21
subscribe=['14482033','93156074','3513275']


def main():
    wl=point()
    print(wl)
    crt=datetime.now()
    while True:
        print(f"开始摸鱼，到工作时间{hour}:00再上班")
        reachtime(hour)
        imformation=[]
        image=[]
        for mid in subscribe:
            infos,img=bili(mid,crt)
            wait()
            for i in infos:
                imformation.append(i)
            for i in img:
                image.append(i)
            
        for a in range(len(imformation)):
            i=imformation[a]
            j=image[a]
            send(i,wl)
            wait()
            download(j)
            wait()
            send_img(wl)
            wait()


            

        weather_forcast=weather()
        for i in weather_forcast:
            send(i,wl)
            wait()
        send_img(wl)
        


if __name__ == '__main__':
    main()
