# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random


class Images360SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Images360DownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self):
        self.user_agents =["Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
        ]
        self.proxies = ['http://219.234.5.128:3128',
                        'http://124.243.226.18:8888',
                        'http://123.132.232.254:37638',
                        'http://61.135.217.7:80',
                        'http://222.128.9.235:59593',
                        'http://118.190.94.224:9001',
                        'http://121.33.220.158:808',
                        'http://61.160.247.63:808',
                        'http://58.53.128.83:3128',
                        'http://222.171.251.43:40149',
                        'http://171.37.162.16:8123',
                        'http://110.189.152.86:52277',
                        'http://120.79.174.103:8118',
                        'http://112.252.152.152:8118',
                        'http://27.17.45.90:43411',
                        'http://61.176.223.7:58822',
                        'http://221.224.136.211:35101',
                        'http://14.118.135.10:808',
                        'http://118.187.58.34:53281',
                        'http://112.242.67.236:8118',
                        'http://117.114.149.66:53281',
                        'http://106.15.42.179:33543',
                        'http://220.164.126.62:47701',
                        'http://60.191.201.38:45461',
                        'http://61.135.155.82:443',
                        'http://139.129.207.72:808',
                        'http://221.218.102.146:33323',
                        'http://58.210.136.83:52570',
                        'http://111.160.236.84:39692',
                        'http://27.54.248.42:8000',
                        'http://14.204.20.95:8080',
                        'http://180.164.24.165:53281',
                        'http://101.132.142.124:8080',
                        'http://219.238.186.188:8118',
                        'http://58.215.140.6:8080',
                        'http://221.210.120.153:54402',
                        'http://202.104.113.35:53281',
                        'http://106.12.7.54:8118',
                        'http://58.218.201.188:58093',
                        'http://113.12.202.50:40498',
                        'http://218.76.253.201:61408',
                        'http://58.240.7.195:32617',
                        'http://221.239.86.26:46164',
                        'http://124.193.135.242:54219',
                        'http://123.7.61.8:53281',
                        'http://113.69.137.222:8118',
                        'http://183.63.123.3:56489',
                        'http://114.119.116.92:61066',
                        'http://121.31.194.148:8123',
                        'http://183.47.2.201:30278',
                        'http://116.113.27.170:47849',
                        'http://119.1.97.193:60916',
                        'http://116.7.176.75:8118',
                        'http://110.84.208.56:8118',
                        'http://117.21.191.151:61007',
                        'http://175.148.71.128:1133',
                        'http://119.254.94.95:43150',
                        'http://121.31.194.214:8123',
                        'http://27.24.215.49:57248',
                        'http://118.122.92.252:37901',
                        'http://180.104.107.46:45700',
                        'http://58.240.224.252:33035',
                        'http://183.3.150.210:41258',
                        'http://221.214.180.122:33190',
                        'http://182.111.64.7:41766',
                        'http://182.88.187.62:8123',
                        'http://111.75.223.9:35918',
                        'http://110.87.24.206:6666',
                        'http://116.236.98.78:43682',
                        'http://117.21.191.154:32431',
                        'http://221.227.31.84:8123',
                        'http://118.89.138.129:52699',
                        'http://222.191.243.187:42649',
                        'http://27.154.34.146:31527',
                        'http://42.176.36.251:37000',
                        'http://123.190.76.50:53281',
                        'http://42.48.118.106:50038',
                        'http://113.107.173.92:55320',
                        'http://59.45.168.235:42059',
                        'http://113.108.242.36:47713',
                        'http://218.25.131.121:47043',
                        'http://61.145.69.27:42380',
                        'http://119.254.94.114:45691',
                        'http://118.181.226.22:37346',
                        'http://124.232.133.201:30819',
                        'http://125.73.220.18:31036',
                        'http://113.206.17.85:8118',
                        'http://218.59.228.18:61976',
                        'http://119.254.94.71:42788',
                        'http://112.84.85.164:8118',
                        'http://182.88.214.170:8123',
                        'http://115.46.79.75:8123',
                        'http://211.152.33.24:48749',
                        'http://116.192.171.51:48565',
                        'http://113.59.59.73:35683',
                        'http://101.27.22.144:61234',
                        'http://221.1.200.242:38652',
                        'http://219.234.181.194:33695',
                        'http://101.204.21.247:8118',
                        'http://202.103.12.30:60850']


    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        #request.headers['User-Agent'] = random.choice(self.user_agents)
        #request.meta['proxy'] = random.choice(self.proxies)
        referer = request.url
        if referer:
            request.headers['referer'] = referer


    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
