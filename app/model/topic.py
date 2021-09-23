from django.db import models
import uuid
from app.model.course import Courses
class Topics(models.Model):
    topicid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    icon = models.TextField()
    course=models.ForeignKey(Courses, on_delete=models.CASCADE)
    topicname =models.CharField(max_length=200,unique=True)
    topic_Descriptions = models.CharField(max_length=200)
    duration= models.IntegerField()
    marks_for_pre_question = models.FloatField()
    minimum_mark = models.IntegerField()
    status = models.BooleanField(default=False)
    create_At=models.DateTimeField(auto_now_add=True)
    updated_At=models.DateTimeField(auto_now=True)
