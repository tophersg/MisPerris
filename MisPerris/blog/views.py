from django.shortcuts import render



def post_list(request):
    
    return render(request, 'blog/Main.html')

def home(request):
    return render(request,'Main.html')


def usuario(request):
    return render(request,'MainUsuario.html')    