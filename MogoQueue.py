from pymongo import MongoClient,errors
from _datetime import datetime,timedelta
class MogoQueue():
    OUTSIANDING = 1
    PROCESSING = 2
    COMPLETE = 3
    def __init__(self,db,collection,timeout=300):
        self.client=MongoClient()
        self.Clinet=self.client[db]
        self.db=self.Clinet[collection]
        self.timeout=timeout
    def __bool__(self):
        record = self.db.find_one(
            {'status': {'$ne': self.COMPLETE}}
        )
        return True if record else False
    def push_theme(self,url,title,number):#这个函数用来添加新的URL以及URL主题名字进去队列
        try:
            self.db.insert({'_id':url,'status':self.OUTSIANDING,'主题':title,'书籍数量':number})
            print(title,url,'插入队列成功')
        except errors.DuplicateKeyError as e:#插入失败则是已经存在于队列了
            print(title,url,'已经存在队列中')
            pass
    def push_queue(self,url):
        try:
            self.db.insert({'_id':url,'status':self.OUTSIANDING})
            print(url,'插入队列成功')
        except errors.DuplicateKeyError as e:#插入失败则是已经存在于队列了
            print(url,'已经存在队列中')
            pass
    def push_book(self,title,author,book_style,book_introduction,book_url):
        try:
            self.db.insert({'_id':book_url,'书籍名称':title,'书籍作者':author,'书籍类型':book_style,'简介':book_introduction})
            print(title, '书籍插入队列成功')
        except errors.DuplicateKeyError as e:
            print(title, '书籍已经存在队列中')
            pass


    def select(self):
        record = self.db.find_and_modify(
            query={'status':self.OUTSIANDING},
            update={'$set':{'status': self.PROCESSING, 'timestamp':datetime.now() }}
        )
        if record:
            return record['_id']
        else:
            self.repair()
            raise KeyError
    def repair(self):
        record = self.db.find_and_modify(
            query={
                'timestamp':{'$lt':datetime.now()-timedelta(seconds=self.timeout)},
                'status':{'$ne':self.COMPLETE}
            },
            update={'$set':{'status':self.OUTSIANDING}}

        )
        if record:
            print('重置URL',record['_id'])
    def complete(self,url):
        self.db.update({'_id':url},{'$set':{'status':self.COMPLETE}})