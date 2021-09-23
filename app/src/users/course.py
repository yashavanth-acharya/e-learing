from app.model.course import Courses
from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from app.src.finderror import Find_error

class Course(TemplateView):
    def get(self,request):  
        if "endtime" in request.session:
                del request.session['endtime']
        data=[]
        try:
            for info in Courses.objects.filter(status=True):
                data.append([
                    info.courseid,
                    info.coursename,
                    info.icon,
                    info.course_Descriptions
                ])  
        except Exception as e:
            Find_error()
            data=[]


        coursedata={"data":data}    
        return render(request,"user/Courses.html",coursedata)
            