from django.contrib import admin
from . import models


# Register your models here.

#@admin.register(models.Proveedor)
#class ProveedorAdmin(admin.ModelAdmin):
#    list_display = ("nombre",)
#    list_filter = ("nombre",)
#    search_fields = ("nombre",)
#    ordering = ("nombre",)

@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "precio",
        )
    

    
