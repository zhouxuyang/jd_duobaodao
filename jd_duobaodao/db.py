#!/usr/bin/env python

# -*- encoding: utf-8 -*-
import pymysql
import logging

from peewee import MySQLDatabase,Model,CharField,DateTimeField

db = MySQLDatabase("duobaodao",host='192.168.2.216',port=3306,user='duobaodao', passwd='123456', charset='utf8')

class Product(Model):
    brandId = CharField()
    brandName = CharField()
    cappedPrice = CharField()
    category1 = CharField()
    category1Name = CharField()
    category2 = CharField()
    category2Name = CharField()
    category3 = CharField()
    category3Name = CharField()
    currentPrice = CharField()
    endTime = CharField()
    id = CharField()
    maxPrice = CharField()
    minPrice = CharField()
    primaryPic = CharField()
    productName = CharField()
    productType = CharField()
    quality = CharField()
    recordCount = CharField()
    reminding = CharField()
    shopId = CharField()
    shopName = CharField()
    size = CharField()
    spectatorCount = CharField()
    startPrice = CharField()
    startTime = CharField()
    status = CharField()
    usedNo = CharField()
    create_day = DateTimeField()
    class Meta:
        database = db
        db_table='tb_ods_product_base_day'

class Price(Model):
    auctionId = CharField()
    auctionRecordId = CharField()
    currentPrice = CharField()
    num = CharField()
    currentBidder = CharField()
    bidderNickName = CharField()
    bidderImage = CharField()
    status = CharField()
    offerPrice = CharField()
    class Meta:
        database = db
        db_table='tb_ods_product_price_day'


#
# class DB_MySQL():
#     '''数据库操作类'''
#     HOST = '192.168.2.216'
#     DBNAME = 'duobaodao'
#     USER = 'duobaodao'
#     PASSWD = '123456'
#     PORT = '3306'
#     CHARSET = 'utf8'
#
#     def __init__(self):
#         self.conn = pymysql.connect(host=self.HOST, port=int(self.PORT), user=self.USER, passwd=self.PASSWD,
#                                     db=self.DBNAME, charset=self.CHARSET)
#         self.cur = self.conn.cursor()
#
#     # 插入数据
#     def insert(self, item, table_name):
#         try:
#             fields = item.keys()
#             sql = 'insert into %s(%s) value(%s)' % (table_name, ','.join(fields), ','.join(['%s'] * len(fields)))
#             self.cur.execute(sql, [item[x] for x in fields])
#             self.conn.commit()
#         except Exception as e:
#             logging.error('mysql插入数据执行异常: %s' % str(e))
#
#     # 判断url是否已经存在
#     def url_is_exist(self, url, table_name):
#         try:
#             sql = 'select 1 from ' + table_name + ' where orig_url = %s limit 1'
#             if self.cur.execute(sql, (url,)):
#                 return True
#             else:
#                 return False
#         except Exception as e:
#             logging.error('mysql查询orig_url是否存在执行异常: ' + str(e))
#
#     def close(self):
#         self.cur.close()
#         self.conn.close()
#
#
# db_mysql = DB_MySQL()
