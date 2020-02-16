"""
@ProjectName: DXY-2019-nCov-Crawler
@FileName: crawler.py
@Author: Jiabao Lin
@Date: 2020/1/21
"""
from bs4 import BeautifulSoup
from service.db import DB

import re
import json
import time
import logging
import datetime
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}


class Crawler:
    def __init__(self):
        self.session = requests.session()
        self.session.headers.update(headers)
        self.db = DB()
        self.crawl_timestamp = int()

    def run(self):
        while True:
            self.crawler()
            time.sleep(10)

    def crawler(self):
        while True:
            self.crawl_timestamp = int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)
            try:
                r = self.session.get(url='https://3g.dxy.cn/newh5/view/pneumonia')
            except requests.exceptions.ChunkedEncodingError:
                continue
            soup = BeautifulSoup(r.content, 'lxml')

            overall_information = re.search(r'\{("id".*?)\]\}', str(soup.find('script', attrs={'id': 'getStatisticsService'})))
            province_information = re.search(r'\[(.*?)\]', str(soup.find('script', attrs={'id': 'getListByCountryTypeService1'})))
            area_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getAreaStat'})))
            abroad_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getListByCountryTypeService2'})))
            news = re.search(r'\[(.*?)\]', str(soup.find('script', attrs={'id': 'getTimelineService'})))

            if not overall_information or not province_information or not area_information or not news:
                continue

            self.overall_parser(overall_information=overall_information)
            self.province_parser(province_information=province_information)
            self.area_parser(area_information=area_information)
            self.abroad_parser(abroad_information=abroad_information)

            break

        logger.info('Successfully crawled.')

    def overall_parser(self, overall_information):
        overall_information = json.loads(overall_information.group(0))

        overall = {}
        overall['modifyTime'] = overall_information['modifyTime']
        overall['currentConfirmedCount'] = overall_information['currentConfirmedCount']
        overall['confirmedCount'] = overall_information['confirmedCount'] 
        overall['suspectedCount'] = overall_information['suspectedCount']
        overall['curedCount'] = overall_information['curedCount'] 
        overall['deadCount'] = overall_information['deadCount'] 
        overall['seriousCount'] = overall_information['seriousCount']
        

        if not self.db.find_one(collection='DXYOverall', data=overall):
            overall['updateTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYOverall', data=overall)

    def province_parser(self, province_information):
        provinces = json.loads(province_information.group(0))
        for province in provinces:
            data_upload = {}
            data_upload['provinceId'] = province['provinceId']
            data_upload['provinceName'] = province['provinceName']
            data_upload['provinceShortName'] = province['provinceShortName']
            
            data_upload['modifyTime'] = province['modifyTime']
            data_upload['currentConfirmedCount'] = province['currentConfirmedCount']
            data_upload['confirmedCount'] = province['confirmedCount'] 
            data_upload['suspectedCount'] = province['suspectedCount']
            data_upload['curedCount'] = province['curedCount'] 
            data_upload['deadCount'] = province['deadCount'] 
            if self.db.find_one(collection='DXYProvince', data=data_upload):
                continue
            data_upload['updateTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYProvince', data=data_upload)


    def area_parser(self, area_information):
        area_information = json.loads(area_information.group(0))
        for area in area_information:
            area.pop('comment')
            area.pop('locationId')
            if self.db.find_one(collection='DXYArea', data=area):
                continue
            area['country'] = '中国'
            area['updateTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYArea', data=area)

    def abroad_parser(self, abroad_information):
        countries = json.loads(abroad_information.group(0))
        for country in countries:
            data_upload = {}
            data_upload['countryName'] = country['provinceName']
            data_upload['countryShortName'] = country['provinceShortName']
            data_upload['continents'] = country['continents']
            data_upload['modifyTime'] = country['modifyTime']
            data_upload['currentConfirmedCount'] = country['currentConfirmedCount']
            data_upload['confirmedCount'] = country['confirmedCount'] 
            data_upload['suspectedCount'] = country['suspectedCount']
            data_upload['curedCount'] = country['curedCount'] 
            data_upload['deadCount'] = country['deadCount'] 
            if self.db.find_one(collection='DXYAbroad', data=data_upload):
                continue
            data_upload['updateTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYAbroad', data=data_upload)

    

if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
