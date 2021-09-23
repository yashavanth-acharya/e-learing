from django.db import models
import uuid

class contactus(models.Model):
    contactusid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name= models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    mobile= models.CharField(max_length=14)
    msg =models.CharField(max_length=600)
    create_At=models.DateTimeField(auto_now_add=True)
