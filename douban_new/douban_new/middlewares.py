# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import redis
import base64
import random
import requests
import json
from fake_useragent import UserAgent

import time

from scrapy.utils.project import get_project_settings
settings = get_project_settings()
from twisted.internet.defer import DeferredLock
from OpenSSL import SSL
from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.downloadermiddlewares.redirect import RedirectMiddleware

# 代理服务器
proxyServer = "http://http-dyn.abuyun.com:9020"
proxyUser = "H8R5F1Q199813JGD"
proxyPass = "426AC2BDC1A4DF33"

# 代理隧道验证信息
# proxyUser = "H26R2B3Z19691VND"
# proxyPass = "8A5DE76C56D2E1CC"



proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")



class AbuyunProxy(object):

    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth

    def process_response(self, request, response, spider):
        if response.status in [403,302,301]:
            return request
        return response


class RandomUserAgent(object):
    def process_request(self,request,spider):
        UA = UserAgent(use_cache_server=False, verify_ssl=False).random
        request.headers['User-Agent'] = UA



class GetFailedUrl(object):

    def __init__(self):
        self.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))

    def process_response(self, request, response, spider):
        if response.status in self.retry_http_codes:
            # 将爬取失败的URL存下来，你也可以存到别的存储
            with open('E:/'+str(spider.name) + "new" + ".txt", "a") as f:
                f.write(response.url + "\n")
            return response
        return response

    def process_exception(self, request, exception, spider):
        with open('E:/' + 'failed_url_02' + ".txt", "a") as f:
            f.write(request.url + "\n")


class DailiyunProxy():
    def process_request(self,request,spider):
        resp = requests.get(
            'http://tangnaifu.v4.dailiyun.com/query.txt?key=NP077E4FFA&word=&count=1&rand=false&detail=false')
        proxy_meta = 'https://' + resp.text
        request.meta["proxy"] = proxy_meta

    def process_response(self, request, response, spider):
        if response.status != 200:
            return request
        return response






class FreeProxyMiddware(object):
    def __init__(self):
        self.proxypool_url = 'http://127.0.0.1:5555/random'
        self.lock = DeferredLock()
        self.current_proxy = None

    def get_random_proxy(self):
        self.lock.acquire()
        tmp_proxy = requests.get(self.proxypool_url).text.strip()
        res_proxy = 'https://{}'.format(tmp_proxy)
        print(res_proxy)
        self.lock.release()
        return res_proxy


    def process_request(self,request,spider):
        if not self.current_proxy:
            res_proxy = self.get_random_proxy()
            self.current_proxy = res_proxy
        request.meta["proxy"] = self.current_proxy

    def process_response(self, request, response, spider):
        if response.status != 200:
            self.current_proxy = self.get_random_proxy()
            return request
        return response


class FreeNewProxyMiddware(object):
    def __init__(self):
        self.proxypool_url = 'http://127.0.0.1:5010/get/'
        self.lock = DeferredLock()
        self.current_proxy = None

    def get_random_proxy(self):
        # self.lock.acquire()
        tmp_proxy = requests.get(self.proxypool_url).text.strip()
        new_proxy = json.loads(tmp_proxy)['proxy']
        res_proxy = 'https://{}'.format(new_proxy)
        # self.lock.release()
        return res_proxy

    def process_request(self,request,spider):
        if 'proxy' not in request.meta:
            res_proxy = self.get_random_proxy()
            self.current_proxy = res_proxy
        request.meta["proxy"] = self.current_proxy

    def process_response(self, request, response, spider):
        if response.status in [403,302,301]:
            self.current_proxy = self.get_random_proxy()
            return request
        return response



class CustomContextFactory(ScrapyClientContextFactory):
    """
    Custom context factory that allows SSL negotiation.
    """

    def __init__(self):
        # Use SSLv23_METHOD so we can use protocol negotiation
        self._ssl_method = SSL.SSLv23_METHOD



class RedisProxyMiddleWare(object):
    def __init__(self):
        self.port = redis.Redis(host='127.0.0.1', port=6379)
        self.lock = DeferredLock()
        self.current_proxy = None

    def get_proxy(self):
        res = self.port.keys()
        return res

    def get_random_proxy(self):
        tmp_proxy = random.choice(self.port.keys())
        res_proxy = tmp_proxy.decode('utf-8')
        return res_proxy


    def process_request(self,request,spider):
        self.current_proxy = self.get_random_proxy()
        request.meta["proxy"] = self.current_proxy


    def process_response(self, request, response, spider):
        if response.status in [403,301,302]:
            self.current_proxy = self.get_random_proxy()
            with open('E:/' + 'failed_redirect_url' + ".txt", "a") as f:
                f.write(request.url + "\n")
        return response




