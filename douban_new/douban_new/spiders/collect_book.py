# -*- coding: utf-8 -*-

import scrapy
import random
import re
from scrapy.utils.project import get_project_settings
settings = get_project_settings()

class CollectBookSpider(scrapy.Spider):
    name = 'collect_book'
    allowed_domains = ['douban.com']
    start_urls = ['https://douban.com/']

    def start_requests(self):
        filepath = ''
        # filepath = '' 文件路径，保存了所有用户的id
        for i in  open(filepath, encoding='utf-8').readlines():
            user_id = i.strip()
            url = 'https://book.douban.com/people/{}/collect'.format(user_id)
            yield scrapy.Request(
                url,
                callback=self.parse,
            )

    def parse(self, response):
        current_url = response.url
        user_id = re.findall(r'https://book.douban.com/people/(.*)/collect',current_url)[0]
        info = {}
        li_list = response.xpath('//ul[@class="interest-list"]/li')
        books = []
        for li in li_list:
            books_dict = {}
            books_name = li.xpath('./div[@class="info"]/h2/a/@title').extract_first()
            ratings = li.xpath('./div[@class="info"]/div[@class="short-note"]/div[1]/span[1]/@class').extract_first()
            if ratings:
                ratings = re.findall(r'\d',ratings)
            else:
                ratings = 'have_no_rates'
            books_dict[books_name] = ratings
            books.append(books_dict)
        info[user_id] = books
        yield info
        has_next = response.xpath('//div[@class="paginator"]/span[@class="next"]/a')
        if has_next:
            next_url = response.xpath('//div[@class="paginator"]/span[@class="next"]/a/@href').extract_first()
            next_url = 'https://book.douban.com' + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,
            )


