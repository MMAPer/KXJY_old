from pymongo import MongoClient
import json
from bson import json_util
from common.utils import md5

client = MongoClient("mongodb://serp:serp123456@127.0.0.1:27017")
db = client.serp

user_collection = db.user
user = user_collection.find_one({'username': 'serp', 'password': 'serp123456'})
if user:
    token = md5('serp')
    user['token'] = token
    user_collection.update({'username': 'serp', 'password': 'serp123456'}, user)