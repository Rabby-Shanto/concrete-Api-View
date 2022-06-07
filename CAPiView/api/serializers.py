from rest_framework import serializers
from .models import Student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','address','email']