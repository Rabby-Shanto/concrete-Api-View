from unicodedata import name
from django.contrib import admin
from .models import Student

@admin.register(Student)

class studenyAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','address','email']
