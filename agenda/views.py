from django.shortcuts import render, redirect
from .forms import AgendaForm
from .models import Agenda

def lista_agendas(request):
    agendas = Agenda.objects.all().order_by('-fecha_creacion')
    return render(request, 'agenda_list.html', {'agendas': agendas})

def lista_citas(request):
    citas = Agenda.objects.all().order_by('-fecha_creacion')
    return render(request, 'lista_citas.html', {'citas': citas})

def barrasa(request):
    return render(request, 'barrasa.html')

def beauty(request):
    return render(request, 'beauty.html')

def gracias(request):
    return render(request, 'gracias.html')

def index(request):
    initial_data = {}
    servicio_preseleccionado = request.GET.get('servicio')
    if servicio_preseleccionado:
        initial_data['servicio'] = servicio_preseleccionado
    
    form = AgendaForm(initial=initial_data)


    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')  # asegúrate que esta vista está definida en tus URLs
        
    

    return render(request, 'index.html', {'form': form})