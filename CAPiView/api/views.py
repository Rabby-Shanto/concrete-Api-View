from functools import partial
from pickle import TRUE
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView


class student_list(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class student_create(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class student_retrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class student_update(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class student_destroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer




