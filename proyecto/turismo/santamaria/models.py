from email import message_from_binary_file
from random import choices
from re import sub
from django.db import models

# Create yoclass Cliente(models.Model):
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    telefono=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="cliente", null=True)
    

def __str__(self): 
        return self.nombre
    
class Subcategoria(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="nombre subcategoria")
    
class Categoria(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="nombre categoria")

    def __str__(self):
        return self.nombre    
    
class Proveedor(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)
    subcategoria=models.ForeignKey(Subcategoria, null=True, on_delete=models.CASCADE) 
    correo=models.EmailField(max_length=100)
    ciudad=models.CharField(max_length=50)
    telefono=models.CharField(max_length=15)
    imagen = models.ImageField(upload_to="proveedor", null=True)
    

    def __str__(self):
        return self .nombre
    
opciones_consultas=[
    [0,"reserva"],
    [1, "consulta"],
    [2, "reclamo"],
    [3, "sugerencia"]
]
    
    
    
class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    tipo_consulta=models.IntegerField(choices=opciones_consultas)
    message = models.TextField()
    avisos =models.BooleanField()     
    
    def __str__(self):
        return self.nombre
        