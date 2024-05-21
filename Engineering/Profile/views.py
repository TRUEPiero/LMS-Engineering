from typing import Any
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse


class ShowProfile(LoginRequiredMixin, TemplateView):
    template_name = 'Profile\\index.html'


    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        return context

# @login_required()
def delete_photo(request):
    request.user.photo = None
    request.user.save()
    return redirect(reverse('profile'))

@login_required()
def change_photo(request):

    request.user.photo = request.FILES['file']
    request.user.save()

    return redirect(reverse('profile'))
