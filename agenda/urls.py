from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name = 'home'), 
    path('agenda/', views.agenda_form, name='agenda_form'),
]

