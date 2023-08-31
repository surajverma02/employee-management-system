"""
Emp Urls
"""
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("home/", empHome),
    path("add-emp/", addEmp),
    path("del-emp/<int:empid>", delEmp),
    path("update-emp/<int:empid>", updateEmp),
    path("updated/<int:empid>", updated),
    path("testimonials/", Testimonial)
]