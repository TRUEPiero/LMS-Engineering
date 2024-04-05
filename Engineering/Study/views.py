from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


exercise = ['Задание 1','Задание 2', 'Задание 3', 'Задание 4']

# Create your views here.
def index(request):
    if request.GET:    # Проверка сессии в куках
        return redirect("login", permanent=True)    # Переадрисация на страницу авторизации

    options = {
        'title': 'LMS Engineering',
        'exercise': exercise,
        'user':'АКБАШЕВ ВЛАДИСЛАВ'
    }
    
    return render(request,'Study/index.html', options)


def show_exercise(request, Ex_id):

    options = {
        'title': 'Задание ' + str(Ex_id),
        'Ex_id':Ex_id,
        'user':'АКБАШЕВ ВЛАДИСЛАВ'
    }

    return render(request, 'Study/exercise.html', options)
    # return HttpResponse(f'Страница задания<br>Страница №{Ex_id}')


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")
