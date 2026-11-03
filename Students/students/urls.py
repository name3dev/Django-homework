from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_register, name='student_register'),
    path('student/result/', views.student_result, name='student_result'),
]