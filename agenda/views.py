from django.shortcuts import render, redirect, get_object_or_404
from .forms import AgendaForm
from collections import defaultdict
from .models import Agenda
from django.http import HttpResponse

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

            if template == 'index.html':
                servicio = cita.servicio.lower()
                if any(palabra in servicio for palabra in ['ceja', 'brow', 'microblading']):
                    cita.origen = 'Emmi Brow Design'
                else:
                    cita.origen = 'Emmi Wellness Therapies'
            elif template == 'barrasa.html':
                cita.origen = 'Emmi Brow Design'
            elif template == 'beauty.html':
                cita.origen = 'Emmi Wellness Therapies'

            cita.save()
            return redirect('gracias')
    else:
        form = AgendaForm(initial=initial_data)

    context = {'form': form}

    # ✅ Solo para barrasa.html, incluir galería de Nosotros
    if template == 'barrasa.html':
        nosotros_path = os.path.join(settings.MEDIA_ROOT, 'Nosotros')
        imagenes_nosotros = []
        if os.path.exists(nosotros_path):
            for archivo in os.listdir(nosotros_path):
                if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                    imagenes_nosotros.append(f'{settings.MEDIA_URL}Nosotros/{archivo}')
        context['imagenes_nosotros'] = imagenes_nosotros

    return render(request, template, context)

def lista_agendas(request):
    agendas = Agenda.objects.all().order_by('-fecha_creacion')
    return render(request, 'agenda_list.html', {'agendas': agendas})

def lista_citas(request):
    agendas = Agenda.objects.all().order_by('-fecha_creacion')
    citas_por_origen = defaultdict(list)
    for cita in agendas:
        citas_por_origen[cita.origen].append(cita)
    return render(request, 'lista_citas.html', {'citas_por_origen': dict(citas_por_origen)})

def gracias(request):
    return render(request, 'gracias.html')

def eliminar_cita(request, cita_id):
    cita = get_object_or_404(Agenda, id=cita_id)
    cita.delete()
    return redirect('lista_citas')

def galeria(request, galeria_id):
    # Aquí puedes implementar la lógica para mostrar la galería
    # Por ejemplo, podrías cargar imágenes desde un modelo o una carpeta específica
    return render(request, 'indexgaleria.html')