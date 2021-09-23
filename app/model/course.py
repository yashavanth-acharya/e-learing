from django.db import models
import uuid

class Courses(models.Model):
    courseid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    icon = models.TextField()
    coursename =models.CharField(max_length=200,unique=True)
    course_Descriptions = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    create_At=models.DateTimeField(auto_now_add=True)
    updated_At=models.DateTimeField(auto_now=True)

