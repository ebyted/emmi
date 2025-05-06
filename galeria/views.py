from django.shortcuts import render


def galeria_view(request):
    return render(request, 'galeria/indexgaleria.html')  # debes crear este template
