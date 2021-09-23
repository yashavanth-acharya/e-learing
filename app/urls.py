from django.urls import path
from .src.login import Login,Logout
from .src.users.home import Home
from .src.singup import Singup
from .src.users.course import Course
from .src.users.topic import Topic,check_topic_id
from .src.users.topicdetilas import Topicinfo
from .src.users.mcq import Mcq
from .src.users.result import Results,GetResults
from .src.users.changepassword import userchangepassword
from .src.users.userfeedback import userfeedback
from .src.users.userprofile import profile
from .src.users.contact_us import Contactus
from .src.users.topicdocuments import Topicdocumentview


from .src.admin.dashboard import Dashboard
from .src.admin.course import Addcourse,Editcourses
from .src.admin.viewcourse import Viewcourse,getcourse,DeleteCourse
from .src.admin.topic import Addtopic,Edittopic
from .src.admin.viewtopic import Viewtopic,gettopic,DeleteTopic

from .src.admin.viewquestions import ViewAddedtopic,ViewNexth,Deletequestion
from .src.admin.addquestions import AddQuestions,Editquestions
from .src.admin.users import User,Getuser,adminchangepassword
from .src.admin.status import CoursesStatus,TopicStatus
from .src.admin.userfeedback import Userfeedback,getFeedback
from .src.admin.userquery import userquery,getuserquery
from .src.admin.studentresult import ViewResult,GetstudentResults
from .src.admin.viewdocument import Viewdocument,Getdocuments
from .src.admin.document import Editdocuments,Deletedocument

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('login', Login.as_view(),name='login'),
    path('signup', Singup.as_view(),name='Singup'),
    path('Course', Course.as_view(),name='Course'),
    path('topic/<str:id>/', Topic.as_view(),name='Topic'),
    path('topicdetails/<str:id>', Topicinfo.as_view(),name='topicinfo'),
    path('attempt/<str:id>', Mcq.as_view(),name='topicinfo'),
  
    path('checktopic', check_topic_id.as_view(),name='checktopic'),
    path('results', Results.as_view(),name='Result'),
    path('getresults', GetResults.as_view(),name='getresults'),
    path('changepassword', userchangepassword.as_view(),name='changepassword'),
    path('feedback', userfeedback.as_view(),name='feedback'),
    path('profile', profile.as_view(),name='profile'),
    path('contactus', Contactus.as_view(),name='contactus'),
    path('topicdocument/<str:id>', Topicdocumentview.as_view(),name='contactus'),







    #admin
    path('dashboard', Dashboard.as_view(),name='Dashboard'),
    
    path('addcourse', Addcourse.as_view(),name='Addcourse'),
    path('courses', Viewcourse.as_view(),name='Viewcourse'),
    path('getcourse', getcourse.as_view(),name='getcourse'),
    path('editcourse', Editcourses.as_view(),name='Editcourses'),
    path('deletecourse', DeleteCourse.as_view(),name='DeleteCourse'),

    path('addtopic', Addtopic.as_view(),name='Addtopic'),
    path('topic', Viewtopic.as_view(),name='Viewtopic'),
    path('gettopic', gettopic.as_view(),name='gettopic'),
    path('edittopic', Edittopic.as_view(),name='Edittopic'),
    path('deletetopic', DeleteTopic.as_view(),name='DeleteTopic'),

    path('viewaddedtopic', ViewAddedtopic.as_view(),name='ViewAddedtopic'),
    path('questions', ViewNexth.as_view(),name='ViewNexth'),
    path('addquestion', AddQuestions.as_view(),name='AddQuestions'),
    path('editquestion', Editquestions.as_view(),name='Editquestions'),
    path('deletequestion', Deletequestion.as_view(),name='Deletequestion'),

    path('students', User.as_view(),name=''),
    path('getuser', Getuser.as_view(),name='Getuser'),
    path('coursestatus',CoursesStatus.as_view(),name='CoursesStatus'),
    path('topicstatus',TopicStatus.as_view(),name='TopicStatus'),
    path('adminchangepassword',adminchangepassword.as_view(),name='changepassword'),
    path('userfeedback',Userfeedback.as_view(),name='userfeedback'),
    path('getFeedback',getFeedback.as_view(),name='getFeedback'),
    path('userquerys',userquery.as_view(),name='userquery'),
    path('getuserquery',getuserquery.as_view(),name='getuserquery'),
    path('studentresult',ViewResult.as_view(),name='studentresult'),
    path('getstudentresult',GetstudentResults.as_view(),name='getstudentresult'),
    path('document',Viewdocument.as_view(),name='document'),
    path('getdocument',Getdocuments.as_view(),name='getdocument'),
    path('editdocuments',Editdocuments.as_view(),name='editdocuments'),
    path('deletedocument',Deletedocument.as_view(),name='deletedocument'),






    
    path('logout', Logout.as_view(),name='Logout'),








]


# sudo docker build -t Elearning.azurecr.io/elearning:latest .
# sudo docker push Elearning.azurecr.io/elearning:latest