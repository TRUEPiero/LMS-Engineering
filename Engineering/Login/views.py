from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from . import forms

# Create your views here.
class LoginUser(LoginView):
    form_class = forms.LoginUser
    template_name = 'Login/index.html'
    extra_context = {'title': 'Авторизация'}

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
