from django.urls import *
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    AdminView, AdminItem, AdminStat
)


urlpatterns = [
    #regular User
    path('', views.loginview, name="loginpage"),

    #Adding auction form
    path('addAuction/', views.additemview, name="additem"),

    #verifying auction form
    path('checkitem/', views.checkitem, name="checkformdata"),

    #regular user login verify
    path('verifylogin/', views.verifylogin, name="checklogin"),

    #Showing users posted item
    path('myitem/', views.myitem, name="myitem"),

    #individual auction data 
    path('itemdetails/<int:id>' , views.individualdetails, name = 'itemview'),

    #GalleryView
    path('home/', views.homeview, name="homeview"),

    #saving bids for any individual item
    path('savebid/<int:id>', views.savebid, name="savebid"),

    #admin login
    path( 'admin/', auth_views.LoginView.as_view(), name="login"),
    
    #Admin home
    path('admin/home/', AdminView.as_view(), name="adminhome"),

    #viewing all the items
    path('admin/item/', AdminItem.as_view(), name="adminitem"),

    #stat page
    path('admin/stat/', AdminStat.as_view(), name="adminstat"),
    
    
]