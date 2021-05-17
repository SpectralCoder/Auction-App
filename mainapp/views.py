from django.shortcuts import *
from django.http import *
from . import myform
from . import logics


# Create your views here.
def loginview(request):

    return render(request, 'login.html')

def verifylogin(request):
    data = myform.MyForm(request.POST)
    if data.is_valid():
        #success
        email=data.cleaned_data['email']
        id = logics.saveUser(email)
        request.session['id']=id
        request.session['email']=email
        # SessionManager.saveSessionId(id)
        # b=SessionManager.getSessionId()
        # print(b)
        # if request.session.has_key('id'):
        #     username = request.session['id']
        return render(request, 'home.html')



    