from django.db import models
import uuid
from app.model.topic import Topics
class Feedback(models.Model):
    Feedbackid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    user = models.UUIDField()
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    Feedback =models.CharField(max_length=600)
    create_At=models.DateTimeField(auto_now_add=True)
