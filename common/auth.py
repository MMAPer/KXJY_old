from django.shortcuts import redirect

salt = 'kxjy'
def cookie_auth(func):
    def weaper(request, *args, **kwargs):
        cookies = request.COOKIES.get('token')
        print("auth_cookies=", cookies)
        if cookies:
            from kxjy.settings import db
            user_collection = db.user
            user = user_collection.find_one({'token': cookies})
            if user:
                return func(request)
            else:
                return redirect('/login')
        else:
            return redirect('/login')
    return weaper


def permission_auth(func):
    def weaper(request, *args, **kwargs):
        username = request.COOKIES.get('username')
        print("username=", username)
        if username:
            from kxjy.settings import db
            user_collection = db.user
            user = user_collection.find_one({'username': username})
            if user.get("role")!="普通用户":
                return func(request)
            else:
                return redirect('/login')
        else:
            return redirect('/login')
    return weaper