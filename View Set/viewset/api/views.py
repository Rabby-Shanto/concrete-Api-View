from django.shortcuts import render
from .models import Teacher
from serializers import TeacherSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.


