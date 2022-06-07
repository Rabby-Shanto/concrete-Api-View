from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.student_list.as_view()),
    # path('students/', views.student_create.as_view()),
    # path('students/<int:pk>', views.student_retrieve.as_view()),
    path('students/<int:pk>', views.student_update.as_view()),
]
