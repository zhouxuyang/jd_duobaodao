# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from jd_duobaodao.db import Price,Product
from jd_duobaodao.items import ProductItem, PriceItem


class JdDuobaodaoPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, ProductItem):
            prod = Product(','.join(['%s="%s"' % (key, item[key]) for key in item.keys()]))
            prod.save()
        if isinstance(item, PriceItem):
            price = Price(','.join(['%s="%s"' % (key, item[key]) for key in item.keys()]))
            price.save()
        return item
