from django.http import HttpResponse
from django.shortcuts import render
from .models import Perritos
from .forms import RescatesForm
from django.shortcuts import redirect

def adopcion_lista(request):
    adopciones = Perritos.objects.all().order_by('fecha_publicacion');
    return render(request, 'adopcion/adopcion_lista.html', { 'adopciones': adopciones })

def adopcion_detalles(request, titulo):
    # return HttpResponse(titulo)
    adopcion = Perritos.objects.get(titulo=titulo)
    return render(request, 'adopcion/adopcion_detalles.html', { 'adopcion': adopcion })

def rescate_nuevo(request):
    if request.method == "POST":
        formp = RescatesForm(request.POST)
        if formp.is_valid():
            Perritos = formp.save(commit=False)
            Perritos.author = request.user
            Perritos.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        formp = RescatesForm()
    return render(request, 'adopcion/rescate_nuevo.html', {'formp': formp})

def rescate_editar(request, pk):
    adopcion = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = RescatesForm(request.POST, instance=post)
        if form.is_valid():
            adopcion = form.save(commit=False)
            adopcion.author = request.user
            adopcion.save()
            return redirect('Nuevo_formulario', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/Nuevo_formulario.html', {'form': form})    