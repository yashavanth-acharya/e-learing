from app.model.topic import Topics
from app.model.course import Courses
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from ..finderror import *
from app.auth.adminauth import *


class Viewtopic(TemplateView):
    @check_admin_login
    def get(self,request):
        data={"data":Courses.objects.all()}
        
        return render(request,"adminfolder/viewtopic.html",data)

class gettopic(TemplateView):
    @check_admin_login
    def get(self,request):
        info=[]
        counts=0
        try:
            # data.courseid,
            for data in Topics.objects.all():
                info.append([
                    counts+1,
                    data.topicname,
                    data.topic_Descriptions,
                    "<a href="+str(data.icon)+" >"+str(data.topicname)+"</a>",
                    data.duration,
                    data.marks_for_pre_question,
                    data.minimum_mark,
                    data.create_At,
                    data.updated_At,
                    "<buttons class='btn btn-primary'data-bs-toggle='modal' data-bs-target='#modal2'  title='Edit' onclick='editcourse(\""+str(data.topicid)+"\")' >Edit</buttons>"
                    "<buttons class='btn btn-danger' title='Delete' onclick='deletetopic(\""+str(data.topicid)+"\")' >Delete<buttons>",

                ])
                if data.status:
                   info[counts].insert(9,'<span class="badge bg-primary" onclick="Activtetopic(\''+str(data.topicid)+'\')" style="cursor:pointer">Enabled</span>')
                else:
                    info[counts].insert(9,'<span class="badge bg-danger" onclick="Activtetopic(\''+str(data.topicid)+'\')"  style="cursor:pointer">Disabled</span>')
                counts+=1
            
        except Exception as e:
            print(e)
            info=[]
        info={"data":info}
        return JsonResponse(info,safe=False)
        # if 'admin' in request.session:
        #     return render("/addcourse.html")
        # else:
        #     return redirect("/")


class DeleteTopic(TemplateView):
    @check_admin_login
    def get(self,request):
        topicid=request.GET['topicid']
        try:
            data=Topics.objects.get(topicid=topicid)
            if data:
                data.delete()
                msg={"msg":"Topic Deleted successfully","error":0}
                return JsonResponse(msg,safe=False)

            else:
                msg={"msg":"Invalid course","error":1}
                return JsonResponse(msg,safe=False)
                
        except Exception as e:
            Find_error()
            msg={"msg":"Server error","error":1}
            return JsonResponse(msg,safe=False)


