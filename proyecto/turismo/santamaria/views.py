import re
from django.shortcuts import redirect, render 
from django.contrib import messages
from .forms import ContactoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
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


def registro(request):
    data= {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)  
            messages.success(request, "Felicidades tu registro fue exitoso")  
            return redirect(to="home")
        data["form"]= formulario    
    return render(request, 'registration/registro.html', data)

