from django.urls import *
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    AdminView, AdminItem, AdminStat
)
from django.contrib.admin.views.decorators import staff_member_required



urlpatterns = [
    #regular User
    path('', views.homeview, name="homeview"),

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

    #saving bids for any individual item
    path('savebid/<int:id>', views.savebid, name="savebid"),

    #admin login
    path( 'admin/', auth_views.LoginView.as_view(), name="login"),
    
    #Admin home
    path('admin/home/', staff_member_required(AdminView.as_view()), name="adminhome"),

    #viewing all the items
    path('admin/item/', staff_member_required(AdminItem.as_view()), name="adminitem"),

    #stat page
    path('admin/stat/', staff_member_required(AdminStat.as_view()), name="adminstat"),
    
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('deleteitem/<int:id>' , views.deleteitem, name = 'delete'),
    
]