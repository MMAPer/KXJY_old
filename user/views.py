from bson import json_util
from django.http import JsonResponse
from django.shortcuts import render
from kxjy.settings import db

# Create your views here.
from kxjy.status import StatusCode


def getUsers(request):
    res = StatusCode.OK()
    user_collection = db.user
    users = list(user_collection.find())
    res["data"] = users
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


def addUser(request):
    res = StatusCode.OK()
    user = request.POST.get("user")
    user_collection = db.user
    user_collection.insert(user)