from django.db import models

# Create your models here.
class Post(models.Model):
    user= models.TextField(unique=True)
    #username= models.CharField(max_length=300, unique=True)
    q1= models.TextField()
    q2= models.TextField()
    q3= models.TextField()
    q4= models.TextField()
    q5= models.TextField()
    q6= models.TextField()
    q7= models.TextField()
    q8= models.TextField()
    q9= models.TextField()
    q10= models.TextField()