# login/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render 


class SignUpForm(UserCreationForm):
    # Add any additional fields you added to the CustomUser model
    # For example, you can add 'profile_picture' field.
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
