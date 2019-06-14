from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# This is done so you can add fields to the user account.
# 1.  must inherit base form (UserCreationForm)
# 2.  Create class and add the field you want.
class UserRegisterForm(UserCreationForm):
    email   = forms.EmailField()
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    class Meta:
        model = User
        fields = ['username','password1','password2','first_name','last_name','email']


class UserUpdateForm(forms.ModelForm):
    email   = forms.EmailField()
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','user_access']