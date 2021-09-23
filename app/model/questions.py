from django.db import models
import uuid
from app.model.topic import Topics
class Questions(models.Model):
    questionid = models.UUIDField(unique = True,default = uuid.uuid4,editable = False)
    topic=models.ForeignKey(Topics, on_delete=models.CASCADE)
    questions = models.CharField(max_length=1000)
    options=models.TextField()
    correct_answer=models.CharField(max_length=500)
    create_At=models.DateTimeField(auto_now_add=True)
    updated_At=models.DateTimeField(auto_now=True)
