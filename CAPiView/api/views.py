from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView


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

# get and post method at the same time 

class student_lscview(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class student_rudview(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


