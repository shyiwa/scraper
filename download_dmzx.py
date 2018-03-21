# -*- coding: utf-8 -*-

# 从动漫在线下载漫画

import urllib as ul
import requests
import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#from datetime import datetime as dt

def download(url):
    res = requests.get(url)
    bs_content_page = BeautifulSoup(res.text, 'lxml')
    a = bs_content_page.body
print(a)    
    a = a.children
    for child in a:
        print(child)
    name = bs_content_page.find('h1').contents[0]
    name = name.strip()    # 去除首尾空格
    table = bs_content_page.find_all('div','subsrbelist center')
    table = table.find_all('a',target = '_blank')
    nChapters = table.__len__()
    
    print('共', str(nChapters), '章')
        
    for j in range(nChapters):
        chap_url = 'http://www.manhuagui.com' + table[j]['href']
        chap_name = table[j]['title'].strip()
        
        path = './' + name + '/' + chap_name
        os.makedirs(path)  
        
        res = requests.get(chap_url)
        bs = BeautifulSoup(res.text,'lxml')
        nPages = bs.find_all(text = re.compile(r'/\d+\)'))[0]
        nPages = int(re.sub('\D','', str(nPages)))

        print('下载倒数第', j+1, '章, ', nPages, '张图片')
        for i in range(nPages):
            path = './' + name + '/' + chap_name + '/' + str(i+1) + '.jpg'
            page_url = 'http://www.manhuagui.com/comic/416/216853.html#p='+str(i+1)
            browser.get(page_url)
            res = browser.page_source
            bs = BeautifulSoup(res,'lxml')
            
            res = requests.get(page_url)
            bs = BeautifulSoup(res.text,'lxml')
            img_url = bs.find_all('div','clearfix')[1]
   
            ul.request.urlretrieve(img_url,path)
            
            #browser = webdriver.PhantomJS(executable_path='C:/Users/WWW/Anaconda3/pkgs/phantomjs-2.1.1-0/Library/bin/PhantomJS')
            browser.get(page_url)
            data = browser.page_source
            bs = BeautifulSoup(data,'lxml')
            img_url = bs.find_all('img','mangaFile')[0]['src']
            browser.get(img_url)
            ul.request.urlretrieve(img_url,path,schedule)
                   
            img = requests.get(img_url,headers=headers).content            
            with open(path, 'wb') as f:
                f.write(img)
                
#显示下载进度
def schedule(a,b,c):
     #a:已下载的数据块 b:数据块的大小 c:远程文件的大小
     per = 100.0 * a * b / c
     if per > 100 :
         per = 100
     print('%.2f%%' % per)


if __name__ == '__main__':
    
#    for i in range(92):
#        path = './2/'+str(i+1)+'.jpg'
#        url = 'http://183.91.33.78/p0.xiaoshidi.net/2013/01/29035807'+str(i)+'.jpg'
#        ul.request.urlretrieve(url,path)
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.binary_location = 'C:/Users/wys/AppData/Local/Google/Chrome/Application/chrome.exe'

    browser = webdriver.Chrome(chrome_options = chrome_options)
    browser.get(url)
    
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER' 
    }   
#    page=  ul.request.Request(url, headers=headers)
#    page_info = ul.request.urlopen(page).read().decode('utf-8')
#    #print(page_info)
    
    url = 'http://www.dmzx.com/manhua/64/'
    download(url)

    url1 = 'http://lib.bjut.edu.cn/statics/images/dt_img.jpg'
    ul.request.urlretrieve(url1,path,schedule)
