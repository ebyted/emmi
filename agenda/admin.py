from django.contrib import admin
from .models import Agenda

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'servicio', 'fecha_creacion')
    list_filter = ('servicio', 'fecha_creacion')  # para filtrar por servicio en el admin
    search_fields = ('nombre', 'email', 'servicio')