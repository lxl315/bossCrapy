# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''
 create by: lxl
 description: 招聘信息Item
 create time: 2019-03-25 18:59  
 @:paramter:
 @:return 
 '''
class BosscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    item_id=scrapy.Field() #id
    name = scrapy.Field() #职位名称
    salary=scrapy.Field() #薪资
    profession =scrapy.Field() #学历
    experience=scrapy.Field()#经验
    welfare =scrapy.Field() #福利
    job =scrapy.Field()#工作内容
    city=scrapy.Field()#地区

