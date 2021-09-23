# from model.course import Courses
from django.views.generic import TemplateView
from django.http import JsonResponse
from app.model.topic import Topics
from app.model.Feedback import Feedback
from app.model.result import Result
from ..finderror import *
from app.auth.userauth import check_user_login


class userfeedback(TemplateView):
    @check_user_login
    def post(self, request):
        result_id= request.POST['id']
        feedback=request.POST['feedback']
    
        try:
            results=Result.objects.filter(Resultid=result_id,user_id=request.session['user']['user'])
            if results:
                Feedback(user=request.session['user']['user'],topic_id=Topics.objects.get(topicname=results[0].topic).topicid,Feedback=feedback).save()
                results.update(feedback_status=True)
                return JsonResponse({"data":"Thanks for your feedback","error":0})
        except Exception as e:
            Find_error()
            return JsonResponse({"data":"Server error ","error":1})
        
        else:
            return JsonResponse({"data":"Invalid ","error":1})