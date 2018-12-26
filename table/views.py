from bson import json_util
from django.http import JsonResponse

from common.status import StatusCode
from kxjy.settings import db


# Create your views here.


def getTableByLabelName(request, labelName):
    res = StatusCode.OK()
    table_collection = db.table
    table = table_collection.find_one({"label":labelName})
    res['data'] = table
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


def addTable(request):
    res = StatusCode.OK()
    table = request.POST.get("table")
    table_collection = db.table
    table_collection.insert(table)
    res['data'] = table
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})