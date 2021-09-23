from django.db import models
from django.utils import timezone
import uuid
from .user import Userdetails
class Result(models.Model):
    Resultid = models.UUIDField(primary_key = True,default=uuid.uuid4,editable = False)
    user=models.ForeignKey(Userdetails, on_delete=models.CASCADE,default=timezone.now)
    topic=models.CharField(max_length=200)
    totalmark = models.CharField(max_length=200)
    outof= models.CharField(max_length=200,)
    submitted_time = models.DateTimeField()
    feedback_status = models.BooleanField(default=False)
    create_At=models.DateTimeField(auto_now_add=True)
    

