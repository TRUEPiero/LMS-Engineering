from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    if request.GET:    # Проверка сессии в куках
        return redirect("login", permanent=True)    # Переадрисация на страницу авторизации

    # template_string = render_to_string('Study/index.html')
    # return HttpResponse(template_string)
    return render(request,'Study/index.html')
    # return HttpResponse(f"Главная страница. Тут будет список учебных материалов.")


def show_exercise(reqest, Ex_id):
    print(reqest.GET)
    return HttpResponse(f'Страница задания<br>Страница №{Ex_id}')


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")
