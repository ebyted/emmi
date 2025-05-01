from django.shortcuts import render, redirect
from .forms import AgendaForm
from collections import defaultdict
from .models import Agenda
<<<<<<< HEAD
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
=======
>>>>>>> development

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
<<<<<<< HEAD
                    cita.origen = 'brow_design'
                else:
                    cita.origen = 'wellness_therapies'
            else:
               #mapear el template a nuevos valores
                if template == 'barrasa.html':
                    cita.origen = 'brow_design'
                elif template == 'beauty.html':
                    cita.origen = 'wellness_therapies'
=======
                    cita.origen = 'barrasa'
                else:
                    cita.origen = 'beauty'
            else:
                cita.origen = template.split('.')[0]  # 'barrasa' o 'beauty'
>>>>>>> development

            cita.save()
            return redirect('gracias')
    else:
        form = AgendaForm(initial=initial_data)

    return render(request, template, {'form': form})

def lista_agendas(request):
    agendas = Agenda.objects.all().order_by('-fecha_creacion')
    return render(request, 'agenda_list.html', {'agendas': agendas})

<<<<<<< HEAD

@login_required
=======
>>>>>>> development
def lista_citas(request):
    agendas = Agenda.objects.all().order_by('-fecha_creacion')
    citas_por_origen = defaultdict(list)
    for cita in agendas:
<<<<<<< HEAD
        origen = (cita.origen or 'index').strip()
        citas_por_origen[origen].append(cita)

    return render(request, 'lista_citas.html', {
    'citas_por_origen': dict(citas_por_origen)
})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('lista_citas')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')

def gracias(request):
    return render(request, 'gracias.html')

@require_POST
def eliminar_cita(request, cita_id):
    Agenda.objects.filter(id=cita_id).delete()
    return redirect('lista_citas')
=======
        origen = cita.origen or 'index'
        citas_por_origen[origen].append(cita)
    return render(request, 'lista_citas.html', {'citas_por_origen': citas_por_origen})

def gracias(request):
    return render(request, 'gracias.html')
>>>>>>> development
