# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''
 description: 使用scrapy 自带的  -o item.json 指定把爬取到的数据转换成json文件 也可以在此方法里加入别的保存功能如保存到数据库
 create time: 2019-03-26 17:27
 @:paramter:
 @:return
 '''
import bosscrapy.database as db
from scrapy.exceptions import DropItem
from bosscrapy.items import BosscrapyItem
cursor = db.conn.cursor()


class BosscrapyPipeline(object):
    '''

     description: 查询数据库中的记录，用来判断是否入库
     create time: 2019-04-15 15:13
     @:paramter:
     @:return 返回数据库中的记录
     '''

    def __init__(self):
        self.item_id = set()

    def get_bossscrapy(self, item):
        sql = "SELECT id FROM bossscrapy WHERE item_id='%s'" % item['item_id']
        
        cursor.execute(sql)
        return cursor.fetchone()

    def save_bossscrapy(self, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'INSERT INTO bossscrapy (%s) VALUES (%s)' % (fields, temp)
        cursor.execute(sql, values)
        return db.conn.commit()
    def dropitem(self,item):        
        for k,v in item.items():
            if v=="":
                print('null------->%s'%item)
                raise DropItem(item) #数据清洗，去掉值为空的数据

    def process_item(self, item, spider):                  
        self.dropitem(item)
        exist = self.get_bossscrapy(item) # 去重
        if not exist:
            self.save_bossscrapy(item)
        else:
            print('------该职位已经爬取过-------!')
        return item
