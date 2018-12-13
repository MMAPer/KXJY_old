from bson import json_util
from django.http import JsonResponse
from django.shortcuts import render
from kxjy.settings import db

# Create your views here.


def getUsers(request):
    res = {}
    user_collection = db.user
    users = list(user_collection.find())
    res["data"] = users
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})
