from django.views.generic import TemplateView
from django.shortcuts import render
from app.model.topic import Topics
from django.http import JsonResponse
from ..finderror import *
from app.auth.adminauth import *
from app.model.user import Userdetails
from app.model.Feedback import Feedback

class Userfeedback(TemplateView):
    @check_admin_login
    def get(self, request):
        return render(request, 'adminfolder/feedback.html')


class getFeedback(TemplateView):
    @check_admin_login
    def get(self, request):
        data=[]
        count=1
        try:
            for info in Feedback.objects.all():
                user=Userdetails.objects.get(userid=info.user).name
                topic=Topics.objects.get(topicid=info.topic_id).topicname
                data.append([
                    count, 
                    user,
                    topic,
                    info.Feedback,
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