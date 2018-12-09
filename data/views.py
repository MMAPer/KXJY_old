from bson import json_util
from django.http import JsonResponse
from django.shortcuts import render
from kjjy.settings import db

# Create your views here.


def getDatas(request):
    res = {}
    data_collection = db.data
    datas = list(data_collection.find())
    res["data"] = datas
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


def getDataByLabelAndName(request, labelName, itemName):
    res = {}
    data_collection = db.data
    datas = list(data_collection.find({"name": labelName, "item": itemName}))
    res["data"] = datas
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})