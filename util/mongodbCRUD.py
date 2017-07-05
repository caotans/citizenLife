#! usr/bin/python
# cording:utf-8
import pymongo
from pymongo import MongoClient
client=MongoClient('127.0.0.1',27017)
client = MongoClient('mongodb://10.0.0.9:27017/')
db=client.test_database
db.collection_names(include_system_collections=False)
posts=db.posts
posts.find_one()
print(posts.find_one())