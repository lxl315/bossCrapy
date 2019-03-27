# -*- coding: utf-8 -*-
import scrapy
from bosscrapy.items import  BosscrapyItem

class BossscrapySpider(scrapy.Spider):
    name = 'bossScrapy'
    allowed_domains = ['zhipin.com']
    host ='https://www.zhipin.com'
    start_urls = ['https://www.zhipin.com/c101010100-p100109/',
                     'https://www.zhipin.com/c101020100-p100109/',
                     'https://www.zhipin.com/c101110100-p100109/',
                     'https://www.zhipin.com/c101270100-p100109/']



    '''
     create by: lxl
     description: 解析列表页数据，并判断是否存在下一个
     create time: 2019-03-25 18:55  
     @:paramter:
     @:return 
     '''
    def parse(self, response):
        #print(response.xpath('//h3[@class="name"]/a[starts-with(@href ,"/job_detail")]//@href').extract_first())
        for url in response.xpath('//h3[@class="name"]/a[starts-with(@href ,"/job_detail")]//@href').extract():
            yield scrapy.Request(self.host+url,callback=self.parse_detail)

        next_page_url = response.xpath('//a[@class="next"]//@href').extract_first()

        if next_page_url:
            yield scrapy.Request(self.host+next_page_url,callback=self.parse)

    def parse_detail(self,response):
        item= BosscrapyItem()
        item['name'] = response.xpath('//h1/text()').extract_first()
        item['salary'] = response.xpath('//span[@class="salary"]/text()').extract_first().replace('\n',"").strip()
        item['profession'] =response.xpath('//div[@class="info-primary"]/p/text()').extract()[2]
        item['experience'] =response.xpath('//div[@class="info-primary"]/p/text()').extract()[1]
        item['welfare']  = ','.join(response.xpath('//div[@class="job-tags"]/span/text()').extract())
        tempjob = "".join(response.xpath('//div[@class="text"]/text()').extract()).split()
        item['job'] =''.join(tempjob)
        item['city'] =response.xpath('//div[@class="info-primary"]/p/text()').extract_first()
        yield item