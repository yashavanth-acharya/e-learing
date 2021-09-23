from app.model.topic import Topics
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from ..finderror import *
from app.auth.adminauth import *
from app.model.topicdocument import Topicsdocuments


class Viewdocument(TemplateView):
    @check_admin_login
    def get(self,request):
        data={"data":Topics.objects.all()}
        return render(request,"adminfolder/viewdocument.html",data)


    @check_admin_login
    def post(self,request):
        topicid=request.POST['topicname']
        documents=request.POST['documents']

        if len(documents)==0 and len(topicid)==0:
            msg={"msg":"All fileds are required *","error":1}
            return JsonResponse(msg,safe=False)

        try:
            if Topicsdocuments.objects.filter(topic_id=topicid):
                msg={"msg":"Documents already exists","error":1}
                return JsonResponse(msg,safe=False)

            Topicsdocuments(document=documents,topic_id=topicid).save()
            msg={"msg":"Documents added successfully","error":0}
            return JsonResponse(msg,safe=False)
        except Exception as e:
            print(e)
            msg={"msg":"Server error","error":1}
            return JsonResponse(msg,safe=False)


class Getdocuments(TemplateView):
    @check_admin_login
    def get(self,request):
        info=[]
        counts=0
        try:
            for data in Topicsdocuments.objects.all():
                topicname=Topics.objects.get(topicid=data.topic.topicid).topicname
                info.append([
                    counts+1,
                    topicname,
                    "<a href="+str(data.document)+" >"+str(topicname)+"</a>",
                    data.create_At,
                    data.updated_At,
                    "<buttons class='btn btn-primary'data-bs-toggle='modal' data-bs-target='#modal2'  title='Edit' onclick='editdocuments(\""+str(data.documentid)+"\")' >Edit</buttons>"
                    "<buttons class='btn btn-danger' title='Delete' onclick='deletetopicdocument(\""+str(data.documentid)+"\")' >Delete<buttons>",
                ])
                counts+=1
            
        except Exception as e:
            print(e)
            info=[]
        info={"data":info}
        return JsonResponse(info,safe=False)