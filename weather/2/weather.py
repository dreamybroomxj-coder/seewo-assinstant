import requests

url = "https://devapi.qweather.com/v7/weather/24h?location=101280107&key=ef4079fe8151415ba4621f8f9353c73e"
l=[]
w=""
p=0

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

        w+=f"{fx_time}\n温度: {temp}°C\n天气: {weather_text}\n降水概率: {pop}%\n\n"
        p+=1
        if p%3==0:
            l.append(w)
            p=0
            w=""

else:
    print("请求失败")

if l!=[]:
    for i in l:
        print(i)