from django.db import models
import uuid
from app.model.topic import Topics

class Topicsdocuments(models.Model):
    documentid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    document = models.TextField()
    topic=models.ForeignKey(Topics, on_delete=models.CASCADE)
    create_At=models.DateTimeField(auto_now_add=True)
    updated_At=models.DateTimeField(auto_now=True)
