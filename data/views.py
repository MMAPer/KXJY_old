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
    datas = list(data_collection.find({"label": labelName, "venue": venueName}))
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


#  渲染数据详情页
def getDetailHtml(request, labelName, venueName, itemName):
    context = {}
    context['label'] = labelName
    context['venue'] = venueName
    context['item'] = itemName
    return render(request, 'back/data/admin_data_detail.html', context)


#  获取数据详情
def getDetailData(request, labelName, venueName, itemName):
    res = StatusCode.OK()
    data_collection = db.data
    data = data_collection.find_one({"label":labelName, "venue":venueName, "item.name":itemName})
    res['data'] = data
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})