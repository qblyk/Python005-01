import pretty_errors
import requests
import time
import json
from queue import Queue
from lxml import etree
import threading

class CrawlThread(threading.Thread):
    '''爬虫类'''
    # 继承父类进行初始化
    def __init__(self,thread_id,queue):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
        }

    # 重写run方法
    def run(self):
        print(f'启动线程：{self.thread_id}')
        self.scheduler()
        print(f'结束线程：{self.thread_id}')

    # 模拟调度任务
    def scheduler(self):
        while not self.queue.empty():
            # 队列为空不处理
            page = self.queue.get()
            print(f'下载线程:{self.thread_id}, 下载页面:{page}')
            url = f'https://www.solidot.org/?issue={20201205 - page}'
            print(url)

            try:
                # downloader 下载器
                response = requests.get(url,headers=self.headers)
                dataQueue.put(response.text)
            except Exception as e:
                print('下载出现异常',e)

class ParserThread(threading.Thread):
    '''页面内容分析'''
    print('开始分析页面')
    def __init__(self, thread_id, queue, file):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.queue = queue
        self.file = file

    def run(self):
        print(f'启动线程分析: {self.thread_id}')
        while flag:
            try:
                item = self.queue.get(False)
                # print('item值打印',item)
                if not item:
                    continue
                self.parse_data(item)
                self.queue.task_done()
            except Exception as e:
                pass
        print(f'结束线程: {self.thread_id}')
    
    def parse_data(self, item):
        '''
        解析网页内容的函数
        :param item:
        :return:
        '''
        # print('====>itme:',item)

        try:
            html = etree.HTML(item)
            # print(html)
            # books = html.xpath('//div[@class="pl2"]')
            newsList = html.xpath('//div[@class="bg_htit"]/h2/a')
            print(newsList)
            for news in newsList:
                try:
                    title = news.xpath('./text()')
                    link = news.xpath('./@href')
                    response = {
                        'title':title,
                        'link':link
                    }
                    # 解析方法和scrapy相同，再构造一个json
                    json.dump(response, fp=self.file, ensure_ascii=False)
                    self.file.write('\n')
                except Exception as e:
                    print('news error', e)
        except Exception as e:
            print('page error', e)

if __name__ == "__main__":
    
    # 定义存放网页的任务队列
    pageQueue = Queue(10)
    for page in range(0,5):
        pageQueue.put(page)
    
    # 定义存放解析数据的任务队列
    dataQueue = Queue()

    # 爬虫线程
    crawl_threds = []
    crawl_name_list = ['crawl_1','crawl_2','crawl_3']
    for thread_id in crawl_name_list:
        thread = CrawlThread(thread_id, pageQueue)
        thread.start()
        crawl_threds.append(thread)

    # 将结果保存到一个json文件中
    with open('book.json','a+',encoding='utf-8') as pipline_f:

        # 解析线程
        parse_thread = []
        parser_name_list = ['parse_1', 'parse_2', 'parse_3']
        flag = True
        for thread_id in parser_name_list:
            thread = ParserThread(thread_id, dataQueue, pipline_f)
            pipline_f.write('\n')
            thread.start()
            parse_thread.append(thread)
        
        # 结束crawl线程
        for t in crawl_threds:
            t.join()

        # 结束parse线程
        flag = False
        for t in parse_thread:
            t.join()

    print('退出主线程')

