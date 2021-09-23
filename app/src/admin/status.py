from app.model.topic import Topics
from app.model.course import Courses
from django.views.generic import TemplateView
from django.http import JsonResponse
from ..finderror import *
from app.auth.adminauth import *



class CoursesStatus(TemplateView):
    @check_admin_login
    def get(self,request):
        try:
            data=Courses.objects.filter(courseid=request.GET['course_id'])
        except Exception:
            Find_error()
            msg={"msg":"Server error","error":1}
            return JsonResponse(msg,safe=False)
       
        if data:
            if data[0].status:
                status=False
            else:
                status=True
            data.update(status=status)
            msg={"msg":"activated","error":0}
            return JsonResponse(msg,safe=False)
        else:
            msg={"msg":"Invalid course","error":1}
            return JsonResponse(msg,safe=False)


class TopicStatus(TemplateView):
    @check_admin_login
    def get(self,request):
        try:
            data=Topics.objects.filter(topicid=request.GET['topicid'])
        except Exception:
            Find_error()
            msg={"msg":"Server error","error":1}
            return JsonResponse(msg,safe=False)
       
        if data:
            if data[0].status:
                status=False
            else:
                status=True
            data.update(status=status)
            msg={"msg":"activated","error":0}
            return JsonResponse(msg,safe=False)
        else:
            msg={"msg":"Invalid course","error":1}
            return JsonResponse(msg,safe=False)