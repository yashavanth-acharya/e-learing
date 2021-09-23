from app.model.course import Courses
from django.views.generic import TemplateView
from django.http import JsonResponse
from ..finderror import *
from app.auth.adminauth import *
\

class Addcourse(TemplateView):
    @check_admin_login
    def post(self,request):
        try:
            course_title=request.POST['name']
            course_description=request.POST['descriptions']
            icondata=request.POST['icons']
        except Exception as e:
            print(e)
            msg={"msg":"Enter valid information","error":1}

        if len(course_title)==0 or len(course_description)==0 or len(icondata)==0:
            msg={"msg":"All fileds are required *","error":1}
            return JsonResponse(msg,safe=False)

        if Courses.objects.filter(coursename=course_title):
            msg={"msg":"Course name already exists","error":1}
            return JsonResponse(msg,safe=False)
        try:
            Courses(coursename=course_title,course_Descriptions=course_description,icon=icondata).save()
            msg={"msg":"Course added successfully","error":0}
        except Exception as e:
            print(e)
            msg={"msg":"Server error","error":1}
        return JsonResponse(msg,safe=False)

    


class Editcourses(TemplateView):
    @check_admin_login
    def get(self,request):
      
        courseid=request.GET['couserid']
        data=Courses.objects.get(courseid=courseid)
        if data:
            request.session['couserid']=str(data.courseid)
            data={"icon":data.icon,"coursename":data.coursename,"course_description":data.course_Descriptions}
            msg={"data":data,"error":0}
            return JsonResponse(msg,safe=False)

        else:
            msg={"data":"Invalid course","error":1}
            return JsonResponse(msg,safe=False)
        
    @check_admin_login
    def post(self,request):
        try:
            courseinfo=Courses.objects.filter(courseid=request.session['couserid'])
            if courseinfo:
                course_title=request.POST['name']
                course_description=request.POST['descriptions']
                icondata=request.POST['icons']
                
                if len(course_title)==0 or len(course_description)==0 or len(icondata)==0:
                    msg={"msg":"All fileds are required *","error":1}
                    return JsonResponse(msg,safe=False)

                courseinfo.update(coursename=course_title,course_Descriptions=course_description,icon=icondata)
                msg={"msg":"Course updated successfully","error":0}
                return JsonResponse(msg,safe=False)
            else:
                msg={"msg":"Invalid course","error":1}
                return JsonResponse(msg,safe=False)
        
            
        except Exception as e:
            Find_error()
            msg={"msg":"Server error","error":1}
            return JsonResponse(msg,safe=False)

        

