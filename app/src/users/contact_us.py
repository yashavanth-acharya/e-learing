# from model.course import Courses
from django.views.generic import TemplateView
from django.http import JsonResponse
from app.model.contanct_us import contactus

class Contactus(TemplateView):
    def post(self, request):
        name= request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        msg=request.POST['msg']
        try:
            contactus(name=name, email=email, mobile=phone,msg=msg).save()
            return JsonResponse({"data":"Thank you","error":0})
        except Exception as e:
            print(e)
            return JsonResponse({"data":"Server error ","error":1})
        