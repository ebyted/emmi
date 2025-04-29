from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('brow-design/', views.barrasa, name='brow_design'),
    path('wellness/', views.beauty, name='wellness'),
    path('gracias/', views.gracias, name='gracias'),
    path('agendas/', views.lista_agendas, name='agendas'),
    path('citas/', views.lista_citas, name='lista_citas'),
    path('eliminar-cita/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),
]