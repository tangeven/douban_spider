# -*- coding: utf-8 -*-
import scrapy
import re


class FollowsitesSpider(scrapy.Spider):
    name = 'followsites'
    allowed_domains = ['douban.com','book.douban.com']
    start_urls = ['http://douban.com/']

    def start_requests(self):
        for i in  open('E:/res_id_02', encoding='utf-8').readlines()[0:100001]:
            user_id = i.strip()
            url = 'https://book.douban.com/people/{}/minisite'.format(user_id)
            yield scrapy.Request(
                url,
                callback=self.parse,
            )

    def parse(self, response):
        current_url = response.url
        user_id = re.findall(r'https://book.douban.com/people/(.*)/minisite', current_url)[0]
        info = {}
        li_list = response.xpath('//ul[@class="user-list"]/li')
        sites = []
        for li in li_list:
            sites_name = li.xpath('./div[@class="info"]/h3/a/@title').extract_first()
            sites.append(sites_name)
        info[user_id] = sites
        yield info
        has_next = response.xpath('//div[@class="paginator"]/span[@class="next"]/a')
        if has_next:
            next_url = response.xpath('//div[@class="paginator"]/span[@class="next"]/a/@href').extract_first()
            next_url = 'https://book.douban.com' + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,
            )

