from app.model.course import Courses
from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from ..finderror import *
from app.auth.adminauth import *


class Viewcourse(TemplateView):
    @check_admin_login
    def get(self,request):
        return render(request,"adminfolder/viewcourse.html")

class getcourse(TemplateView):
    @check_admin_login
    def get(self,request):
        info=[]
        counts=0
        try:
            # data.courseid,
            for data in Courses.objects.all():
                info.append([
                    counts+1,
                    data.coursename,
                    data.course_Descriptions,
                    "<a href="+str(data.icon)+" >"+str(data.coursename)+"</a>",
                    data.create_At,
                    data.updated_At,
                    "<buttons class='btn btn-primary' data-bs-toggle='modal' data-bs-target='#modal2'  title='Edit' onclick='editcourse(\""+str(data.courseid)+"\")' >Edit </buttons>"
                    "<buttons class='btn btn-danger' title='Delete' onclick='deletecourse(\""+str(data.courseid)+"\")' >Delete<buttons>",

                ])
                if data.status:
                   info[counts].insert(6,'<span class="badge bg-primary" onclick="Activtecourse(\''+str(data.courseid)+'\')" style="cursor:pointer">Enabled</span>')
                else:
                    info[counts].insert(6,'<span class="badge bg-danger" onclick="Activtecourse(\''+str(data.courseid)+'\')"  style="cursor:pointer">Disabled</span>')
                counts+=1
            
        except Exception as e:
            print(e)
            info=[]
        info={"data":info}
        return JsonResponse(info,safe=False)
      


class DeleteCourse(TemplateView):
    @check_admin_login
    def get(self,request):
        courseid=request.GET['couserid']
        try:
            data=Courses.objects.get(courseid=courseid)
            if data:
                data.delete()
                msg={"msg":"Course Deleted successfully","error":0}
                return JsonResponse(msg,safe=False)

            else:
                msg={"msg":"Invalid course","error":1}
                return JsonResponse(msg,safe=False)
                
        except Exception as e:
            Find_error()
            msg={"msg":"Server error","error":1}
            return JsonResponse(msg,safe=False)


