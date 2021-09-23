from app.model.course import Courses
from app.model.user import Userdetails
from app.model.topic import Topics

from django.views.generic import TemplateView
from django.shortcuts import render
from app.auth.adminauth import *

class Dashboard(TemplateView):
    
    @check_admin_login
    def get(self,request):
        # if 'admin' in request.session:
        try:
            course=Courses.objects.all().count()
            user=Userdetails.objects.filter(user_role="user").count()
            topic=Topics.objects.all().count()

            counts={"course":course,"user":user,"topic":topic}
        except Exception as e:
            print(e)
            counts={"course":"0","user":"0","topic":"0"}
    
        return render(request,"adminfolder/dashboard.html",counts)
        # else:
        #     return redirect("/")
            