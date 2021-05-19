from django.shortcuts import *
from django.http import *
from . import myform
from . import logics
from .models import *


# Create your views here.
def loginview(request):
    return render(request, 'login.html')

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

def additemview(request):
    return render(request, 'auctionItem.html')

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
            x=logics.getItem()
            print("Your data")
            print(x)
            return render(request, 'home.html',{"ItemData" : x})
        return render(request, 'auctionItem.html')
    return HttpResponseForbidden('allowed only via POST')



    