from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #HTTPRequest
    return HttpResponse("Главная страница. Тут будет список учебных материалов.")
