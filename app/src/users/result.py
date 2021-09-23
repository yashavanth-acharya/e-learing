from django.views.generic import TemplateView
from django.shortcuts import render
from app.model.result import Result
from app.model.topic import Topics
from django.http import JsonResponse
from ..finderror import *
from app.auth.userauth import check_user_login
class Results(TemplateView):
    @check_user_login
    def get(self,request):
        return render(request,"user/Results.html")
       

class GetResults(TemplateView):
    @check_user_login
    def get(self, request):
        verifedimg='<i class="fa fa-check-circle" style="font-size:20px;color:green"></i>'
        try:
            count=1
            data=[]
            for info in Result.objects.filter(user_id=request.session['user']['user']):
                topicinfo=Topics.objects.get(topicname=info.topic)
                if float(info.totalmark)>float(topicinfo.minimum_mark):
                    status="<p style='color:green'>Pass</p>"
                else:
                    status="<p style='color:red'>Fail</p>"

                if info.feedback_status:
                    fstatus = verifedimg
                else:
                     fstatus = "<buttons class='btn btn-info' data-bs-toggle='modal' data-bs-target='#staticBackdrop' onclick='feedback(\""+str(info.Resultid)+"\")'>Feedback</button>"
                data.append([
                    count,
                    info.topic,
                    info.totalmark,
                    info.outof,
                    info.submitted_time,
                    status,
                    fstatus
                ])
                count += 1
        except Exception as e:
            Find_error()
            data=[]

        return JsonResponse({"data":data})