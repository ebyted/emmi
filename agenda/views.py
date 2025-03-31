from django.shortcuts import render, redirect
from .forms import AgendaForm

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