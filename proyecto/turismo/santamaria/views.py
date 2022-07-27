from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'santamaria/home.html')

def contacto(request):
    return render(request, 'santamaria/contacto.html')

def galeria(request):
    return render(request, 'santamaria/galeria.html')

