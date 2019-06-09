# -*- coding: utf-8 -*-
import scrapy
from jd_duobaodao.db import Product, Price
from jd_duobaodao.items import PriceItem
from urllib.parse import urlencode, urlparse, parse_qs
import datetime
import json


class GetproductpriceSpider(scrapy.Spider):
    name = 'getproductprice'
    allowed_domains = ['jd.com']
    get_price_url = 'https://used-api.jd.com/auctionRecord/batchCurrentInfo?auctionId=%s&callback=__jp12'

    def start_requests(self):
        day_id = datetime.date.today() + datetime.timedelta(days=-1)
        products = Product.select(Product.id, Product.create_day).where(Product.create_day.cast('date') == day_id)
        for product in products:
            yield scrapy.Request(url=self.get_price_url % product.id, callback=self.parse)

    def parse(self, response):
        # 解析请求内容
        n1 = response.text.find('(')
        rej = json.loads(response.text[n1 + 1:-2])
        # 查询成功
        if rej['code'] == 200:
            data = rej['data']
            parse = parse_qs(urlparse(response.url).query, True)
            id = parse['auctionId'][0]
            data = data[id]
            item = PriceItem()
            item['auctionId'] = data['auctionId']
            item['auctionRecordId'] = data['auctionRecordId']
            item['currentPrice'] = data['currentPrice']
            item['num'] = data['num']
            item['currentBidder'] = data['currentBidder']
            item['bidderNickName'] = data['bidderNickName']
            item['bidderImage'] = data['bidderImage']
            item['status'] = data['status']
            item['offerPrice'] = data['offerPrice']
        yield item
