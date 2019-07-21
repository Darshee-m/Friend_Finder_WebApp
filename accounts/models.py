from django.db import models

# Create your models here.
class Users(models.Model):
    user= models.TextField(unique=True)
    email= models.TextField()
    mobileno=models.TextField()
    gender=models.TextField()
    city=models.TextField()
    country=models.TextField()