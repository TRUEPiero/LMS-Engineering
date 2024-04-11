from typing import Any
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from . import models, forms
from django.views import View
from django.views.generic import TemplateView, DetailView, FormView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

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

class MainPage(LoginRequiredMixin,TemplateView):

    template_name='Study/index.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        all_sections = models.Sections_of_modules.objects.all()

        dict_sections = {}

        for section in all_sections:
            dict_sections[section] = []
            modules = models.Modules_of_education_materials.objects.filter(section=section)
            for fmodule in modules:
                dict_module = {}
                dict_module[fmodule] = models.Education_materials.objects.filter(module=fmodule)
                dict_sections[section].append(dict_module)

        context['sections'] = dict_sections
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
        context['completed_ex'] = models.CompletedEx.objects.filter(student=self.request.user)
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


# class NewCompleted(CreateView):
#     form_class = forms.NewCompletedEx
#     slug_url_kwarg = 'ex_slug'
#     template_name = 'Study/completed_ex.html'
#     success_url = reverse_lazy('home')

def complete_exercise(request, ex_slug):
    if request.POST:
        exercise = get_object_or_404(models.Education_materials, slug=ex_slug)

        new_completed_ex = models.CompletedEx(message=request.POST['message'], education_material=exercise, student=request.user,file=None)
        if request.FILES:
            new_completed_ex.file = request.FILES['file']
        new_completed_ex.save()
        return redirect('home')
    else:
        return redirect('home')



def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")
