from app.model.user import Userdetails
from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from app.auth.hashpassword import verify_password
from app.auth.hashpassword import gethashpassword
from django.http import JsonResponse
from app.auth.userauth import check_user_login

class userchangepassword(TemplateView):
    @check_user_login
    def get(self,request):
        return render(request,"user/changepassword.html")
        
    
    def post(self,request):
        oldpassword=request.POST['oldpassword']
        password=request.POST['password']

        if len(oldpassword)==0 or len(password)==0:
            return JsonResponse({'data':"Given fielda is required *","error":1})

        if len(password)>32 or len(password)<8 or len(oldpassword)>32 or len(oldpassword)<8:
            return JsonResponse({'data':"Password lenght sholud be between 8 or 32","error":1})
        if 'user' in request.session:
            usertype=request.session['user']['user']
        else:
            usertype=request.session['admin']['user']
        user=Userdetails.objects.filter(userid=usertype)
        # print(username[0])
        if user:
            if verify_password(oldpassword,user[0].password):
               user.update(password=str(gethashpassword(password)))
               return JsonResponse({'data':"Password changed successfully","error":0})
            else:
                return JsonResponse({'data':"Invalid password","error":1})

        return JsonResponse({'data':"Invaild user","error":1})