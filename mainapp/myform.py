from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyForm(forms.Form):
    email=forms.EmailField()

class ItemForm(forms.Form):
    proname= forms.CharField(max_length=100)
    minbid= forms.IntegerField()
    description= forms.CharField(max_length=1000)
    picture = forms.ImageField()
    date= forms.DateField()

class BidForm(forms.Form):
    amount= forms.IntegerField()

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']