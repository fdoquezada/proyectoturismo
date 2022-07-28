from django.contrib import admin
from .models import Cliente, Subcategoria, Categoria, Proveedor, Contacto

class ClienteAdmin(admin.ModelAdmin):
    list_display =["nombre","apellido","telefono"]
    list_editable =["telefono"]
    search_fields =["nombre"]
    list_per_page:5
     

# Register your models here.

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Subcategoria)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Contacto)



