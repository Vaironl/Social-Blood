from django import forms
from socialblood.models import Request
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password =  forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class RequestForm(forms.ModelForm):
    blood_type = forms.CharField(label="Blood Type", max_length=4)

    class Meta:
        model = Request
        fields = ('blood_type','location',)