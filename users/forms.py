from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# This is done so you can add fields to the user account.
# 1.  must inherit base form (UserCreationForm)
# 2.  Create class and add the field you want.
class UserRegisterForm(UserCreationForm):
    email   = forms.EmailField()
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username','password1','password2','firstname','lastname','email']


class UserUpdateForm(forms.ModelForm):
    email   = forms.EmailField()
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username','firstname','lastname','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','user_access']