from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from . import models
from . import forms


# Create your views here.
def index(request):
    if request.GET:    # Проверка сессии в куках
        return redirect("login", permanent=True)    # Переадрисация на страницу авторизации

    all_modules = models.Modules_of_education_materials.objects.all()
    all_exercise = models.Education_materials.objects.all()

    options = {
        'title': 'LMS Engineering',
        'all_modules': all_modules,
        'all_exercise': all_exercise,
        'user':'Акбашев Владислав'
    }

    return render(request,'Study/index.html', options)


def show_exercise(request, ex_slug):

    exercise = get_object_or_404(models.Education_materials, slug=ex_slug)

    exercise_data = {
        'id': exercise.pk,
        'date_created': exercise.date_created,
        'title': exercise.title,
        'discription': exercise.discription,
        'deadline': exercise.deadline,
        'file': exercise.file,
        'type': exercise.type,
        'module': exercise.module,
    }

    options = {
        'title': exercise.title,
        'user':'Акбашев Владислав',
        'exercise_data': exercise_data,
    }

    return render(request, 'Study/exercise.html', options)


def new_exercise(request, module_slug):

    module = get_object_or_404(models.Modules_of_education_materials,slug=module_slug)
    all_modules = models.Modules_of_education_materials.objects.exclude(slug=module_slug)
    all_types = models.Type_of_education_materials.objects.all()

    form = forms.AddNewExercise

    options = {
        'title': 'Новое задание',
        'user': 'Акбашев Владислав',
        'form': form
    }

    return render(request, 'Study/new_exercise.html', options)


def new_exercise_post(request):

    title           = request.POST.get('title')
    discription     = request.POST.get('discription')
    deadline        = request.POST.get('deadline')
    type_id         = request.POST.get('selected_type')
    module_id       = request.POST.get('selected_module')
    file            = request.POST.get('file')

    selected_type = get_object_or_404(models.Type_of_education_materials, pk=type_id)
    selected_module = get_object_or_404(models.Modules_of_education_materials, pk=module_id)

    new_exercise = models.Education_materials(title=title, discription=discription, type=selected_type, module=selected_module, deadline=deadline, file=file)
    new_exercise.save()

    all_modules = models.Modules_of_education_materials.objects.all()
    all_exercise = models.Education_materials.objects.all()

    options = {
        'title': 'LMS Engineering',
        'all_modules': all_modules,
        'all_exercise': all_exercise,
        'user':'Акбашев Владислав'
    }

    return redirect("home", permanent=True)



def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")
