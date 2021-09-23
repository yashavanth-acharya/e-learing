from functools import wraps
from django.shortcuts import redirect
from app.model.user import Userdetails

def check_admin_login(func):
    @wraps(func)
    def inner(self,request, *args, **kwargs):
      
        if request.session.get("admin"):
            if  request.session.get("admin")['role']=="admin":
                return func(self,request, *args, **kwargs)
            else:
                return redirect("/")
        else:
            # next_url = request.path_info
            # request.session['redirecturl']=next_url
            return redirect("/")
            

    return inner