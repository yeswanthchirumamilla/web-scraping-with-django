from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class LoginForm(AuthenticationForm):
#     remember_me = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

#     # You can also override the default labels, help_text, and widgets
#     username = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
#         label='Username'
#     )

#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
#         label='Password'
#     )

#     # You can add custom validation methods if needed
#     def clean_remember_me(self):
#         remember_me = self.cleaned_data['remember_me']
#         # Your custom validation logic for the 'remember_me' field
#         return remember_me

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

from django import forms
from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import Weather

class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = '__all__'
