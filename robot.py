# -*- coding: utf-8 -*-

# 使用爬虫爬取数据前，解析网站robots.txt文件
import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
rp.set_url("http://example.webscraping.com/robots.txt")
rp.read()
url = "http://example.webscraping.com"

user_agent = "BadCrawler"  # 代理
print(rp.can_fetch(user_agent, url))

user_agent = "GoodCrawler"
print(rp.can_fetch(user_agent, url))


# 使用builtwith模块查看网站使用的技术
import builtwith
url = 'http://www.12306.com'
builtwith.parse(url)

# 查看网站所有者是谁
import whois
url = 'baidu.com'
print(whois.whois(url))

# 捕获联网异常并重试
import urllib
url = "http://i.hamreus.com/ps1/c/cslr/wqbhjz/01.JPG.webp?cid=216853&md5=lbJkXighZetr-xl1JVcjIw"
url = 'http://httpstat.us/500'
def download(url, num_retries):
    print('Downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError as e:
        print('error:', e.code, e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code <= 600:
                return download(url, num_retries-1)
    return html

download(url, 2)

url = 'http://www.meetup.com/'
html = urllib.request.urlopen(url).read()
