from django.shortcuts import render
from .forms import PostulantesForm
from django.shortcuts import redirect


def post_list(request):
    
    return render(request, 'blog/Main.html')

def home(request):
    return render(request,'Main.html')

def administrador(request):
    return render(request,'blog/Base_registro.html')


def postulante_nuevo(request):
    if request.method == "POST":
        form = PostulantesForm(request.POST)
        if form.is_valid():
            Postulantes = form.save(commit=False)
            Postulantes.author = request.user
            Postulantes.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form = PostulantesForm()
    return render(request, 'blog/Nuevo_formulario.html', {'form': form})

def postulante_editar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostulantesForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('Nuevo_formulario', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/Nuevo_formulario.html', {'form': form})