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
