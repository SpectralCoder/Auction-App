from django import forms

class MyForm(forms.Form):
    email=forms.EmailField()

class ItemForm(forms.Form):
    proname= forms.CharField(max_length=100)
    minbid= forms.IntegerField()
    description= forms.CharField(max_length=1000)
    picture = forms.ImageField()
    date= forms.DateField()