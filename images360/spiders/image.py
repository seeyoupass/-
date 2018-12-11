# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from scrapy import Request
import json
from images360.items import Images360Item
from scrapy import Spider


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']

    def start_requests(self):
        data = {
            'ch': 'beauty',

            'isttype': 'new',
            'temp': 1
        }
        base_url = 'http://image.so.com/zj?'
        for page in range(0,10):
            data['sn'] = page*30
            params = urlencode(data)
            url = base_url + params
            yield Request(url,self.parse)

    def parse(self, response):
        item = Images360Item()
        data = json.loads(response.text)
        for images in data['list']:
            item['id'] = images.get('imageid')
            item['thumb'] = images.get('qhimg_thumb_url')
            item['url'] = images.get('qhimg_url')
            item['title'] = images.get('group_title')
            yield item