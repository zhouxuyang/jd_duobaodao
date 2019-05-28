# -*- coding: utf-8 -*-
import scrapy
import json
from jd_duobaodao.items import DuoBaoDaoItem
from urllib.parse import urlencode, urlparse, parse_qs
import math


class GetproductlistSpider(scrapy.Spider):
    name = 'getproductlist'
    allowed_domains = ['jd.com']
    base_url = 'https://used-api.jd.com/auction/list?pageNo=%s&pageSize=50&category1=&status=&orderDirection=1&orderType=1&callback=__jp0'

    def start_requests(self):
        yield scrapy.Request(self.base_url % 1, callback=self.parse)

    def parse(self, response):
        # 解析请求内容
        n1 = response.text.find('(')
        rej = json.loads(response.text[n1 + 1:-2])
        # 查询成功
        if rej['code'] == 200:
            data = rej['data']
            for product in data['auctionInfos']:
                item = DuoBaoDaoItem()
                item['brandId'] = product['brandId']
                item['brandName'] = product['brandName']
                item['cappedPrice'] = product['cappedPrice']
                item['category1'] = product['category1']
                item['category1Name'] = product['category1Name']
                item['category2'] = product['category2']
                item['category2Name'] = product['category2Name']
                item['category3'] = product['category3']
                item['category3Name'] = product['category3Name']
                item['currentPrice'] = product['currentPrice']
                item['endTime'] = product['endTime']
                item['id'] = product['id']
                item['maxPrice'] = product['maxPrice']
                item['minPrice'] = product['minPrice']
                item['primaryPic'] = product['primaryPic']
                item['productName'] = product['productName']
                item['productType'] = product['productType']
                item['quality'] = product['quality']
                item['recordCount'] = product['recordCount']
                item['reminding'] = product['reminding']
                item['shopId'] = product['shopId']
                item['shopName'] = product['shopName']
                item['size'] = product['size']
                item['spectatorCount'] = product['spectatorCount']
                item['startPrice'] = product['startPrice']
                item['startTime'] = product['startTime']
                item['status'] = product['status']
                item['usedNo'] = product['usedNo']
                yield item
            # 下一页
            parse = parse_qs(urlparse(response.url).query, True)
            current_page = int(parse['pageNo'][0])
            total_pages = math.ceil(data['totalNumber'] / 50)
            if current_page < total_pages:
                yield scrapy.Request(self.base_url % str(current_page + 1), callback=self.parse)
