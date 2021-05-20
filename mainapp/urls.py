from django.urls import *
from . import views

urlpatterns = [
    path('', views.loginview, name="loginpage"),
    path('addAuction/', views.additemview, name="additem"),
    path('checkitem/', views.checkitem, name="checkformdata"),
    path('verifylogin/', views.verifylogin, name="checklogin"),
    path('myitem/', views.myitem, name="myitem"),
    path('itemdetails/<int:id>' , views.individualdetails, name = 'itemview'),
    path('home/', views.homeview, name="homeview"),
    path('savebid/<int:id>', views.savebid, name="savebid"),

    
]