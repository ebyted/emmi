# agenda/urls.py o backend/urls.py si lo tienes todo ahí
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('brow-design/', views.barrasa, name='brow_design'),
    path('wellness/', views.beauty, name='wellness'),
    path('gracias/', views.gracias, name='gracias'),
    path('agendas/', views.lista_agendas, name='agendas'),
    path('citas/', views.lista_citas, name='lista_citas'),
]