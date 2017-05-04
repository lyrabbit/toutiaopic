# -*- coding: utf-8 -*-
import scrapy
import json,re
from ScrapyToutiaoPic.items import ScrapypicItem
class ToutiaoSpider(scrapy.Spider):
    name = "toutiao"
    allowed_domains = ["toutiao.com"]
    start_urls = 'http://www.toutiao.com/search_content/?offset={offset}&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count={count}&cur_tab=1'

    # def parse(self, response):
    #     pass

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls.format(offset=0, count=20),callback=self.pic_detail)

    def pic_detail(self,response):
        try:
            try:
                  response_text = json.loads(response.text)["data"]
                  item = ScrapypicItem()
                  for text in response_text:
                      for image_url in text['image_list']:
                          item["front_image_url"] = [image_url['url']]
                          yield item
                  if json.loads(response.text)["has_more"]==1:
                      offset = json.loads(response.text)["offset"]
                      yield scrapy.Request(url=self.start_urls.format(offset=offset, count=20), callback=self.pic_detail)
            except Exception as e:
                print u"无图片"
        except Exception as e:
            print e,u"链接请求失败"






