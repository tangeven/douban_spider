# -*- coding: utf-8 -*-

# Scrapy settings for douban_new project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

user_id = open('E:/res_id_02', encoding='utf-8').readlines()
JOBDIR='douban_job'

BOT_NAME = 'douban_new'

SPIDER_MODULES = ['douban_new.spiders']
NEWSPIDER_MODULE = 'douban_new.spiders'

DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

# DOWNLOADER_CLIENTCONTEXTFACTORY = 'douban_new.context.CustomContextFactory'

LOG_LEVEL = 'INFO'
# -*- coding: utf-8 -*-

# Scrapy settings for douban_top project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

FEED_EXPORT_ENCODING = 'utf-8'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban_top (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

DOWNLOAD_DELAY = 0.1

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 18
# CONCURRENT_REQUESTS_PER_IP = 1
# CONCURRENT_REQUESTS = 32
# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Referer': 'https://www.douban.com/people/{}/'.format(random.choice(open('E:/res_id_02', encoding='utf-8').readlines())),
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'douban_top.middlewares.DoubanTopSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'douban_new.middlewares.AbuyunProxy': 420,
    'douban_new.middlewares.RandomUserAgent': 421,
    'douban_new.middlewares.GetFailedUrl': 100,
    # 'douban_new.middlewares.RedisProxyMiddleWare': 420,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'douban_new.pipelines.DoubanNewPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



COOKIES_LIST = [
    {
    'bid': 'HVrw6Ob4SSs',
    'gr_user_id': 'e16a6755-9aa6-458c-9920-88d0b8c686d0',
    '__yadk_uid': '7N2gY7cS6FA940Gdwrer71QUUpR4d3RX',
    'll': '118171',
    'viewed': '34907855_34935067',
    'douban-fav-remind': '1',
    '__gads': 'ID=979d3a75789c6fde:T=1582507660:S=ALNI_MaVijLIcW5RiL52IBQwaw1YrQppIA',
    'push_doumail_num': '0',
    'push_noty_num': '0',
    '_ga': 'GA1.2.1488912142.1582501249',
    '_gid': 'GA1.2.850538002.1583677471',
    '__utma': '30149280.1488912142.1582501249.1583713530.1583714093.13',
    '__utmc': '30149280',
    '__utmz': '30149280.1583714093.13.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmt': '1',
    'dbcl2': '211816248:hPRHFUprajs',
    'ck': 'Dmoa',
    'ap_v': '0,6.0',
    '__utmt_douban': '1',
    '_pk_ses.100001.3ac3': '*',
    '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1583714165%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D',
    'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03': 'dce71472-f70e-48ca-a31d-9164ae34de12',
    'gr_cs1_dce71472-f70e-48ca-a31d-9164ae34de12': 'user_id%3A1',
    '__utmv': '30149280.21181',
    'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_dce71472-f70e-48ca-a31d-9164ae34de12': 'true',
    '_vwo_uuid_v2': 'D69092AF3F0E90894E2B529AA957F8005|053d77b45eb0ca51954e5bc10e4e71ee',
    '_pk_id.100001.3ac3': 'ab90154f17c77497.1582501270.7.1583714170.1583676870.',
    '__utmb': '30149280.8.10.1583714093',
},
    {
    'bid': 'HVrw6Ob4SSs',
    'gr_user_id': 'e16a6755-9aa6-458c-9920-88d0b8c686d0',
    '__yadk_uid': '7N2gY7cS6FA940Gdwrer71QUUpR4d3RX',
    'll': '118171',
    'viewed': '34907855_34935067',
    'douban-fav-remind': '1',
    '__gads': 'ID=979d3a75789c6fde:T=1582507660:S=ALNI_MaVijLIcW5RiL52IBQwaw1YrQppIA',
    'push_doumail_num': '0',
    'push_noty_num': '0',
    '_ga': 'GA1.2.1488912142.1582501249',
    '_gid': 'GA1.2.850538002.1583677471',
    '__utma': '30149280.1488912142.1582501249.1583713530.1583714093.13',
    '__utmc': '30149280',
    '__utmz': '30149280.1583714093.13.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmt': '1',
    'ap_v': '0,6.0',
    '__utmt_douban': '1',
    '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1583714165%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D',
    '_pk_ses.100001.3ac3': '*',
    'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03': 'dce71472-f70e-48ca-a31d-9164ae34de12',
    'gr_cs1_dce71472-f70e-48ca-a31d-9164ae34de12': 'user_id%3A1',
    'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_dce71472-f70e-48ca-a31d-9164ae34de12': 'true',
    '_vwo_uuid_v2': 'D69092AF3F0E90894E2B529AA957F8005|053d77b45eb0ca51954e5bc10e4e71ee',
    'dbcl2': '47872936:vEvQA0LZkbw',
    'ck': 'y5z_',
    '__utmv': '30149280.4787',
    '_pk_id.100001.3ac3': 'ab90154f17c77497.1582501270.7.1583714585.1583676870.',
    '__utmb': '30149280.16.10.1583714093',
},
    {
    'bid': 'HVrw6Ob4SSs',
    'gr_user_id': 'e16a6755-9aa6-458c-9920-88d0b8c686d0',
    '__yadk_uid': '7N2gY7cS6FA940Gdwrer71QUUpR4d3RX',
    'll': '118171',
    'viewed': '34907855_34935067',
    'douban-fav-remind': '1',
    '__gads': 'ID=979d3a75789c6fde:T=1582507660:S=ALNI_MaVijLIcW5RiL52IBQwaw1YrQppIA',
    'push_doumail_num': '0',
    'push_noty_num': '0',
    '_ga': 'GA1.2.1488912142.1582501249',
    '_gid': 'GA1.2.850538002.1583677471',
    '__utma': '30149280.1488912142.1582501249.1583713530.1583714093.13',
    '__utmc': '30149280',
    '__utmz': '30149280.1583714093.13.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    'ap_v': '0,6.0',
    '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1583714165%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D',
    '_pk_ses.100001.3ac3': '*',
    'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03': 'dce71472-f70e-48ca-a31d-9164ae34de12',
    'gr_cs1_dce71472-f70e-48ca-a31d-9164ae34de12': 'user_id%3A1',
    'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_dce71472-f70e-48ca-a31d-9164ae34de12': 'true',
    '_vwo_uuid_v2': 'D69092AF3F0E90894E2B529AA957F8005|053d77b45eb0ca51954e5bc10e4e71ee',
    'dbcl2': '3252709:Ivf+9k8i41Y',
    'ck': 'LDc_',
    '__utmt': '1',
    '__utmv': '30149280.325',
    '__utmt_douban': '1',
    '_pk_id.100001.3ac3': 'ab90154f17c77497.1582501270.7.1583714771.1583676870.',
    '__utmb': '30149280.22.10.1583714093',
},
    {
    'bid': 'HVrw6Ob4SSs',
    'gr_user_id': 'e16a6755-9aa6-458c-9920-88d0b8c686d0',
    '__yadk_uid': '7N2gY7cS6FA940Gdwrer71QUUpR4d3RX',
    'll': '118171',
    'viewed': '34907855_34935067',
    'douban-fav-remind': '1',
    '__gads': 'ID=979d3a75789c6fde:T=1582507660:S=ALNI_MaVijLIcW5RiL52IBQwaw1YrQppIA',
    'push_doumail_num': '0',
    'push_noty_num': '0',
    '_ga': 'GA1.2.1488912142.1582501249',
    '_gid': 'GA1.2.850538002.1583677471',
    '__utma': '30149280.1488912142.1582501249.1583713530.1583714093.13',
    '__utmc': '30149280',
    '__utmz': '30149280.1583714093.13.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    'ap_v': '0,6.0',
    '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1583714165%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D',
    '_pk_ses.100001.3ac3': '*',
    'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03': 'dce71472-f70e-48ca-a31d-9164ae34de12',
    'gr_cs1_dce71472-f70e-48ca-a31d-9164ae34de12': 'user_id%3A1',
    'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_dce71472-f70e-48ca-a31d-9164ae34de12': 'true',
    '_vwo_uuid_v2': 'D69092AF3F0E90894E2B529AA957F8005|053d77b45eb0ca51954e5bc10e4e71ee',
    '__utmt': '1',
    '__utmt_douban': '1',
    'dbcl2': '102909596:Ki1F+2u9ODg',
    'ck': 'Z8i2',
    '__utmv': '30149280.10290',
    '_pk_id.100001.3ac3': 'ab90154f17c77497.1582501270.7.1583714863.1583676870.',
    '__utmb': '30149280.28.10.1583714093',
},
    {
    'bid': 'HVrw6Ob4SSs',
    'gr_user_id': 'e16a6755-9aa6-458c-9920-88d0b8c686d0',
    '__yadk_uid': '7N2gY7cS6FA940Gdwrer71QUUpR4d3RX',
    'll': '118171',
    'viewed': '34907855_34935067',
    'douban-fav-remind': '1',
    '__gads': 'ID=979d3a75789c6fde:T=1582507660:S=ALNI_MaVijLIcW5RiL52IBQwaw1YrQppIA',
    'push_doumail_num': '0',
    'push_noty_num': '0',
    '_ga': 'GA1.2.1488912142.1582501249',
    '_gid': 'GA1.2.850538002.1583677471',
    '__utma': '30149280.1488912142.1582501249.1583713530.1583714093.13',
    '__utmc': '30149280',
    '__utmz': '30149280.1583714093.13.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    'ap_v': '0,6.0',
    '_pk_ses.100001.3ac3': '*',
    '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1583714165%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D',
    'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03': 'dce71472-f70e-48ca-a31d-9164ae34de12',
    'gr_cs1_dce71472-f70e-48ca-a31d-9164ae34de12': 'user_id%3A1',
    'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_dce71472-f70e-48ca-a31d-9164ae34de12': 'true',
    '_vwo_uuid_v2': 'D69092AF3F0E90894E2B529AA957F8005|053d77b45eb0ca51954e5bc10e4e71ee',
    '__utmt': '1',
    '__utmt_douban': '1',
    'dbcl2': '2795029:4VMdomPs50w',
    'ck': 'q7yU',
    '__utmv': '30149280.279',
    '_pk_id.100001.3ac3': 'ab90154f17c77497.1582501270.7.1583715029.1583676870.',
    '__utmb': '30149280.35.10.1583714093',
}
]

RETRY_ENABLED = True              # 默认开启失败重试，一般关闭
RETRY_TIMES = 3                         # 失败后重试次数，默认两次
HTTP_CODES = [500, 502, 503, 504, 522, 524, 408]    # 碰到这些验证码，才开启重试


# REDIRECT_ENABLED = False
# HTTPERROR_ALLOWED_CODES = [301,403,302]




