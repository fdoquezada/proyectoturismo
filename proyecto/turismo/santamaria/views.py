import re
from django.shortcuts import render 
from .forms import ContactoForm

# Create your views here.
def home(request):
    return render(request, 'santamaria/home.html')

def contacto(request):
    data = {
        'form' : ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Contacto enviado"
        else:
            data["form"]=formulario
        
        
    return render(request, 'santamaria/contacto.html', data)

def galeria(request):
    return render(request, 'santamaria/galeria.html')

