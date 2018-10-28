from django.http import HttpResponse
from django.shortcuts import render
from .models import Perritos

def adopcion_lista(request):
    adopciones = Perritos.objects.all().order_by('fecha_publicacion');
    return render(request, 'adopcion/adopcion_lista.html', { 'adopciones': adopciones })
