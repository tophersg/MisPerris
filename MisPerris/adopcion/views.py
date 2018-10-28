from django.shortcuts import render

# Create your views here.
def adopcion_lista(request):
    return render(request,'adopcion/adopcion_lista.html')