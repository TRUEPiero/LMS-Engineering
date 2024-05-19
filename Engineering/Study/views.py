from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from . import models, forms
from django.views import View
from django.views.generic import TemplateView, DetailView, FormView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from Login.models import StudentGroup

# Create your views here.
# @login_required()
# def index(request):
#     all_sections = models.Sections_of_modules.objects.all()

#     dict_sections = {}

#     for section in all_sections:
#         dict_sections[section] = []
#         modules = models.Modules_of_education_materials.objects.filter(section=section)
#         for fmodule in modules:
#             dict_module = {}
#             dict_module[fmodule] = models.Education_materials.objects.filter(module=fmodule)
#             dict_sections[section].append(dict_module)

#     options = {
#         'sections': dict_sections,
#         'title':'LMS Engineering'
#     }

#     return render(request, 'Study/index.html', options)
def create_sectiondict(section):

    dict_sections = {}

    for section in section:
        dict_sections[section] = []
        modules = models.Modules_of_education_materials.objects.filter(section=section)
        for fmodule in modules:
            dict_module = {}
            dict_module[fmodule] = models.Education_materials.objects.filter(module=fmodule).order_by("date_created")
            dict_sections[section].append(dict_module)

    return dict_sections


def create_comletedEx_dict(groups):

    dict_Exersices = {}

    for group in groups:
        dict_Exersices[group] = []
        User = get_user_model()
        users = User.objects.order_by('first_name').filter(study_group=group)
        for fuser in users:
            dict_comleted_ex = {}
            dict_execisesgrades = {}

            c_exercises = models.CompletedEx.objects.filter(student=fuser).order_by("-date_created")
            for ex in c_exercises:
                grade_obj = models.Grades.objects.filter(complete_exercise = ex)
                if grade_obj:
                    dict_execisesgrades[ex] = grade_obj[0]
                else:
                    dict_execisesgrades[ex] = ''

            dict_comleted_ex[fuser] = dict_execisesgrades
            dict_Exersices[group].append(dict_comleted_ex)

    return dict_Exersices

class MainPage(LoginRequiredMixin,TemplateView):

    template_name='Study/index.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        main_sections = models.Sections_of_modules.objects.filter(is_first=False,is_last=False)
        first_sections = models.Sections_of_modules.objects.filter(is_first=True,is_last=False)
        last_sections = models.Sections_of_modules.objects.filter(is_first=False,is_last=True)

        context['sections_first'] = create_sectiondict(first_sections)
        context['sections_main'] = create_sectiondict(main_sections)
        context['sections_last'] = create_sectiondict(last_sections)
        context['title'] = 'LMS Engineeging'
        return context
    # pass

class ShowExercise(LoginRequiredMixin,DetailView):
    model = models.Education_materials
    template_name = 'Study/exercise.html'
    slug_url_kwarg = 'ex_slug'
    context_object_name = 'object'


    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = context['object'].title

        completed_ex_dict = {}
        completed_ex = models.CompletedEx.objects.filter(student=self.request.user, education_material=context['object'])
        for ex in completed_ex:
            grade_obj = models.Grades.objects.filter(complete_exercise = ex)
            if grade_obj:
                completed_ex_dict[ex] = grade_obj[0]
            else:
                completed_ex_dict[ex] = ''

        context['completed_ex'] = completed_ex_dict
        return context


class NewExercise(LoginRequiredMixin,CreateView):
    form_class = forms.AddNewExercise
    template_name = 'Study/new_exercise.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новое задание'
        return context


    def get_form_kwargs(self):
        context = super().get_form_kwargs()
        context['current_module'] = get_object_or_404(models.Modules_of_education_materials, slug=self.kwargs['module_slug'])
        return context


    def form_valid(self, form):
        ex = form.save(commit=False)
        ex.author = self.request.user
        return super().form_valid(form)


class DeleteExercise(LoginRequiredMixin,DeleteView):
    model = models.Education_materials
    slug_url_kwarg = 'ex_slug'
    success_url = reverse_lazy('home')


class UpdateExercise(LoginRequiredMixin,UpdateView):
    model = models.Education_materials
    slug_url_kwarg = 'ex_slug'
    fields = ['title', 'module','type', 'discription','deadline', 'files']
    template_name = 'Study/update_ex.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


@login_required()
def new_grade(request, ex_slug):
    if request.POST:
        completed_exercise = get_object_or_404(models.CompletedEx, pk=request.POST['completed_ex_id'])

        grade_obj = models.Grades.objects.filter(complete_exercise=completed_exercise)
        if grade_obj:
            grade_obj.update(grade=request.POST['grade'])
        else:
            new_grade_model = models.Grades.objects.create(complete_exercise=completed_exercise,
                                                       teacher=completed_exercise.teacher,
                                                       student=completed_exercise.student,
                                                       grade=request.POST['grade'], message=request.POST['message'])

        return redirect(reverse('completed', args=[ex_slug]))

    else:
        return redirect(reverse('completed', args=[ex_slug]))


@login_required()
def complete_exercise(request, ex_slug):
    if request.POST:

        exercise = get_object_or_404(models.Education_materials, slug=ex_slug)

        new_completed_ex = models.CompletedEx(message=request.POST['message'],
                                            education_material=exercise, student=request.user,
                                            teacher=exercise.author)
        if request.FILES:
            new_completed_ex.file = request.FILES['file']
        new_completed_ex.save()

        return redirect(reverse('exercise', args=[ex_slug]))

    else:

        return redirect('home')

class CompletedExercises(LoginRequiredMixin, TemplateView):
    template_name ='Study\\completed-exercises.html'
    slug_url_kwarg = 'ex_slug'


    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        object = get_object_or_404(models.Education_materials, slug=kwargs['ex_slug'])

        all_groups = StudentGroup.objects.all()

        context['title'] = object.title
        context['object'] = object
        context['groups'] = create_comletedEx_dict(all_groups)

        return context


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")
