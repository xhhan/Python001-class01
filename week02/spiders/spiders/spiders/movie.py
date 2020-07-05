import scrapy
from bs4 import BeautifulSoup as bs
from lxml import etree as et


from spiders.items import SpidersItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        et_html = et.HTML(response.text)
        for selector in response.xpath('//div[@class="movie-hover-info"]')[:10]:
            item = SpidersItem()
            item['film_name'] = selector.xpath('./div[1]/span[1]/text()').extract_first().strip()
            item['film_type'] = selector.xpath('./div[2]/text()[2]').extract_first().strip()
            item['file_date'] = selector.xpath('./div[4]/text()[2]').extract_first().strip()
            yield item
        # for i in range(1, 5):
        #     link_path = '//*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[1]/a/@href'
        #     print(i,link_path)
        #     print(i, et_html.xpath(link_path))
        #     film_link = "https://maoyan.com"+str(et_html.xpath(link_path)[0])
            #yield scrapy.Request(film_link, callback=self.parse2)



    # def parse2(self, response):
    #     items = []
    #     item = {}
    #     et_html = et.HTML(response.text)
    #     film_name_xpath = '/html/body/div[3]/div/div[2]/div[1]/h1/text()'
    #     film_type_xpath = '/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]/text()'
    #     film_date_xpath = '/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()'
    #     film_name = et_html.xpath(film_name_xpath)
    #     print(film_name,et_html)
    #     film_type = et_html.xpath(film_type_xpath)
    #     file_date = et_html.xpath(film_date_xpath)
    #     item['film_name'] = film_name
    #     item['film_type'] = film_type
    #     item['file_date'] = file_date
    #     items.append(item)
    #     print(items)
    #     return items
