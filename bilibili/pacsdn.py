# 爬取bilibili up主的视频信息

'''
{
    'name': XXX // 视频名称
    'author': XXX //作者名称
    'date': XXX //发布时间
    'url': XXX //视频链接
    'wachted': XXX //观看次数
    'bullet_comments' XXX //弹幕数量
    'liked': XXX //点赞数量
    'coin': XXX //投币数量
    'collected': XXX //收藏数量
    'shared': XXX //收藏数量
    'now_date': XXX //获取信息时间
}
'''

from selenium import webdriver
import re
import json
from bs4 import BeautifulSoup
import time
from urllib import parse as url_parse
import datetime
from selenium.webdriver.common.by import By

class BSpider():

    def __init__(self):
        # 某个up主的视频页面，只需对pagenum字段进行替换切换不同的页面
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        self.main_url = 'https://space.bilibili.com/upuser_id/video?tid=0&page=page_num&keyword=&order=pubdate'
        self.browser = webdriver.Firefox(options=options)

    def close_webdriver(self):
        # 关闭相关驱动
        self.browser.quit()

    def locate2upuser(self, name_string):
        # 通过名字定位到该up主的ID号
        # url中文编码
        name_string = url_parse.quote(name_string)

        self.browser.get('https://search.bilibili.com/upuser?keyword='+name_string+'&page=1&order=fans&order_sort=0&user_type=3')
        time.sleep(3)

        # 获取当前up的个人链接
        uid = self.browser.find_element(By.XPATH,'//*[@id="user-list"]/div[1]/ul/li/div[2]/div[1]/a[1]').get_attribute('href')
        time.sleep(1)
        # 从链接中取得id
        uid = uid.split('/')[-1].split('?')[0]
        # print(uid)
        return uid

    def resub(self, url, r_pattern, value):
        # 正则替换
        pattern = re.compile(r_pattern)
        page_url = re.sub(pattern, value, url)
        return page_url
        
    def get_detial_list(self, url):
        # 获取某一页视频 url及名称 列表
        detial_url_list = []
        detial_name_list = []
        self.browser.get(url)
        time.sleep(2)
        html = BeautifulSoup(self.browser.page_source)

        for a_label in html.find('div', id = 'submit-video-list').find_all('a', attrs = {'target':'_blank', 'class':'title'}):
            if (a_label['href'] != None):
                detial_url_list.append('https:'+a_label['href'])
                detial_name_list.append(a_label.text)
        
        return detial_url_list, detial_name_list

    def get_pagenum(self, url):
        # 获取当前up的视频页数
        page_url = url
        page_url = self.resub(page_url, r'page_num', str(1))
        self.browser.get(page_url)
        time.sleep(1)
        html = BeautifulSoup(self.browser.page_source)

        page_number = html.find('span', attrs={'class':'be-pager-total'}).text
        return int(page_number.split(' ')[1])

    def get_digit_from_string(self, string):
        #print(string)
        return re.findall(r"\d+\.?\d*", string)[0]
        
    def get_video_detial(self, video_detial_dect):
        # 获取某个视频的基本信息

        url = video_detial_dect['url']
        self.browser.get(url)
        # 这里的时间设置的大一点，不然页面会加载不出来，
        # 导致获取到的信息为空 可以用浏览器先测试一下多少时间可以获取到这些页面资源 
        # 这个由自己电脑的性能和网络决定，出现空值的时候试着将sleep的值调大一点
        time.sleep(5)
        html = BeautifulSoup(self.browser.page_source)
        print(url)
        # 清洗数据获取信息 要进行正则替换去掉中文 保留数字
        try:
            video_detial_dect['watched'] = self.get_digit_from_string(html.find('span', attrs={'class':'view'})['title'])
            video_detial_dect['bullet_comments'] = self.get_digit_from_string(html.find('span', attrs={'class':'dm'})['title'])
            video_detial_dect['liked'] = self.get_digit_from_string(html.find('span', attrs={'class':'like'})['title'])
            video_detial_dect['coin'] = html.find('span', attrs={'class':'coin'}).get_text().strip()
            video_detial_dect['collected'] = self.get_digit_from_string(html.find('span', attrs={'class':'collect'})['title'])
            video_detial_dect['shared'] = html.find('span', attrs={'class':'share'}).get_text().strip().split('\n')[0]
            video_detial_dect['date'] = self.browser.find_element_by_xpath('//*[@id="viewbox_report"]/div/span[3]').text
            video_detial_dect['now_date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        except Exception as e:
            video_detial_dect['watched'] = ''
            video_detial_dect['bullet_comments'] = ''
            video_detial_dect['liked'] = ''
            video_detial_dect['coin'] = ''
            video_detial_dect['collected'] = ''
            video_detial_dect['shared'] = ''
            video_detial_dect['date'] = ''
            video_detial_dect['now_date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
            print(e)
        print(video_detial_dect)
        return video_detial_dect

    def get_page(self, upuser_name):
        # 获取一个up 主下的所有视频
        uid = self.locate2upuser(upuser_name)
        url = self.resub(self.main_url, r'upuser_id', str(uid))
        
        # page_number = 1
        page_number = self.get_pagenum(url) # 页数
        # 视频url列表 名称列表
        detial_url_list = []
        detial_name_list = []

        for index in range(page_number):
            print("------------------------------------")
            print("page: %d" %(index+1))

            # 对于不同的页，进行正则替换
            page_url = url
            page_url = self.resub(page_url, r'page_num', str(index+1))
            print('page_url: %s' %page_url)
            detial_url_list_onepage, detial_name_list_onepage = self.get_detial_list(page_url)
            # 这里要用extend加到后面
            detial_url_list.extend(detial_url_list_onepage)
            detial_name_list.extend(detial_name_list_onepage)
        
        # print(detial_url_list)
        # print(detial_name_list)

        # 视频json
        video_detial_json = []
        for i in range(len(detial_url_list)):
            video_detial_dect = {}
            video_detial_dect['url'] = detial_url_list[i]
            video_detial_dect['author'] = upuser_name
            video_detial_dect['name'] = detial_name_list[i]
            video_detial_dect = self.get_video_detial(video_detial_dect)
            video_detial_json.append(video_detial_dect)
        # print(video_detial_json)

        
        print('dump to json file ...')
        with open(r'2020\Crawl\Bilibili\Item1\data\video_detial.json', 'w', encoding='utf-8') as f:
            json.dump(video_detial_json, f, ensure_ascii=False,sort_keys=True, indent=4)
        print('dump  file done.')


print("init....")
bilibili = BSpider()
print("init done.")
# 更改名字爬取不同的UP视频信息
bilibili.get_page('红腿小隼')
bilibili.close_webdriver()
