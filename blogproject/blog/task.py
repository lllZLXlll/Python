# import schedule
# import time
# import requests, re
# from .models import News
#
#
# def get_news():
#     # 爬取新闻
#     path = 'http://news.baidu.com/?tn=news'
#     content = requests.get(path)
#     content = content.content
#
#     with open('media/uploads/news/new.html', 'wb') as file:
#         file.write(content)
#
#     with open('media/uploads/news/new.html', 'r', encoding='utf-8') as file:
#         content = file.read()
#
#         list = re.findall('id="headline-tabs"[\S\s]*id="pane-recommend"', content)
#         list = re.findall('<a.*htm.*>.*</a>', ''.join(list))
#         for new in list[::-1]:  # 从网页上读取的a标签是从头到尾读取，热点新闻是在前面，这里选择倒序循环
#             title = re.findall('<a.*>(.*)</a>$', new)
#             url = re.findall('href="(.*[htm|html|shtml])"', new)
#             news = News(title=title[0], url=url[0], created_time=datetime.datetime.now())
#             news.save()
#
#
# def job():
#     print('每天7点爬取一次新闻--开始--')
#     print('每天7点爬取一次新闻--结束--')
#
# schedule.every().day.at("17:39").do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

import schedule
import time

def job():
    print("I'm working...")

schedule.every().day.at("17:41").do(job)
schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)