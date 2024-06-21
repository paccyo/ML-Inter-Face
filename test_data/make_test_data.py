from icrawler.builtin import BingImageCrawler
import os

n = 3

os.makedirs(f'data{n}/cat', exist_ok=True)
os.makedirs(f'data{n}/dog', exist_ok=True)

if n == 3:
    os.makedirs(f'data{n}/bear', exist_ok=True)


crawler = BingImageCrawler(storage = {'root_dir' : f'data{n}/cat'})
crawler.crawl(keyword = '猫', max_num = 100)

crawler = BingImageCrawler(storage = {'root_dir' : f'data{n}/dog'})
crawler.crawl(keyword = '犬', max_num = 100)

if n == 3:
    crawler = BingImageCrawler(storage = {'root_dir' : f'data{n}/bear'})
    crawler.crawl(keyword = '熊', max_num = 100)
