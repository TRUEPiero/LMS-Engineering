from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

class LoginUser(AuthenticationForm):
    username = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control-material', 'placeholder':'ЛОГИН'}))
    password = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control-material', 'placeholder':'ПАРОЛЬ'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
