from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from app.model.questions import Questions
from app.model.questions import Questions
from django.http import JsonResponse
import json
from ..finderror import *
from app.auth.adminauth import *


class AddQuestions(TemplateView):
    @check_admin_login
    def get(self,request):
        info=[]
        counts=1
        try:
            for data in Questions.objects.all():
                # print(data.options)
                qoptions=json.loads(data.options.replace("'", "\""))
               
                info.append([
                    counts,
                    data.questions,
                    qoptions['option1'],
                    qoptions['option2'],
                    qoptions['option3'],
                    qoptions['option4'],
                    data.correct_answer,
                    data.create_At,
                    data.updated_At,
                    "<buttons class='btn btn-primary'data-bs-toggle='modal' data-bs-target='#modal2'  title='Edit' onclick='editquestion(\""+str(data.questionid)+"\")' >Edit </buttons>"
                    "<buttons class='btn btn-danger' title='Delete' onclick='deletequestion(\""+str(data.questionid)+"\")' > Delete<buttons>",

                ])
                counts+=1
            
        except Exception as e:
            Find_error()
            info=[]
        info={"data":info}
        return JsonResponse(info,safe=False)

    @check_admin_login
    def post(self,request):
        id=request.session["addquestionstopicid"]
        questions=request.POST['Question']
        options1=request.POST['Options1']
        options2=request.POST['Options2']
        options3=request.POST['Options3']
        options4=request.POST['Options4']
        answers=request.POST['Answers']
        if len(questions)==0 or len(answers)==0 or len(options1)==0 or len(options2)==0 or len(options3)==0 or len(options4)==0:

            msg={"data":"Please fill given all fileds","error":1}
            return JsonResponse(msg,safe=False)

         
        if answers not in ['Options1','Options2','Options3','Options4']:
            msg={"data":"Invliad answer selected","error":1}
            return JsonResponse(msg,safe=False)
        try:
            options={"option1":options1.lower(), "option2":options2.lower(), "option3":options3.lower(), "option4":options4.lower()}
            if answers=="Options1":
                answers=options1.lower()
            if answers=="Options2":
                answers=options2.lower()
            if answers=="Options3":
                answers=options3.lower()
            if answers=="Options4":
                answers=options4.lower()
                
            Questions(topic_id=id,questions=questions,correct_answer=answers,options=str(options)).save()
            msg={"data":"Question added successfully","error":0}
            return JsonResponse(msg,safe=False)
        except Exception:
            Find_error()
            msg={"data":"Server error","error":1}
            return JsonResponse(msg,safe=False)

            



class Editquestions(TemplateView):
    @check_admin_login
    def get(self,request):
        id=request.GET['questionid']
        try:
            data=Questions.objects.get(questionid=id)
            if data:
                request.session['questionid']=id
                options=json.loads(data.options.replace("'", "\""))
                data={"question":data.questions,"options":options,"answer":data.correct_answer}
                msg={"data":data,"error":0}
                return JsonResponse(msg,safe=False)
        except Exception:
                Find_error()
                msg={"data":"Server error","error":1}
                return JsonResponse(msg,safe=False)
        
    @check_admin_login
    def post(self,request):
        if Questions.objects.filter(questionid=request.session['questionid']):
            questions=request.POST['Question']
            options1=request.POST['Options1']
            options2=request.POST['Options2']
            options3=request.POST['Options3']
            options4=request.POST['Options4']
            answers=request.POST['Answers']
            if len(questions)==0 or len(answers)==0 or len(options1)==0 or len(options2)==0 or len(options3)==0 or len(options4)==0:
                msg={"data":"Please fill given all fileds","error":1}
                return JsonResponse(msg,safe=False)

            if answers not in ['Options1','Options2','Options3','Options4']:
                msg={"data":"Invliad answer selected","error":1}
                return JsonResponse(msg,safe=False)
            try:
                options={"option1":options1, "option2":options2, "option3":options3,"option4":options4}
                if answers=="Options1":
                    answers=options1.lower()
                if answers=="Options2":
                    answers=options2.lower()
                if answers=="Options3":
                    answers=options3.lower()
                if answers=="Options4":
                    answers=options4.lower()
                Questions.objects.filter(questionid=request.session['questionid']).update(questions=questions,correct_answer=answers,options=str(options))
                msg={"data":"Question Updated successfully","error":0}
                return JsonResponse(msg,safe=False)
            except Exception:
                Find_error()
                msg={"data":"Server error","error":1}
                return JsonResponse(msg,safe=False)
        else:
            msg={"data":"Invalid Question","error":1}
            return JsonResponse(msg,safe=False)
           
