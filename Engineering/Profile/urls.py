from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowProfile.as_view(), name='profile'),
]
