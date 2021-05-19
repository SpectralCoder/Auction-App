from django.urls import *
from . import views

urlpatterns = [
    path('', views.loginview, name="loginpage"),
    path('addAuction/', views.additemview, name="additem"),
    path('checkitem/', views.checkitem, name="checkformdata"),
    path('verifylogin/', views.verifylogin, name="checklogin"),

    
]