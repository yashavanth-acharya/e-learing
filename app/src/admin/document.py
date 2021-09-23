from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from ..finderror import *
from app.auth.adminauth import *
from app.model.topicdocument import Topicsdocuments


class Editdocuments(TemplateView):
    @check_admin_login
    def get(self,request):
        documentid=request.GET['id']
        try:
            data=Topicsdocuments.objects.filter(documentid=documentid)
            editdata=[]
            for info in data:
                editdata.append([
                    info.topic.topicid,
                    info.document
                ])

            data={"data":editdata,"error":0}
            return JsonResponse(data,safe=False)
        except Exception as e:
            print(e)
            msg={"data":"Server error","error":1}
            return JsonResponse(msg,safe=False)
    @check_admin_login
    def post(self,request):
        documentid=request.POST['id']
        topicname=request.POST['topicname']
        documents=request.POST['documents']

        if len(documents)==0 and len(topicname)==0 and len(documentid)==0:
            msg={"msg":"All fileds are required *","error":1}
            return JsonResponse(msg,safe=False)

        try:
            Topicsdocuments.objects.filter(documentid=documentid).update(document=documents,topic_id=topicname)
            msg={"msg":"Document Updated successfully","error":0}
            return JsonResponse(msg,safe=False)
        except Exception as e:
            print(e)
            msg={"msg":"Server error","error":1}
            return JsonResponse(msg,safe=False)



class Deletedocument(TemplateView):
    def post(self,request):
        documentid=request.POST['id']

        try:
            Topicsdocuments.objects.filter(documentid=documentid).delete()
            msg={"msg":"Document deleted successfully","error":0}
            return JsonResponse(msg,safe=False)
        except Exception as e:
            print(e)
            msg={"msg":"Server error","error":1}
            return JsonResponse(msg,safe=False)