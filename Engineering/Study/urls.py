from django.urls import path
from . import views

urlpatterns = [
    # path('', views.MainPage.as_view(), name='home'),
    path('', views.index, name='home'),
    path('exercise/<slug:ex_slug>/', views.ShowExercise.as_view(), name='exercise'),
    path('new_exercise/<slug:module_slug>', views.NewExercise.as_view(), name='new_exercise'),
]
