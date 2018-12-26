import json
import os

from bson import json_util
from django.http import JsonResponse
from django.shortcuts import render

from common.auth import cookie_auth, permission_auth
from common.status import StatusCode
from kxjy import settings
from kxjy.settings import db


# Create your views here.

# 获取所有数据
def getDatas(request):
    res = StatusCode.OK()
    data_collection = db.data
    datas = list(data_collection.find())
    res["data"] = datas
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


# 获取指定类别下面的展品数据
def getDataByLabel(request, labelName):
    res = StatusCode.OK()
    data_collection = db.data
    datas = list(data_collection.find({"label": labelName}))
    res["data"] = datas
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


# 获取指定类别指定场馆下面的展品数据
def getDataByLabelAndName(request, labelName, venueName):
    res = StatusCode.OK()
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


def deleteData(request, labelName, venueName, itemName):
    res = StatusCode.OK()
    data_collection = db.data
    data_collection.delete_one({"label":labelName, "venue":venueName, "item.name":itemName})
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})

#  渲染添加数据页面
def getAddDataHtml(request):
    return render(request, 'back/data/admin_data_add.html')


def addData(request):
    res = StatusCode.OK()
    data = {}
    label = request.POST.get("label")
    venue = request.POST.get("venue")
    item = request.POST.get("item")
    item = json.loads(item)
    #  ri!! 踩了好多坑：前端：let data_obj = new FormData();
    #             for(i=0; i<this.imgList.length; i++)
    #             {
    #                 data_obj.append("imgList[]", this.imgList[i].file);
    #             }
    imgList = request.FILES.getlist("imgList[]")
    imgPath = []
    for i in range(len(imgList)):
        fname = os.path.join(settings.MEDIA_ROOT, imgList[i].name)
        furl = settings.MEDIA_URL+imgList[i].name
        imgPath.append(furl)
        with open(fname, 'wb') as pic:
            for c in imgList[i].chunks():
                pic.write(c)
    data["label"] = label
    data["venue"] = venue
    data["item"] = item
    data['imgList'] = imgPath
    data['videoList'] = []
    data_collection = db.data
    data_collection.insert(data)
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


# 渲染数据修改页面
def getUpdateDataHtml(request, labelName, venueName, itemName):
    context = {}
    context['label'] = labelName
    context['venue'] = venueName
    context['item'] = itemName
    return render(request, 'back/data/admin_data_update.html', context)


def updateData(request, labelName, venueName, itemName):
    res = StatusCode.OK()
    data = {}
    labelName = request.POST.get("label")
    venueName = request.POST.get("venue")
    item = request.POST.get("item")
    item = json.loads(item)
    imgOldList = json.loads(request.POST.get("imgOldList"))
    # #  ri!! 踩了好多坑：前端：let data_obj = new FormData();
    # #            j for(i=0; i<this.imgList.length; i++)
    # #             {
    # #                 data_obj.append("imgList[]", this.imgList[i].file);
    # #             }
    #
    imgList = request.FILES.getlist("imgList[]")
    imgPath = []
    for i in range(len(imgOldList)):
        imgPath.append(imgOldList[i])
    for i in range(len(imgList)):
        fname = os.path.join(settings.MEDIA_ROOT, imgList[i].name)
        furl = settings.MEDIA_URL+imgList[i].name
        imgPath.append(furl)
        with open(fname, 'wb') as pic:
            for c in imgList[i].chunks():
                pic.write(c)
    data["label"] = labelName
    data["venue"] = venueName
    data["item"] = item
    data['imgList'] = imgPath
    data['videoList'] = []
    data_collection = db.data
    data_collection.update_one({"label":labelName, "venue":venueName, "item.name":itemName},{"$set":data})
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})