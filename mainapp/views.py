from django.shortcuts import *
from django.http import *
from . import myform
from . import logics
from .models import *
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    View,TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
import json

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
#View for login
@login_required(login_url='login')
def loginview(request):
    return render(request, 'login.html')

#homepage view
@login_required(login_url='login')
def homeview(request):
    x=logics.getItem()
    return render(request, 'home.html',{"ItemData" : x})

#redirecting to homepage if one is logged in
@login_required(login_url='login')
def verifylogin(request):
    x=logics.getItem()
    data = myform.MyForm(request.POST)
    if data.is_valid():
        #success
        email=data.cleaned_data['email']
        id = logics.saveUser(email)
        request.session['id']=id
        request.session['email']=email
        return render(request, 'home.html', {"ItemData" : x})

#showing form for new item
@login_required(login_url='login')
def additemview(request):
    return render(request, 'auctionItem.html')

#if form is valid than saving it and redirecting to homepage
@login_required(login_url='login')
def checkitem(request):
    x=logics.getItem()
    if request.method == 'POST':
        data=myform.ItemForm(request.POST, request.FILES)
        print(data)
        if data.is_valid():
            print(request.user.id)
            owner=User.objects.get(email=request.user.email)
            print("here1")
            proname=data.cleaned_data['proname']
            minbid=data.cleaned_data['minbid']
            description=data.cleaned_data['description']
            date= data.cleaned_data['date']
            picture= data.cleaned_data['picture']
            logics.saveItem(proname, minbid, description, date, picture, owner)
            print("here4")
            return render(request, 'home.html',{"ItemData" : x})
        return render(request, 'auctionItem.html')
    return HttpResponseForbidden('allowed only via POST')

#view for showing users posted items
@login_required(login_url='login')
def myitem(request):
    owner=User.objects.get(email=request.user.email)
    x=logics.getMyItem(owner)
    return render(request, 'home.html',{"ItemData" : x})

#view for showing any individual item details
@login_required(login_url='login')
def individualdetails(request, id):
    owner=User.objects.get(email=request.user.email)
    postinfo= Item.objects.get(id=id)
    iteminfo= logics.getProduct(id)
    itembid =logics.getBid(postinfo)
    highestbid= logics.getHighBid(postinfo)
    mybid= logics.getMyBid(owner,postinfo)
    print("Here it is")
    print(postinfo.date)
    if (postinfo.date.date() < datetime.date.today()):
        return render(request, 'productdetailsold.html',{"ItemData" : iteminfo, "BidData": itembid,"high": highestbid, "my":mybid})
    return render(request, 'productdetails.html',{"ItemData" : iteminfo, "BidData": itembid,"high": highestbid, "my":mybid})

#view for saving the bid
@login_required(login_url='login')
def savebid(request, id):
    
    if request.method == 'POST':
        data=myform.BidForm(request.POST)

        if data.is_valid():
            postinfo= Item.objects.get(id=id)
            owner= User.objects.get( email = request.user.email)
            mybid=data.cleaned_data['amount']
           
            highestbid= logics.getHighBid(postinfo)
             # checking if input is Valid
            if (highestbid is None and mybid > postinfo.minbid and postinfo.date.date() >= datetime.date.today() ):
                logics.SaveBid(mybid,  postinfo, owner)

                iteminfo= logics.getProduct(id)
                itembid =logics.getBid(postinfo)
                highestbid= logics.getHighBid(postinfo)
                mybid= logics.getMyBid(owner,postinfo)
                return render(request, 'productdetails.html',{"ItemData" : iteminfo, "BidData": itembid,"high": highestbid, "my":mybid})
            

            elif(mybid > highestbid.amount and mybid > postinfo.minbid and postinfo.date.date() >= datetime.date.today()):
                logics.SaveBid(mybid,  postinfo, owner)

                iteminfo= logics.getProduct(id)
                itembid =logics.getBid(postinfo)
                highestbid= logics.getHighBid(postinfo)
                mybid= logics.getMyBid(owner,postinfo)
                return render(request, 'productdetails.html',{"ItemData" : iteminfo, "BidData": itembid,"high": highestbid, "my":mybid})
            return HttpResponseForbidden('Check your Bid ex: if the bid is expired or maintains the bid')
        return HttpResponseForbidden('Data not valid')
    return HttpResponseForbidden('allowed only via POST')

# View for admin gallery view
class AdminView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/home.html'
    x=logics.getItem()
    def get(self, request, *args, **kwargs):
        
        return render(self.request, self.template_name,{"ItemData" : self.x})

#Admin itemview
class AdminItem(LoginRequiredMixin, TemplateView):
    template_name = 'admin/home.html'
    x=logics.getItemall()
    def get(self, request, *args, **kwargs):
        
        return render(self.request, self.template_name,{"ItemData" : self.x})

#admin stats view
class AdminStat(LoginRequiredMixin, TemplateView):
    template_name = 'admin/stats.html'
    
    

  
    def get(self, request, *args, **kwargs):
        itemcount=logics.getItemCount()
        itemvalue=logics.getItemValue()
        
        start_date = datetime.datetime.now()-datetime.timedelta(days=7)
        end_date = datetime.datetime.now()
        delta = datetime.timedelta(days=1)
        created=[]
        auctioned=[]
        labels=[]
        totalauction=[]
        count=7
        while start_date <= end_date:
            
            created.append(logics.totalCreated(start_date))
            auctioned.append(logics.totalAuctioned(start_date))
            totalauction.append(logics.totalAuctionValue(start_date))
            labels.append(count)
            start_date += delta

            count=count-1
            
        return render(self.request, self.template_name,{"count" : itemcount, 
        "auctionvalue": itemvalue, "created": created, "labels":labels,
        "auctioned":auctioned,
        "totalvalue": totalauction })

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('homeview')
    else:
        form = myform.CreateUserForm()
        if request.method == 'POST':
            form = myform.CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                email = logics.saveUser(form.cleaned_data.get('email'))
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homeview')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user.id)

            if user is not None:
                login(request, user)
                return redirect('homeview')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def delete(request):
	p = Post.objects.get(pk=request.POST.get('id', ''))
	p.delete()
	messages.info(request, 'Post deleted successfully')
	return redirect('blog-home')

def deleteitem(request, id):
    p = Item.objects.get(pk=id)
    p.delete()
    return redirect('homeview')
