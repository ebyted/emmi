from django.shortcuts import render, redirect
from .forms import AgendaForm
from collections import defaultdict
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
            cita = form.save(commit=False)

            # Lógica para asignar origen desde la página principal (index.html)
            if template == 'index.html':
                servicio = cita.servicio.lower()
                if any(palabra in servicio for palabra in ['ceja', 'brow', 'microblading']):
                    cita.origen = 'barrasa'
                else:
                    cita.origen = 'beauty'
            else:
                cita.origen = template.split('.')[0]  # 'barrasa' o 'beauty'

            cita.save()
            return redirect('gracias')
    else:
        form = AgendaForm(initial=initial_data)

    return render(request, template, {'form': form})

def lista_agendas(request):
    agendas = Agenda.objects.all().order_by('-fecha_creacion')
    return render(request, 'agenda_list.html', {'agendas': agendas})

def lista_citas(request):
    agendas = Agenda.objects.all().order_by('-fecha_creacion')
    citas_por_origen = defaultdict(list)
    for cita in agendas:
        origen = cita.origen or 'index'
        citas_por_origen[origen].append(cita)
    return render(request, 'lista_citas.html', {'citas_por_origen': citas_por_origen})

def gracias(request):
    return render(request, 'gracias.html')