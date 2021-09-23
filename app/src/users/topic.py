from app.model.course import Courses
from app.model.topic import Topics
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse

class Topic(TemplateView):
    def get(self,request,id):
        if "endtime" in request.session:
                del request.session['endtime']
        try:
            data=[]
            for info in Topics.objects.filter(course_id=id,status=True):
                data.append([
                info.topicid,
                info.topicname,
                info.icon,
                info.topic_Descriptions
            ])  
        except Exception as e:
            print(e)
            data=[]
        topicdata={"data":data}
        return render(request,"user/topic.html",topicdata)
       


# class check_course_id(TemplateView):
#     def post(self,request):
#         courseid = request.POST['courseid']
#         request.session['courseid'] =courseid
#         try:
#             if Courses.objects.get(courseid=courseid):
#                 return redirect("/topic")
#         except Exception as e:
#             print(e)


class check_topic_id(TemplateView):
    def post(self,request):
        topicid = request.POST['id']
        try:
            
            if Topics.objects.get(topicid=topicid):
                request.session['course start']=topicid
                return JsonResponse({"data":"/attempt/"+topicid,"error":0})
            else:
                return JsonResponse({"data":"Invalid id","error":1})
        
        except Exception as e:
            print(e)
            return JsonResponse({"data":"Server error","error":1})