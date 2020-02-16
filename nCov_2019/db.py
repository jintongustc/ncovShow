"""
@ProjectName: DXY-2019-nCov-Crawler
@FileName: db.py
@Author: Jiabao Lin
@Date: 2020/1/21
"""
from pymongo import MongoClient


#uri = '**Confidential**'
#client = MongoClient(uri)
#db = client['2019-nCoV']

client = MongoClient("mongodb+srv://ncov:ncov@cluster0-cyayk.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('ncov')

class DB:
    def __init__(self):
        self.db = db

    def insert(self, collection, data):
        self.db[collection].insert(data)

    def find_one(self, collection, data=None):
        return self.db[collection].find_one(data)
