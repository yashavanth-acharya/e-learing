from app.model.user import Userdetails
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
import hashlib
from ..finderror import *
from app.auth.adminauth import *

class User(TemplateView):
    @check_admin_login
    def get(self,request):
        return render(request,"adminfolder/students.html")
        
        
class Getuser(TemplateView):
    @check_admin_login
    def get(self,request):
        try:
            info=[]
            count=0
            for data in Userdetails.objects.filter(user_role="user"):
                info.append([
                    count,
                    data.username,
                    data.name,
                    data.email,
                    data.mobile,
                    data.address,
                    data.pincode,
                    data.create_At,
                    data.updated_At,
                ])
                count+=1
        except Exception as e:
            print(e)
            info=[]
        info={"data":info}
        return JsonResponse(info,safe=False)
            
    # def post(self,request):
    #     if 'admin' in request.session:
    #         try:
    #             userid=request.POST['userid']
    #             Userdetails.objects(userid=userid).delete()
    #             msg="User deleted successfully"
    #         except Exception as e:
    #             print(e)
    #             msg=""

    #         return render("/Userdetails.html",msg=msg)
    #     else:
    #         return redirect("/")

class adminchangepassword(TemplateView):
    @check_admin_login
    def get(self, request):
        error = {"error":"","msg":""}
        return render(request,"adminfolder/changepassword.html",error)
    @check_admin_login
    def post(self,request):
        oldpassword= request.POST['oldpassword']
        newpassword= request.POST['newpassword']
        data=Userdetails.objects.filter(username=request.session['user'],password=oldpassword)
        if data:
            result = hashlib.md5(newpassword.encode())
            data.update(password=result.hexdigest())
            error = {"error":0,"msg":"Password changed successfully"}
            return render(request,"adminfolder/changepassword.html",error)

        else:
            error = {"error":1,"msg":"Invalid old oldpassword"}
            return render(request,"adminfolder/changepassword.html",error)

