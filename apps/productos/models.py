from django.db import models

# Create your models here.
#class Proveedor(models.Model):
#    nombre=models.CharField(max_length=50,unique=True, blank=True)
#    email= models.EmailField()
#    telefono=models.IntegerField()
#    
#    class Meta:
#        verbose_name="Proveedor"
#        verbose_name_plural="Proveedores"
#    def __str__(self):
#        return self.nombre

class Producto(models.Model):
  nombre=models.CharField(max_length=50, unique=True, blank=True)
  precio=models.IntegerField() 
  def __str__(self):
      return f"{self.nombre}           _______          proveedor: {self.precio}"
    