from django.shortcuts import render
from .forms import AgendaForm

def home(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'gracias.html')
        else:
            return render(request, 'index.html', {'form': form})
    else:
        form = AgendaForm()
        return render(request, 'index.html', {'form': form})

# ⬇️ Esta es la que falta probablemente:
def agenda_form(request):
    form = AgendaForm()
    return render(request, 'agenda/agenda_form.html', {'form': form})

def barrasa(request):
    return render(request, 'barrasa.html')