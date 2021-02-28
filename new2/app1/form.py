from django import forms
from app1.models import *

class signupform(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'bb', 'placeholder':'full name'}), label=" ", max_length=50)
    mobile =  forms.CharField(widget=forms.TextInput(attrs={'class':'bb', 'placeholder':'Mobile No.'}), label=" ", max_length=13)
    email_id =  forms.CharField(widget=forms.TextInput(attrs={'class':'bb', 'placeholder':'Email ID'}), label=" ", max_length=50)
    password =  forms.CharField(widget=forms.TextInput(attrs={'class':'bb', 'placeholder':'Password'}), label=" ", max_length=50)
    pin_code =  forms.CharField(widget=forms.TextInput(attrs={'class':'bb', 'placeholder':'Pin Code'}), label=" ", max_length=10)
    address =  forms.CharField(widget=forms.TextInput(attrs={'class':'bb', 'placeholder':'Address'}), label=" ", max_length=150)
    class Meta():
        model = signup
        fields = ('full_name', 'mobile', 'email_id', 'password', 'pin_code', 'address',)

class loginform(forms.Form):
    email_id =  forms.CharField(widget=forms.TextInput(attrs={'class':'bb', 'placeholder':'Email ID'}), label=" ", max_length=50)
    password =  forms.CharField(widget=forms.TextInput(attrs={'class':'bb', 'placeholder':'Password'}), label=" ", max_length=50)