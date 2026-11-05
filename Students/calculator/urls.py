from django.urls import path
from . import views

urlpatterns = [
    path("", views.calculator, name="calculator"),
    path("calculator/result/", views.calculator_result, name="calculator_result"),
]