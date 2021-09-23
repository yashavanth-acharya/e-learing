from app.model.user import Userdetails
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
import re
from app.auth.hashpassword import gethashpassword
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex2 = r"^[1-9][0-9]{5}$"
mobile_regex = r'^[0][1-9]\d{9}$|^[1-9]\d{9}$'
from ..finderror import *
from app.auth.userauth import check_user_login


class profile(TemplateView):
    @check_user_login
    def get(self,request):
        msg={'data':Userdetails.objects.get(userid=request.session['user']['user']),"dates":str(Userdetails.objects.get(userid=request.session['user']['user']).date_of_birth)[0:10]}
        return render(request,"user/profile.html",msg)

    @check_user_login
    def post(self,request):
        username=request.POST['username']
        name = request.POST['name']
        # gender=request.POST['gender']
        gender="gender"
        email =request.POST['email']
        mobile= request.POST['mobile']
        date_of_birth =request.POST['date']
        address = request.POST['address']
        # city= request.POST['city']
        # state= request.POST['state']
        city= "city"
        state= "state"
        pincode=request.POST['pincode']

        
        if len(name)==0 or len(username)==0 or len(gender)==0 or len(pincode)==0 or len(mobile)==0 or len(email)==0 or \
        len(date_of_birth)==0 or len(address)==0 or len(city)==0 or len(state)==0:
            return JsonResponse({'data':"Given fielda is required *","error":1})

        if username.isalnum() == False:
            return JsonResponse({'data':"Username required alphanumeric characters, without symbols","error":1})

        if(re.match(regex, email)) == None:
            return JsonResponse({'data':"Enter valid email address","error":1})


        if(re.match(mobile_regex,mobile)) == None:
            return JsonResponse({'data':"Enter valid Mobile","error":1})
        
        if(re.match(regex2, pincode)) == None:
            return JsonResponse({'data':"Enter valid pincode","error":1})

        if Userdetails.objects.get(username=username.lower()).userid != Userdetails.objects.get(userid=request.session['user']['user']).userid:
            return JsonResponse({'data':"Username already exists","error":1})

        try:
            Userdetails.objects.filter(userid=request.session['user']['user']).update(
                username =username.lower(),
                name = name,
                # gender= gender,
                email = email,
                mobile= mobile,
                date_of_birth = date_of_birth,  
                address = address,
                # city= city,
                # state= state,
                pincode=pincode)
    
            return JsonResponse({'data':"Your Account Updated successfully","error":0})

        except Exception as e:
            Find_error()
            return JsonResponse({'data':"Server error","error":1})
        
