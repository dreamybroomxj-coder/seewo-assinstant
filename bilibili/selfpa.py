import requests
from bs4 import BeautifulSoup
from time import sleep
url = 'https://space.bilibili.com/434773406/video'
response = requests.get(url)
sleep(3)
soup = BeautifulSoup(response.content, 'html.parser')
print(str(soup))
li_tags = soup.find_all('li', {'class': 'small-item new fakeDanmu-item'})

data_aid_values = []
for li_tag in li_tags[:3]:
    data_aid_values.append(li_tag['data-aid'])

print(data_aid_values)
