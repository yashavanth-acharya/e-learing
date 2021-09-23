from app.model.topic import Topics
from app.model.course import Courses
from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from ..finderror import *
from app.auth.adminauth import *


class Addtopic(TemplateView):
    @check_admin_login
    def post(self,request):
        try:
            topic_title=request.POST['name']
            course=request.POST['course']
            topic_description=request.POST['descriptions']
            icondata=request.POST['icons']
            duration=request.POST['duration']
            marks_for_pre_question=request.POST['marks_for_pre_question']
            minimum_mark= request.POST['minimum_mark']
        except Exception as e:
            print(e)
            msg={"msg":"Enter valid information","error":1}
            return JsonResponse(msg,safe=False)

        if len(topic_title)==0 or len(topic_description)==0 or len(icondata)==0 or len(duration)==0 or len(marks_for_pre_question)==0 or len(minimum_mark)==0 or len(course)==0:
            msg={"msg":"All fileds are required *","error":1}
            return JsonResponse(msg,safe=False)

        if len(Courses.objects.filter(courseid=course))==0:
            msg={"msg":"Invalid  course","error":1}
            return JsonResponse(msg,safe=False)

        if Topics.objects.filter(topicname=topic_title):
            msg={"msg":"Topic name already exists","error":1}
            return JsonResponse(msg,safe=False)

        if isinstance(int(duration), int)==False:
            msg={"msg":"Enter valid time","error":1}
            return JsonResponse(msg,safe=False)
        
        try:
            float(minimum_mark)
        except ValueError:
            msg={"msg":"Enter valid minimum mark","error":1}
            return JsonResponse(msg,safe=False) 

        try:
            float(marks_for_pre_question)
        except ValueError:
            msg={"msg":"Enter valid marks","error":1}
            return JsonResponse(msg,safe=False)  

        try:
            Topics(topicname=topic_title,topic_Descriptions=topic_description,icon=icondata,course_id=course,
            duration=duration,marks_for_pre_question=marks_for_pre_question,minimum_mark=minimum_mark).save()
            msg={"msg":"Topic added successfully","error":0}
            return JsonResponse(msg,safe=False)
        except Exception as e:
            print(e)
            msg={"msg":"Server error","error":1}
            return JsonResponse(msg,safe=False)



class Edittopic(TemplateView):
    @check_admin_login
    def get(self,request):
      
        topicid=request.GET['topicid']
        data=Topics.objects.get(topicid=topicid)
        if data:
            request.session['topicid']=str(data.topicid)
    
            data={
            "icon":data.icon,
            "topicname":data.topicname,
            "topic_description":data.topic_Descriptions,
            "duration":data.duration,
            "marks_for_pre_question":data.marks_for_pre_question,
            "coursename":data.course_id,
            "minimum_mark":data.minimum_mark}
            msg={"data":data,"error":0}
            return JsonResponse(msg,safe=False)

        else:
            msg={"data":"Invalid course","error":1}
            return JsonResponse(msg,safe=False)
        
    @check_admin_login
    def post(self,request):
        try:
            topicinfo=Topics.objects.filter(topicid=request.session['topicid'])
            if topicinfo:
                topic_title=request.POST['name']
                course=request.POST['course']
                topic_description=request.POST['descriptions']
                icondata=request.POST['icons']
                duration=request.POST['duration']
                marks_for_pre_question=request.POST['marks_for_pre_question']
                minimum_mark= request.POST['minimum_mark']

                if len(topic_title)==0 or len(topic_description)==0 or len(icondata)==0 or len(duration)==0 or len(marks_for_pre_question)==0 or len(minimum_mark)==0 or len(course)==0:
                    msg={"msg":"All fileds are required *","error":1}
                    return JsonResponse(msg,safe=False)

                if len(Courses.objects.filter(courseid=course))==0:
                    msg={"msg":"Invalid  course","error":1}
                    return JsonResponse(msg,safe=False)

                # if Topics.objects.filter(topicname=topic_title):
                #     msg={"msg":"Topic name already exists","error":1}
                #     return JsonResponse(msg,safe=False)

                if isinstance(int(duration), int)==False:
                    msg={"msg":"Enter valid time","error":1}
                    return JsonResponse(msg,safe=False)
                
                try:
                    float(minimum_mark)
                except ValueError:
                    msg={"msg":"Enter valid minimum mark","error":1}
                    return JsonResponse(msg,safe=False) 

                try:
                    float(marks_for_pre_question)
                except ValueError:
                    msg={"msg":"Enter valid marks","error":1}
                    return JsonResponse(msg,safe=False)  

               

                topicinfo.update(topicname=topic_title,topic_Descriptions=topic_description,icon=icondata,course_id=course,
            duration=duration,marks_for_pre_question=marks_for_pre_question,minimum_mark=minimum_mark)
                msg={"msg":"Topic updated successfully","error":0}
                return JsonResponse(msg,safe=False)
            else:
                msg={"msg":"Invalid Topic","error":1}
                return JsonResponse(msg,safe=False)
        
            
        except Exception as e:
            Find_error()
            msg={"msg":"Server error","error":1}
            return JsonResponse(msg,safe=False)

        

