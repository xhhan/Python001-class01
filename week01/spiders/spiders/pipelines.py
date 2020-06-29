# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpidersPipeline:
    def process_item(self, item, spider):
        file_date = item['file_date']
        film_name = item['film_name']
        film_type = item['film_type']
        output = f'|{film_name}\t|{file_date}\t|{film_type}\t|'
        print(output)
        print("---------------------------------------\n")
        with open('maoyan.csv','a+', encoding='utf-8') as airtical:
            airtical.write(output)
            airtical.close()
        return item
