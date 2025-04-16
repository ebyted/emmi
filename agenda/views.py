from django.shortcuts import render, redirect
from .forms import AgendaForm
from .models import Agenda

def index(request):
    return procesar_formulario(request, 'index.html')

def barrasa(request):
    return procesar_formulario(request, 'barrasa.html')

def beauty(request):
    return procesar_formulario(request, 'beauty.html')

def procesar_formulario(request, template):
    initial_data = {}
    servicio_preseleccionado = request.GET.get('servicio')
    if servicio_preseleccionado:
        initial_data['servicio'] = servicio_preseleccionado

    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')
    else:
        form = AgendaForm(initial=initial_data)

    return render(request, template, {'form': form})

def lista_agendas(request):
    agendas = Agenda.objects.all().order_by('-fecha_creacion')
    return render(request, 'agenda_list.html', {'agendas': agendas})

def lista_citas(request):
    citas = Agenda.objects.all().order_by('-fecha_creacion')
    return render(request, 'lista_citas.html', {'citas': citas})

def gracias(request):
    return render(request, 'gracias.html')