from django.shortcuts import redirect

salt = 'kjjy'
def cookie_auth(func):
    def weaper(request, *args, **kwargs):
        cookies = request.COOKIES.get('token')
        print("auth_cookies=", cookies)
        if cookies:
            from kjjy.settings import db
            user_collection = db.user
            user = user_collection.find_one({'token': cookies})
            if user:
                return func(request)
            else:
                return redirect('/login')
        else:
            return redirect('/login')
    return weaper