import os
from django.conf import settings
from django.shortcuts import render

def galeria_view(request):
    galeria_path = os.path.join(settings.MEDIA_ROOT, 'Galeria')
    imagenes = []

    if os.path.exists(galeria_path):
        for archivo in os.listdir(galeria_path):
            if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                imagenes.append(f'{settings.MEDIA_URL}Galeria/{archivo}')

    return render(request, 'indexgaleria.html', {'imagenes': imagenes})

def galeria_nosotros_view(request):
    nosotros_path = os.path.join(settings.MEDIA_ROOT, 'Nosotros')
    imagenes_nosotros = []

    if os.path.exists(nosotros_path):
        for archivo in sorted(os.listdir(nosotros_path)):
            if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                imagenes_nosotros.append(f'{settings.MEDIA_URL}Nosotros/{archivo}')

    return render(request, 'barassa.html', {'imagenes_nosotros': imagenes_nosotros})
