from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from app.model.questions import Questions
from app.model.topic import Topics
from django.http import JsonResponse
from ..finderror import *
from app.auth.adminauth import *


class ViewAddedtopic(TemplateView):
    @check_admin_login
    def get(self,request):
        data=Topics.objects.all()
        if data:
            msg={"msg":"","data":data}
            return render(request,"adminfolder/viewquestions.html",msg)
        else:
            msg={"msg":"Add topic","data":""}
            return render(request,"adminfolder/viewquestions.html",msg)

    @check_admin_login
    def post(self,request):
        topicid = request.POST['topicid']
        try:
            data=Topics.objects.get(topicid=topicid)
        except Exception:
            Find_error()
            msg={"path":"Server error","error":1}
            return JsonResponse(msg,safe=False)

        if data:
            request.session['addquestionstopicid']=topicid
            msg={"path":"questions","error":0}
            return JsonResponse(msg,safe=False)
        else:
            msg={"path":"Invalid topicid","error":1}
            return JsonResponse(msg,safe=False)



class ViewNexth(TemplateView):
    @check_admin_login
    def get(self,request):
        if request.session["addquestionstopicid"]:
             return render(request,"adminfolder/addquestions.html")
        else:
            return redirect("viewquestion")


class Deletequestion(TemplateView):
    @check_admin_login
    def get(self,request):
        questionid=request.GET['questionid']
        try:
            data=Questions.objects.get(questionid=questionid)
            if data:
                data.delete()
                msg={"msg":"Question Deleted successfully","error":0}
                return JsonResponse(msg,safe=False)

            else:
                msg={"msg":"Invalid Question","error":1}
                return JsonResponse(msg,safe=False)
                
        except Exception as e:
            Find_error()
            msg={"msg":"Server error","error":1}
            return JsonResponse(msg,safe=False)
    
