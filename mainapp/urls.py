from django.urls import *
from . import views

urlpatterns = [
    path('', views.loginview, name="homepage"),
    path('verifylogin/', views.verifylogin, name="checklogin"),

    
]