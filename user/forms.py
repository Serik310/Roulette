from django import forms
from django.contrib.auth import get_user_model
from .models import CustomUser

class LoginForm(forms.Form):

    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
