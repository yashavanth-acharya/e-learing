# from model.course import Courses
from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect


class Home(TemplateView):
    def get(self,request):
        # if 'user' in request.session:
            # try:
            #    data=Courses.objects.all()
            # except Exception as e:
            #     print(e)
            #     data=[]

        return render(request,"home.html")
        # else:
        #     return redirect("/")
            