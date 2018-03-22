# -*- coding: utf-8 -*-

import urllib, re
import itertools
import datetime, time

def download(url, user_agent = 'mrdl', num_tries = 2):
    headers = {'User-agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(request).read()
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print('Error:',e.code,e.reason)
        else:
            print('Error:',e.reason)
        html = None  
        if num_tries > 0:
            # 如果错误代码在500与600之间，则重试下载，直到次数达到上限
            if hasattr(e,'code') and 500 <= e.code <= 600: 
                html = download(url, num_tries-1)
    return html

# 延时类
class Throttle:
    def __init__(self, delay):
        self.delay = delay
        self.domains = {}   # 字典，域名：访问的时间点，初始为空（因为还没有访问）
    
    def wait(self, url):
        domain = urllib.parse.urlparse(url).netloc
        last_accessed = self.domains.get(domain) # 上一次访问域domain的时间点
        
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now() - 
                                       last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs) # 延时
        self.domains[domain] = datetime.datetime.now()
        

if __name__ == '__main__':
#    url = 'http://example.webscraping.com/places/default/sitemap.xml'
#    sitemap = download(url)      # 下载网站的地图
#    links = re.findall('<loc>(.*?)</loc>', str(sitemap))
#    
#    url = 'http://example.webscraping.com/robots.txt'
#    urllib.request.urlretrieve(url,'./robots.txt')
    
    throttle = Throttle(5)  # 创建5秒的延时类
    for page in itertools.count(1):
        print(page)
        url = "http://example.webscraping.com/places/default/view/-%d" % page        
        
        throttle.wait(url)
        html = download(url)    
        if html == None:
            break