from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from ..finderror import *
from app.auth.adminauth import *
from app.model.contanct_us import contactus

class userquery(TemplateView):
    @check_admin_login
    def get(self, request):
        return render(request, 'adminfolder/userquery.html')


class getuserquery(TemplateView):
    @check_admin_login
    def get(self, request):
        data=[]
        count=1
        try:
            for info in contactus.objects.all():
                data.append([
                    count, 
                    info.name,
                    info.email,
                    info.mobile,
                    info.msg,
                    info.create_At
                ])
                count+=1

            data={"data":data}
            return JsonResponse(data,safe=False)
        except Exception:
            Find_error()
            data=[]
            data={"data":data}
            return JsonResponse(data,safe=False)