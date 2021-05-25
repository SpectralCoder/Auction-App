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

# Create your views here.
#View for login
def loginview(request):
    return render(request, 'login.html')

#homepage view
def homeview(request):
    x=logics.getItem()
    return render(request, 'home.html',{"ItemData" : x})

#redirecting to homepage if one is logged in
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
def additemview(request):
    return render(request, 'auctionItem.html')

#if form is valid than saving it and redirecting to homepage
def checkitem(request):
    x=logics.getItem()
    if request.method == 'POST':
        data=myform.ItemForm(request.POST, request.FILES)
        if data.is_valid():
            owner=User.objects.get(id=request.session['id'])
            proname=data.cleaned_data['proname']
            minbid=data.cleaned_data['minbid']
            description=data.cleaned_data['description']
            date= data.cleaned_data['date']
            picture= data.cleaned_data['picture']
            logics.saveItem(proname, minbid, description, date, picture, owner)
            return render(request, 'home.html',{"ItemData" : x})
        return render(request, 'auctionItem.html')
    return HttpResponseForbidden('allowed only via POST')

#view for showing users posted items
def myitem(request):
    owner=User.objects.get(id=request.session['id'])
    x=logics.getMyItem(owner)
    return render(request, 'home.html',{"ItemData" : x})

#view for showing any individual item details
def individualdetails(request, id):
    print("ID is", id)
    owner=User.objects.get(id=request.session['id'])
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
def savebid(request, id):
    
    if request.method == 'POST':
        data=myform.BidForm(request.POST)

        if data.is_valid():
            postinfo= Item.objects.get(id=id)
            owner=User.objects.get(id=request.session['id'])
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