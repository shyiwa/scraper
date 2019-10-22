# -*- coding: utf-8 -*-

# 从动漫在线下载漫画

import urllib as ul
import requests
import os
import itertools
from datetime import datetime as dt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def download(url):
    res = requests.get(url)			
    bs_content_page = BeautifulSoup(res.content, 'lxml')
    name = bs_content_page.find_all('a',href=url)[0]['title']	# 漫画名
    name = name.strip()    # 去除首尾空格
    table = bs_content_page.select('div > ul > li > a')		# 章节列表
    nChapters = len(table)
    
    print('共', str(nChapters), '章')
    start = dt.now()
        
#    for j in range(nChapters):
    for chap in table:
        chap_url = chap['href']				# 章节的链接网址
        chap_name = chap['title'].strip()	# 章节名
        print('下载', chap_name)
        
        path = os.path.join(os.path.curdir, name, chap_name)		
        if not os.path.exists(path):
            os.makedirs(path) 				# 创建章节的文件夹

        for i in itertools.count(1):
            page_url = chap_url + '#p=%d' % i		# 章节的页面网址
            path = os.path.join(os.path.curdir, name, chap_name, str(i)+'.jpg')
            browser.get(page_url)
            browser.get(page_url)			# 要重复载入网址一次才能刷新页面
            res = browser.page_source
            bs = BeautifulSoup(res,'lxml')
            img_url = bs.find_all('img', id='curPic')[0]['src']	# 图片网址
            try:
                ul.request.urlretrieve(img_url,path)    
            except Exception as e:
                break	# 下载图片时出错说明当前章节的图片已经全部下载过
        
            end = dt.now()
            print((end-start).total_seconds(), '秒')
                
#显示下载进度
def schedule(a,b,c):
     #a:已下载的数据块 b:数据块的大小 c:远程文件的大小
     per = 100.0 * a * b / c
     if per > 100 :
         per = 100
     print('%.2f%%' % per)


if __name__ == '__main__':
    # for i in range(92):
    # path = './2/'+str(i+1)+'.jpg'
    # url = 'http://183.91.33.78/p0.xiaoshidi.net/2013/01/29035807'+str(i)+'.jpg'
    # ul.request.urlretrieve(url,path)
    
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.binary_location = 'C:/Users/wys/AppData/Local/Google/Chrome/Application/chrome.exe'

    # browser = webdriver.Chrome(chrome_options = chrome_options)
    browser = webdriver.PhantomJS(executable_path='C:/Users/WWW/Anaconda3/pkgs/phantomjs-2.1.1-0/Library/bin/PhantomJS')
    
	# headers={
	# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER' 
	# }   
	# page=  ul.request.Request(url, headers=headers)
	# page_info = ul.request.urlopen(page).read().decode('utf-8')
	# print(page_info)

    url = 'http://www.dmzx.com/manhua/64/'
    download(url)

    # url1 = 'http://lib.bjut.edu.cn/statics/images/dt_img.jpg'
    # ul.request.urlretrieve(url1,path,schedule)
