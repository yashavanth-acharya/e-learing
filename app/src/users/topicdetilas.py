from  app.model.topic import Topics
from django.views.generic import TemplateView
from django.shortcuts import render


class Topicinfo(TemplateView):
    def get(self,request,id):
        try:
            data=[]
            for info in Topics.objects.filter(topicid=id):
                
                data.append([
                info.topicid,
                info.topicname,
                info.icon,
                info.topic_Descriptions,
                info.marks_for_pre_question,
                info.minimum_mark,
                info.duration,
                info.course.coursename
            ])  
        except Exception as e:
            print(e)
            data=[]
        topicdata={"data":data}
        return render(request, 'user/topicinfo.html',topicdata)