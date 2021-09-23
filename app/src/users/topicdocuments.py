import bcrypt
from app.model.topic import Topics
from django.views.generic import TemplateView
from django.shortcuts import render
from app.model.topicdocument import Topicsdocuments
from app.auth.userauth import check_user_login

class Topicdocumentview(TemplateView):
    @check_user_login
    def get(self,request,id):
        try:
            data=Topicsdocuments.objects.get(topic_id=id)   
        except Exception as e:
            print(e)
            data=[]
        infodata={"data":data.document}
        return render(request,"user/topicdocument.html",infodata)