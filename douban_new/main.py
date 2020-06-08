from scrapy import cmdline
# # cmdline.execute(r'scrapy crawl collect_book -o 02collectbook.json'.split())
cmdline.execute(r'scrapy crawl user_wishbook -o 02wish_book.json'.split())
# # cmdline.execute('scrapy crawl followsites'.split())
