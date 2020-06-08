# -*- coding: utf-8 -*-

import scrapy
import random
import re
from scrapy.utils.project import get_project_settings
settings = get_project_settings()

class ReadingBookSpider(scrapy.Spider):
    name = 'reading_book'
    allowed_domains = ['douban.com', 'book.douban.com']

    def start_requests(self):
        for i in open('E:/res_id_02').readlines():
            user_id = i.strip()
            url = 'https://book.douban.com/people/{}/do'.format(user_id)
            yield scrapy.Request(
                url,
                callback=self.parse,
            )

    def parse(self, response):
        current_url = response.url
        user_id = re.findall(r'https://book.douban.com/people/(.*)/do', current_url)[0]
        info = {}
        li_list = response.xpath('//ul[@class="interest-list"]/li')
        books = []
        for li in li_list:
            books_name = li.xpath('./div[@class="info"]/h2/a/@title').extract_first()
            books.append(books_name)
        info[user_id] = books
        yield info
        has_next = response.xpath('//div[@class="paginator"]/span[@class="next"]/a')
        if has_next:
            next_url = response.xpath('//div[@class="paginator"]/span[@class="next"]/a/@href').extract_first()
            next_url = 'https://book.douban.com/' + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,
            )
