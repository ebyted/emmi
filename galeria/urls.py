from django.urls import path
from .views import galeria_view

urlpatterns = [
    path('', galeria_view, name='galeria'),
]