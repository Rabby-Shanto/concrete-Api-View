import email
from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
