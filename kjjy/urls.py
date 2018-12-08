"""kjjy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import json
import time

from bson import json_util
from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import include, path
from common.utils import md5
from common.auth import salt, cookie_auth
from .settings import db

#  要引入下面的，才能写视图函数
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()


def login(request):
    # 未登录用户执行以下登录操作
    if request.method == 'POST':
        result = {}
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_collection = db.user
        user = user_collection.find_one({'username': username, 'password': password})
        if user:
            token = md5(username+str(time.time()))
            user['token'] = token
            user_collection.update({'username': username, 'password': password}, user)
            result['code'] = 20000
            result['msg'] = '登录成功'
            response = JsonResponse(result, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})
            response.set_cookie("username", username, expires=60*60*2)
            response.set_cookie("token", token, expires=60*60*2)
            return response
    return render(request, 'login.html')  # 跳转到登录页面

from common.auth import cookie_auth
@cookie_auth
def back(request):
    context = {}
    context["username"] = request.COOKIES.get("username")
    return render(request, 'back/admin.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('back/', back, name='back'),
    path('venue/', include('venue.urls'))
]

"""
1.url映射：
（1）为什么会去urls.py文件中寻找映射呢？是因为在'settings.py'文件中配置了'ROOT_URLCONF'为'urls.py'，
所以django会去'urls.py'中寻找映射
（2）在'urls.py'中我们所有的映射，都应该放在'urlpatterns'这个变量中
（3）所有的映射不是随便写的，而是使用'path'函数或者是're_path'函数进行包装的

2.url传参数：
（1）采用在url中使用变量的方式，在path的第一个参数中，使用'<参数名>'的方式可以传递参数，
然后在视图函数中也要写一个参数，视图函数中的参数必须和url中的参数名称保持一致，不然找不到
这个参数。另外，url中可以传递多个参数
（2）采用查询字符串的方式：在url中，不需要单独的匹配查询字符串的部分，只需要在视图函数中
使用'request.GET.get('参数名称')'的方式获取
"""