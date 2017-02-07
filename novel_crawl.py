from ip_pool_request import html_request
from bs4 import BeautifulSoup
import random
import multiprocessing
import time
import threading
from ip_pool_request2 import download_request
from MogoQueue import MogoQueue
def novel_crawl(max_thread=8):
    crawl_queue = MogoQueue('novel_list','crawl_queue')#实例化数据库操作，链接到数据库，这个是爬虫需要的书籍链接表
    book_list = MogoQueue('novel_list','book_list')#爬取的内容放进这里
    def pageurl_crawler():
        while True:
            try:
                url = crawl_queue.select()#从数据库提取链接，开始抓
                print(url)
            except KeyError:#触发这个异常，则是链接都被爬完了
                print('队列没有数据，你好坏耶')
            else:

                data=html_request.get(url,3)
                soup = BeautifulSoup(data,'lxml')

                all_novel = soup.find('div',{'class':'kindContent'}).findAll('li')


                for novel in all_novel:#提取所需要的所以信息
                    text_tag =novel.find('div',{'class':'textShow'})
                    title = text_tag.find('div',{'class':'name'}).find('a').get_text()
                    author = text_tag.find('span',{'class':'author'}).find('a').get_text()
                    book_style = text_tag.find('span',{'class':'kind'}).find('a').get_text()
                    book_introduction= text_tag.find('div',{'class':'desc'}).get_text().strip().replace('\n','')
                    img_tag = novel.find('div',{'class':'imgShow'}).find('a',{'class':'common'})

                    book_url = 'http://book.easou.com/' + img_tag.attrs['href']
                    book_list.push_book(title,author,book_style,book_introduction,book_url)
                    crawl_queue.complete(url)#完成之后改变链接的状态
                    #print(title,author,book_style,book_introduction,book_url)
    threads=[]
    while threads or crawl_queue:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads)< max_thread:
            thread = threading.Thread(target=pageurl_crawler())#创建线程
            thread.setDaemon(True)#线程保护
            thread.start()
            threads.append(thread)
        time.sleep(5)
def process_crawler():
    process=[]
    num_cups=multiprocessing.cpu_count()
    print('将会启动的进程数为',int(num_cups)-2)
    for i in range(int(num_cups)-2):
        p=multiprocessing.Process(target=novel_crawl)#创建进程
        p.start()
        process.append(p)
        for p in process:
            p.join()
if __name__ == '__main__':
    process_crawler()
