from  app.model.questions import Questions
from app.model.topic import Topics
from django.views.generic import TemplateView
from django.shortcuts import render
import json
import random
import datetime
from datetime import date
from pytz import timezone 
from django.shortcuts import redirect
from app.model.result import Result
from ..finderror import *
from app.auth.userauth import check_user_login
today = date.today()


class Mcq(TemplateView):
    @check_user_login
    def get(self,request,id):
        if "course start" not in request.session:
            if "endtime" in request.session:
                del request.session['endtime']
            return redirect("/")
        data=[]
        try:
            topicinfo=Topics.objects.filter(topicid=id)[0]
            request.session['topicinfo']={
            "marks":topicinfo.marks_for_pre_question,
            "minimum":topicinfo.minimum_mark,
            "topicname":topicinfo.topicname}
          
            now = datetime.datetime.now(timezone("Asia/Kolkata"))
            currenttime = datetime.datetime(int(now.year),int(now.month),int(now.day),int(now.hour),int(now.minute),int(now.second))

            endtime=str(currenttime+datetime.timedelta(minutes=topicinfo.duration)).split(" ")[1]
                       
            d4 = today.strftime("%b %d,%Y \t")
            if "endtime" not in request.session:
                request.session['endtime']=str(d4)+endtime

            for info in Questions.objects.filter(topic=id):
                qoptions=json.loads(info.options.replace("'", "\""))
                data.append([
                    info.questions,
                    qoptions['option1'],
                    qoptions['option2'],
                    qoptions['option3'],
                    qoptions['option4'],
                    info.questionid
                ])
                
        except Exception as e:
            Find_error()
            data=[]
        request.session['questioncount']=len(data)
        data={"data":random.sample(data,len(data)),"endtime":str(request.session['endtime'])}
        return render(request,"user/mcq.html",data)
       

    @check_user_login
    def post(self,request,id):
       
        try:
            # data=Questions.objects.filter(topicid=id)
            questions=request.POST.getlist('question[]')
            options=[]
            marks=0
            for i in range(1,request.session['questioncount']+1):
                for optionslist in request.POST.getlist('option'+str(i)+'[]'):
                    options.append(optionslist)
            for questionid in questions:
                question=Questions.objects.filter(questionid=questionid)[0]
                qoptions=json.loads(question.options.replace("'", "\""))
                op=[qoptions['option1'],qoptions['option2'],qoptions['option3'],qoptions['option4']]
                for answers in options:
                    if answers in op:
                        if question.correct_answer==answers:
                            marks+=request.session['topicinfo']['marks']
                    

            del request.session['endtime']
            del request.session['course start']
            Result(user_id=request.session['user']['user'],
            topic=request.session['topicinfo']['topicname'],
            totalmark=marks,
            outof=request.session['questioncount']*request.session['topicinfo']['marks'],
            submitted_time=datetime.datetime.now()).save()
            
            return redirect("/results")
        except Exception as e:
            Find_error()
            data=[] 
            return redirect("/")
        
            