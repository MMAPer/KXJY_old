import json

from bson import json_util
from django.http import JsonResponse

# Create your views here.
from common.status import StatusCode
from kxjy.settings import db
from common.auth import cookie_auth, permission_auth


@cookie_auth
def getUsers(request):
    res = StatusCode.OK()
    user_collection = db.user
    users = list(user_collection.find())
    res["data"] = users
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


@cookie_auth
@permission_auth
def addUser(request):
    res = StatusCode.OK()
    user = request.POST.get("user")
    user = json.loads(user)
    user_collection = db.user
    user_collection.insert(user)
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


@cookie_auth
@permission_auth
def deleteUser(request, username):
    res = StatusCode.OK()
    user_collection = db.user
    user_collection.delete_one({"username": username})
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})


@cookie_auth
@permission_auth
def updateUser(request, username):
    res = StatusCode.OK()
    user = request.POST.get("user")
    user = json.loads(user)
    user_collection = db.user
    user_collection.update_one({"username": username}, user)
    return JsonResponse(res, json_dumps_params={'default': json_util.default, 'ensure_ascii': False})