# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdDuobaodaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DuoBaoDaoItem(scrapy.Item):
    brandId = scrapy.Field()
    brandName = scrapy.Field()
    cappedPrice = scrapy.Field()
    category1 = scrapy.Field()
    category1Name = scrapy.Field()
    category2 = scrapy.Field()
    category2Name = scrapy.Field()
    category3 = scrapy.Field()
    category3Name = scrapy.Field()
    currentPrice = scrapy.Field()
    endTime = scrapy.Field()
    id = scrapy.Field()
    maxPrice = scrapy.Field()
    minPrice = scrapy.Field()
    primaryPic = scrapy.Field()
    productName = scrapy.Field()
    productType = scrapy.Field()
    quality = scrapy.Field()
    recordCount = scrapy.Field()
    reminding = scrapy.Field()
    shopId = scrapy.Field()
    shopName = scrapy.Field()
    size = scrapy.Field()
    spectatorCount = scrapy.Field()
    startPrice = scrapy.Field()
    startTime = scrapy.Field()
    status = scrapy.Field()
    usedNo = scrapy.Field()
