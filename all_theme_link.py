

from bs4 import BeautifulSoup
import requests
from MogoQueue import MogoQueue
spider_queue = MogoQueue('novel_list','crawl_queue')#实例化封装数据库操作这个类，这个表是存每一页书籍的链接的
theme_queue = MogoQueue('novel_list','theme_queue')#这个表是存每一个主题页面的链接的
html = requests.get('http://book.easou.com/w/cat_yanqing.html')

soup = BeautifulSoup(html.text,'lxml')

all_list = soup.find('div',{'class':'classlist'}).findAll('div',{'class':'tit'})
for list in all_list:
    title = list.find('span',{'class':'name'}).get_text()
    book_number = list.find('span',{'class':'count'}).get_text()
    theme_link = list.find('a')['href']
    theme_links='http://book.easou.com/'+theme_link#每个书籍类目的数量
    #print(title,book_number,theme_links)找到每个分类的标题和每个类目的链接，然后再下面的links提取出来
    theme_queue.push_theme(theme_links,title,book_number)
links=['http://book.easou.com//w/cat_yanqing.html',
'http://book.easou.com//w/cat_xuanhuan.html',
'http://book.easou.com//w/cat_dushi.html',
'http://book.easou.com//w/cat_qingxiaoshuo.html',
'http://book.easou.com//w/cat_xiaoyuan.html',
'http://book.easou.com//w/cat_lishi.html',
'http://book.easou.com//w/cat_wuxia.html',
'http://book.easou.com//w/cat_junshi.html',
'http://book.easou.com//w/cat_juqing.html',
'http://book.easou.com//w/cat_wangyou.html',
'http://book.easou.com//w/cat_kehuan.html',
'http://book.easou.com//w/cat_lingyi.html',
'http://book.easou.com//w/cat_zhentan.html',
'http://book.easou.com//w/cat_jishi.html',
'http://book.easou.com//w/cat_mingzhu.html',
'http://book.easou.com//w/cat_qita.html',
]
def make_links(number,url):#这里要解释一下，因为每个类目的书页不同，而且最末页是动态数据，源代码没有
    #这里采取了手打上最后一页的方法，毕竟感觉抓包花的时间更多
    for i in range(int(number)+1):
        link=url+'?attb=&s=&tpg=500&tp={}'.format(str(i))
        spider_queue.push_queue(link)#这里将每一页的书籍链接插进数据库
        #print(link)

make_links(500,'http://book.easou.com//w/cat_yanqing.html')
make_links(500,'http://book.easou.com//w/cat_xuanhuan.html')
make_links(500,'http://book.easou.com//w/cat_dushi.html')
make_links(5,'http://book.easou.com//w/cat_qingxiaoshuo.html')
make_links(500,'http://book.easou.com//w/cat_xiaoyuan.html')
make_links(500,'http://book.easou.com//w/cat_lishi.html')
make_links(500,'http://book.easou.com//w/cat_wuxia.html')
make_links(162,'http://book.easou.com//w/cat_junshi.html')
make_links(17,'http://book.easou.com//w/cat_juqing.html')
make_links(500,'http://book.easou.com//w/cat_wangyou.html')
make_links(474,'http://book.easou.com//w/cat_kehuan.html')
make_links(427,'http://book.easou.com//w/cat_lingyi.html')
make_links(84,'http://book.easou.com//w/cat_zhentan.html')
make_links(9,'http://book.easou.com//w/cat_jishi.html')
make_links(93,'http://book.easou.com//w/cat_mingzhu.html')
make_links(500,'http://book.easou.com//w/cat_qita.html')