from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Registro
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/Main.html', {'posts': posts})



def home(request):
    return render(request,'Main.html')


def Registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect('perris:home')
    else:
        form = UserCreationForm()
    return render(request,'blog/Registro.html',{'form':form})






