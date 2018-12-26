from bson import json_util
from django.http import JsonResponse

from common.auth import cookie_auth,permission_auth
# Create your views here.
# 视图函数的第一个参数必须是request，这个参数绝对不能少
# 视图函数返回值必须是'django.http.response.HttpResponseBase'的子类的对象
#  获取目前全部场馆类别信息（二级目录）
from common.status import StatusCode
from kxjy.settings import db


def getVenues(request):
    res = {}
    venue_collection = db.venue
    venues = list(venue_collection.find({"status": 1}))
    res["data"] = venues
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


#  获取一级目录
def getVenuesLabel(request):
    res = {}
    venue_collection = db.venue
    venues = list(venue_collection.find({"status": 1}, projection={'label': True}))
    res["data"] = venues
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


#  获取指定一级目录下的二级目录
def getVenuesByLabel(request, label_name):
    print(label_name)
    res = {}
    venue_collection = db.venue
    venue = venue_collection.find_one({'label': label_name, "status": 1}, projection={'venues': True})
    res["data"] = venue
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


#  添加一级目录
def addLabel(request):
    res = StatusCode.OK()
    labelName = request.POST.get("label")
    venue_collection = db.venue
    venue_collection.insert({"label": labelName, "venues": [], "status": 1})
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


#  修改一级目录名称
def modifyLabel(request, originLabelName, labelName):
    res = StatusCode.OK()
    venue_collection = db.venue
    venue_collection.update_one({"label": originLabelName}, {"$set": {"label": labelName}})
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


#  删除一级目录（逻辑删除，设定status=0，不做物理删除）
def delLabel(request, labelName):
    res = StatusCode.OK()
    venue_collection = db.venue
    venue_collection.update_one({"label": labelName}, {"$set": {"status": 0}})
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


#  向指定一级目录中添加二级目录
def addVenueByLabel(request):
    res = StatusCode.OK()
    labelName = request.POST.get("label")
    venueName = request.POST.get("venue")
    venue_collection = db.venue
    venue_collection.update_one({"label": labelName}, {"$push": {"venues": venueName}})
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


#  删除指定一级目录下的二级目录
def delVenue(request, labelName, venueName):
    res = StatusCode.OK()
    venue_collection = db.venue
    venue_collection.update_one({"label": labelName}, {"$pull": {"venues": venueName}})
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


# 修改指定一级目录下的二级目录
def modifyVenue(request, labelName, originVenueName, venueName):
    res = StatusCode.OK()
    venue_collection = db.venue
    venue_collection.update_one({"label": labelName}, {"$pull": {"venues": originVenueName}})
    venue_collection.update_one({"label": labelName}, {"$pull": {"venues": venueName}})
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})
