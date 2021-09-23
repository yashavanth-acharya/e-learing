from functools import wraps
from django.shortcuts import redirect
from app.model.user import Userdetails

def check_user_login(func):
    @wraps(func)
    def inner(self,request, *args, **kwargs):
        if  request.session.get("user"):
            if  request.session.get("user")['role']=="user":
                return func(self,request, *args, **kwargs)
            else:
                next_url = request.path_info
                request.session.clear()
                request.session['redirecturl']=next_url
                return redirect("/")
        else:
            next_url = request.path_info
            request.session.clear()
            request.session['redirecturl']=next_url
            return redirect("/")
            # return func(self,request, *args, **kwargs)

    return inner