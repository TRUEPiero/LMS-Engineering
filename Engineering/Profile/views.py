from typing import Any
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ShowProfile(LoginRequiredMixin, TemplateView):
    template_name = 'Profile\\index.html'


    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        return context
