import scrapy
from bs4 import BeautifulSoup as bs
from lxml import etree as et


from spiders.items import SpidersItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['url=https://movie.douban.com/top250?start=0']

    def parse(self, response):
        items = []
        et_html = et(response.text)
        for i in range(1,10):
            link_path = '//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div['+str(i)+']/a/text'
            film_link = et_html.xpath(link_path)
            yield scrapy.Request(film_link, meta={"link": film_link}, callback=self.parse2)



    def parse2(self, response):
        item = response.meta['link']
        items = []
        et_html = et(response.text)
        film_name_xpath = '//*[@id="content"]/h1/span[1]/text'
        film_type_xpath = '//*[@id="info"]/span[5]/text'
        film_date_xpath = '//*[@id="info"]/span[11]/text'
        film_name = et_html.xpath(film_name_xpath)
        film_type = et_html.xpath(film_type_xpath)
        file_date = et_html.xpath(film_date_xpath)
        item['film_name'] = film_name
        item['film_type'] = film_type
        item['file_date'] = file_date
        items.append(item)
        yield items
