from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('exercise/<slug:ex_slug>/', views.show_exercise, name='exercise'),
    path('new_exercise/<slug:module_slug>', views.new_exercise, name='new_exercise'),

    path('/', views.new_exercise_post, name='new_exercise_post')
]
