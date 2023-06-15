from django import forms
from . import models


class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"
        
#class ProveedorForm(forms.ModelForm):
#    class Meta:
#        model = models.Proveedor
#        fields = "__all__"
#        widgets={
#            "nombre":forms.TextInput(attrs={"class":"form-control"}),
#        }