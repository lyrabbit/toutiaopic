from scrapy.cmdline import execute

import sys,os

sys.path.append(os.path.dirname(os.path.abspath(__name__)))

execute(["scrapy","crawl","toutiao"])