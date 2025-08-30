import requests
import matplotlib.pyplot as plt

url = "https://devapi.qweather.com/v7/weather/24h?location=101280107&key=ef4079fe8151415ba4621f8f9353c73e"


def weather():
    l=[]
    w=""
    p=0
    t=[]

    response = requests.get(url)
    data = response.json()

    if data["code"] == "200":
        hourly_forecast = data["hourly"]
        for forecast in hourly_forecast:
            fx_time = forecast["fxTime"]
            temp = forecast["temp"]
            weather_text = forecast["text"]
            pop = forecast["pop"]
            fx_time = fx_time[:-6].replace("T", " ")

            t.append(int(temp))
            w+=f"{fx_time}\n温度: {temp}°C\n天气: {weather_text}\n降水概率: {pop}%\n\n"
            p+=1
            if p%3==0:
                l.append(w)
                p=0
                w=""

    else:
        print("请求失败")
        l=['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']
    if l!=[]:
        for i in l:
            print(i)


    # 构造X轴小时数据
    hours =['16','17','18','19','20','21','22','23','00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']

    print(t)
    # 绘制曲线图
    plt.plot(hours, t)

    # 设置坐标轴标题和标签
    plt.title("tem")
    plt.xlabel("Hour")
    plt.ylabel("Temperature")

    # 保存图形
    plt.savefig('./img/1.jpg')
    return(l)
