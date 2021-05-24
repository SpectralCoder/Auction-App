from django.urls import *
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    AdminView, AdminItem, AdminStat
)


urlpatterns = [
    path('', views.loginview, name="loginpage"),
    path('addAuction/', views.additemview, name="additem"),
    path('checkitem/', views.checkitem, name="checkformdata"),
    path('verifylogin/', views.verifylogin, name="checklogin"),
    path('myitem/', views.myitem, name="myitem"),
    path('itemdetails/<int:id>' , views.individualdetails, name = 'itemview'),
    path('home/', views.homeview, name="homeview"),
    path('savebid/<int:id>', views.savebid, name="savebid"),
    path( 'admin/', auth_views.LoginView.as_view(), name="login"),
    # path( 'accounts/profile/', views.homeview, name="login"),
    path('admin/home/', AdminView.as_view(), name="adminhome"),
    path('admin/item/', AdminItem.as_view(), name="adminitem"),
    path('admin/stat/', AdminStat.as_view(), name="adminstat"),
    
    
]