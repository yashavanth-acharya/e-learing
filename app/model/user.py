from django.db import models
import uuid

class Userdetails(models.Model):
    userid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    username =models.CharField(max_length=200,unique=True)
    name = models.CharField(max_length=200,)
    # gender= models.CharField(max_length=200,)
    email = models.EmailField(max_length=200)
    mobile= models.CharField(max_length=14)
    date_of_birth = models.DateTimeField()
    address = models.CharField(max_length=500,)
    # city= models.CharField(max_length=100,)
    # state= models.CharField(max_length=100,)
    pincode=models.IntegerField()
    password = models.CharField(max_length=100,)
    user_role = models.CharField(max_length=100,default='user')
    create_At=models.DateTimeField(auto_now_add=True)
    updated_At=models.DateTimeField(auto_now=True)

