from django import forms
from django.forms import CharField, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=15, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=300, help_text='Required. Please enter a valid email')
    password1 = forms.CharField(max_length=25, help_text="password")
    password2 = forms.CharField(max_length=25, help_text="Repeat password please")
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

