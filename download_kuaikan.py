# -*- coding: utf-8 -*-

# 下载快看漫画的漫画

import urllib as ul
import requests
import os
from bs4 import BeautifulSoup
#from datetime import datetime as dt

def download(url):
    res = requests.get(url)
    bs_content_page = BeautifulSoup(res.text, 'lxml')
    name = bs_content_page.find('div','comic-name').contents[0]
    name = name.strip()    # 去除首尾空格
    table = bs_content_page.find_all('td','tit')
    nChapters = table.__len__()
    
    print('共', str(nChapters), '章')
        
    for j in range(nChapters):
    for j in range(18,nChapters):
        chap_url = 'http://www.kuaikanmanhua.com/' + table[j].find('a')['href']
        chap_name = table[j].find('a')['title'].strip()
        
        path = './' + name + '/' + chap_name
        os.makedirs(path)  
        
        res = requests.get(chap_url)
        bs = BeautifulSoup(res.text,'lxml')
        images = bs.find_all('img','kklazy')
        number = images.__len__()
        
        print('下载倒数第', j+1, '章, ', number, '张图片')
        for i in range(number):
            path = './' + name + '/' + chap_name + '/' + str(i+1) + '.jpg'
            img_url = images[i]['data-kksrc']
            ul.request.urlretrieve(img_url,path)
            
#            img = requests.get(img_url).content            
#            with open(path, 'wb') as f:
#                f.write(img)


if __name__ == '__main__':
    
#    for i in range(92):
#        path = './2/'+str(i+1)+'.jpg'
#        url = 'http://183.91.33.78/p0.xiaoshidi.net/2013/01/29035807'+str(i)+'.jpg'
#        ul.request.urlretrieve(url,path)
    
#    headers={
#    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0",
#    }   
#    page=  ul.request.Request(url, headers=headers)
#    page_info = ul.request.urlopen(page).read().decode('utf-8')
#    #print(page_info)
    
    url = 'http://www.kuaikanmanhua.com/web/topic/1004/'
    download(url)

