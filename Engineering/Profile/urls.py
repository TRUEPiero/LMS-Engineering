from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowProfile.as_view(), name='profile'),
    path('deletephoto/', views.delete_photo, name='delete_photo'),
    path('changephoto/', views.change_photo, name='change_photo'),
]
