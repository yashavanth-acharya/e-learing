from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from ..finderror import *
from app.auth.adminauth import *
from app.model.topic import Topics
from app.model.result import Result
from app.model.user import Userdetails

class ViewResult(TemplateView):
    @check_admin_login
    def get(self,request):
        return render(request,"adminfolder/result.html")


class GetstudentResults(TemplateView):
    @check_admin_login
    def get(self,request):
        data=[]
        count=1
        try:
            for info in Result.objects.all():
                topicinfo=Topics.objects.get(topicname=info.topic)
                if float(info.totalmark)>float(topicinfo.minimum_mark):
                    status="<p style='color:green'>Pass</p>"
                else:
                    status="<p style='color:red'>Fail</p>"
                
                data.append([
                    count,
                    Userdetails.objects.get(userid=info.user.userid).username,
                    info.topic,
                    info.totalmark,
                    info.outof,
                    status,
                    info.create_At
                ])
                count+=1
        except Exception:
            data=[]
            Find_error()

        data={"data":data}
        return JsonResponse(data,safe=False)

