from bson import json_util
from django.http import JsonResponse
from django.shortcuts import render
from kxjy.settings import db
from kxjy.status import StatusCode

# Create your views here.

# 获取所有数据
def getDatas(request):
    res = {}
    data_collection = db.data
    datas = list(data_collection.find())
    res["data"] = datas
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


# 获取指定类别指定场馆下面的展品数据
def getDataByLabelAndName(request, labelName, venueName):
    res = {}
    data_collection = db.data
    datas = list(data_collection.find({"name": labelName, "item": venueName}))
    res["data"] = datas
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


# 搜索数据（参数：展馆名称，展品名称）
def searchData(request):
    res = StatusCode.OK()
    venueName = request.GET.get("venue")  # 展馆名称
    itemName = request.GET.get("item")  # 展品名称
    data_collection = db.data
    datas = list(data_collection.find({"venue": {"$regex": venueName}, "item.name": {"$regex": itemName}}))
    res['length'] = len(datas)
    res['data'] = datas
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})