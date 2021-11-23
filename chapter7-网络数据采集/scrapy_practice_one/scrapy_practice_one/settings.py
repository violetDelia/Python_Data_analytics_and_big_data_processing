# Scrapy settings for scrapy_practice_one project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


'''
框架配置文件
'''

BOT_NAME = 'scrapy_practice_one'

SPIDER_MODULES = ['scrapy_practice_one.spiders']
NEWSPIDER_MODULE = 'scrapy_practice_one.spiders'

ITEM_PIPELINES={'scrapy_practice_one.pipelines.ScrapyPracticeOnePipeline': 300}


'''
配置Headers应对反爬虫,不同浏览器有不同的规则.
'''
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_practice_one (+http://www.yourdomain.com)'

'''
禁用robots协议
'''
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

'''
延迟下载,取消DOWNLOAD_DELAY注释
'''
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

'''
配置Headers应对发爬虫,添加'User-Agent'属性,会覆盖所有http请求
'''
# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#   'User-Agent':'需要的信息'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapy_practice_one.middlewares.ScrapyPracticeOneSpiderMiddleware': 543,
# }
'''
启用中间件,key值0~1000之间,不用设为NONE
'''
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrapy_practice_one.middlewares.ScrapyPracticeOneDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'scrapy_practice_one.pipelines.ScrapyPracticeOnePipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
'''
自动限速:取消AUTOTHROTTLE_ENABLED注释
'''
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
'''
使用中间件:
    (1).创建USER_AGENT列表.
        USER_AGENTS=['','']
    (2).创建User-Agent中间件
        在middlewares中
    (3).创建IP地址
        IP_LIST=["",""]
    (4).创建HTTP代理中间件
        在middlewares中
    (5).启动中间件
        取消DOWNLOADER_MIDDLEWARES注释,并将中间件写入
    

'''
USER_AGENTS=['','']
IP_LIST=["",""]
