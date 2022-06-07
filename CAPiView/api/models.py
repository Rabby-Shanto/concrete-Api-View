import email
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    address = models.CharField(max_length=250)
    email = models.EmailField()

    

    
