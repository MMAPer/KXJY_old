from pymongo import MongoClient
import json
from bson import json_util
from common.utils import md5

ids = ["img_01","img_02","img_03"]
print([list((id,i) for i in range(2) for id in ids)])