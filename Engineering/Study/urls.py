from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
    path('exercise/<slug:ex_slug>/', views.ShowExercise.as_view(), name='exercise'),
    path('new_exercise/<slug:module_slug>', views.NewExercise.as_view(), name='new_exercise'),
    path('delete_exercise/<slug:ex_slug>', views.DeleteExercise.as_view(), name='delete_ex'),
    path('update_exercise/<slug:ex_slug>', views.UpdateExercise.as_view(), name='update_ex'),
    path('new_completed/<slug:ex_slug>', views.complete_exercise, name='new_completed'),
    path('completed/<slug:ex_slug>', views.CompletedExercises.as_view(), name='completed'),

]
