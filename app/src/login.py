from app.model.user import Userdetails
from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from app.auth.hashpassword import verify_password
from .finderror import *
class Login(TemplateView):
    def get(self,request):
        msg={"msg":"","error":False}
        return render(request,"login.html",msg)

    def post(self,request):
        try:
            username=request.POST['username']
            password=request.POST['password']
            username=Userdetails.objects.filter(username=username.lower())
            if username:
                if verify_password(password,username[0].password):
                    if "redirecturl" in request.session:
                        path=request.session['redirecturl']
                    if username[0].user_role =="user":
                        
                        request.session['user']={"user":str(username[0].userid),"role":username[0].user_role}
                        if "redirecturl" in request.session:
                            del request.session["redirecturl"]
                            return redirect(path)
                        return redirect("/")
                    else:
                        request.session['admin']={"user":str(username[0].userid),"role":username[0].user_role}
                        return redirect("/dashboard")
            msg={"msg":"Invalid username or password","error":True}   
            return render(request,"login.html",msg)
        except Exception:
            Find_error()
            msg={"msg":"Server error","error":True}   
            return render(request,"login.html",msg)

class Logout(View):
    def get(self,request):
        request.session.clear()
        return redirect("/")

