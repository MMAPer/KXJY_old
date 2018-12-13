from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, reverse
from kxjy.settings import db
import json
from bson import json_util
from common.auth import cookie_auth

# Create your views here.
# 视图函数的第一个参数必须是request，这个参数绝对不能少
# 视图函数返回值必须是'django.http.response.HttpResponseBase'的子类的对象


#  获取目前全部场馆类别信息（二级目录）
@cookie_auth
def getVenues(request):
    res = {}
    venue_collection = db.venue
    venues = list(venue_collection.find())
    res["data"] = venues
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


#  获取一级目录
def getVenuesLabel(request):
    res = {}
    venue_collection = db.venue
    venues = list(venue_collection.find(projection={'name': True}))
    res["data"] = venues
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


#  获取指定一级目录下的二级目录
def getVenuesByLabel(request, label_name):
    print(label_name)
    res = {}
    venue_collection = db.venue
    venue = venue_collection.find_one({'name': label_name}, projection={'items':True})
    res["data"] = venue
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


#  添加一级目录
def addVenueLabel(request):
    pass


#  向指定一级目录中添加二级目录
def addVenueByLabel(request, label_name):
    pass


#  修改一级目录


#  修改指定一级目录下的二级目录


#  删除一级目录


#  删除指定一级目录下的二级目录

