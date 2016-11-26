from django import forms
from socialblood.models import Request
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


BLOOD_TYPES = ('A+', 'A+'),\
              ('A-', 'A-'),\
              ('B+', 'B+'),\
              ('B-', 'B-'),\
              ('AB+', 'AB+'),\
              ('AB-', 'AB-'),\
              ('O+', 'O+'),\
              ('O-', 'O-'),

class RequestForm(forms.ModelForm):
    blood_type = forms.ChoiceField(choices=BLOOD_TYPES, required = True)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required= True , error_message= ("Phone number must be entered in the format:"
                                                    " '+999999999'. Up to 15 digits allowed."))

    class Meta:
        model = Request
        fields = ('blood_type','location', 'phone_number')

class DeleteRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = []