# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''
 create by: lxl
 description: 使用scrapy 自带的  -o item.json 指定把爬取到的数据转换成json文件 也可以在此方法里加入别的保存功能
 create time: 2019-03-26 17:27
 @:paramter:
 @:return
 '''
class BosscrapyPipeline(object):
    def process_item(self, item, spider):
        return item
