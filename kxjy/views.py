import json
from bson import json_util
import time
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from common.utils import md5
from common.auth import salt, cookie_auth
from .settings import db


def login(request):
    # 未登录用户执行以下登录操作
    if request.method == 'POST':
        result = {}
        username = request.POST.get("username")
        password = md5(request.POST.get("password"))
        print(password)
        user_collection = db.user
        user = user_collection.find_one({'username': username, 'password': password})
        if user:
            token = md5(username + str(time.time()))
            user['token'] = token
            user_collection.update({'username': username, 'password': password}, user)
            result['code'] = 20000
            result['msg'] = '登录成功'
            response = JsonResponse(result, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})
            response.set_cookie("username", username, expires=60 * 60 * 2)
            response.set_cookie("token", token, expires=60 * 60 * 2)
            return response
    return render(request, 'login.html')  # 跳转到登录页面


# 渲染后台数据管理页面
@cookie_auth
def back_data(request):
    context = {}
    context["username"] = request.COOKIES.get("username")
    return render(request, 'back/data/admin_data.html', context)


# 渲染后台数据类别管理页面
@cookie_auth
def back_venue(request, class_name):
    context = {}
    context["username"] = request.COOKIES.get("username")
    if class_name == "类别名称":
        return render(request, "back/venue/admin_venue_label.html")
    elif class_name == "包含场馆":
        return render(request, "back/venue/admin_venue_venue.html")


# 渲染后台用户管理页面
@cookie_auth
def back_user(request):
    context = {}
    context["username"] = request.COOKIES.get("username")
    return render(request, 'back/user/admin_user.html', context)


#
# def back_search(request):
#     context = {}
#     context["username"] = request.COOKIES.get("username")
#     return render(request, 'back/search/admin_search.html')

#  前台首页
def front_index(request):
    return render(request, 'front/index.html')


# 前台搜索页
def front_search(request):
    return render(request, 'front/search.html')


#  前台数据详情页
def getFrontDetailHtml(request, labelName, venueName, itemName):
    context = {}
    context['label'] = labelName
    context['venue'] = venueName
    context['item'] = itemName
    return render(request, 'front/detail.html', context)