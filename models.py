from django.db import models

# Create your models here.
class student_data(models.Model):
    first_name=models.CharField(max_length=255,null=True,blank=True)
    last_name=models.CharField(max_length=255,null=True,blank=True)
    email=models.CharField(max_length=255,null=True,blank=True)
    gender=models.CharField(max_length=255,null=True,blank=True)
