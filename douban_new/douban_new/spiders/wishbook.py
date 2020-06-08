# -*- coding: utf-8 -*-
import scrapy
import re

class UserWishbookSpider(scrapy.Spider):
    name = 'user_wishbook'
    allowed_domains = ['douban.com','book.douban.com']

    def start_requests(self):
        # for i in  open('E:/failed_url_02', encoding='utf-8').readlines()[0:100001]:
            # user_id = i.strip()
            # url = 'https://book.douban.com/people/{}/wish'.format(user_id)
        for i in open('E:/failed_url_02.txt', encoding='utf-8').readlines():
            url = i.strip()
            yield scrapy.Request(
                url,
                callback=self.parse,
            )

    def parse(self, response):
        url = response.url
        user_id = re.findall(r'https://book.douban.com/people/(.*)/wish', url)[0]
        li_list = response.xpath('//ul[@class="interest-list"]/li')
        info = {}
        books = []
        for li in li_list:
            books_name = li.xpath('./div[@class="info"]/h2/a/@title').extract_first()
            books.append(books_name)
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



