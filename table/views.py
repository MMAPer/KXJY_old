from bson import json_util
from django.http import JsonResponse
from django.shortcuts import render
from kxjy.settings import db
from kxjy.status import StatusCode

# Create your views here.


def getTableByLabelName(request, labelName):
    res = StatusCode.OK()
    table_collection = db.table
    table = table_collection.find_one({"label":labelName})
    res['data'] = table
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})