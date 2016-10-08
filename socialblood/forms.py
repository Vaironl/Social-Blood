from django import forms
from socialblood.models import Request
from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     password2 = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password', 'password2')

class UserForm(forms.ModelForm):
    """Creates a user, with no priveleges from the given username and password"""
    error_messages = {'password_mismatch' : ("The two password fields didn't match.")}
    password1 = forms.CharField(label=("Password"),widget=forms.PasswordInput())
    password2 = forms.CharField(label=("Password confirmation"), widget=forms.PasswordInput(),
                                help_text=("Enter the same password as above, for verification"))

    class Meta:
        model = User
        fields = ("username","email",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'],code='password_mistach',)
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            return user



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

    class Meta:
        model = Request
        fields = ('blood_type','location')