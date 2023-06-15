from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms, models
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
  


# Create your views here.
def index(request):
    return render(request, "productos/index.html")

class ProductoList(ListView):
    model = models.Producto    
    template_name = "productos/productos_list.html"  
    
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Producto.objects.all()
        return object_list
    
class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    template_name = "productos/productos_form.html"
    success_url = reverse_lazy("productos:productos_list")
    
class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    template_name= "productos/productos_form.html"
    success_url= reverse_lazy("productos:productos_list")
    
    
class ProductoDelete(DeleteView):
    model = models.Producto
    template_name= "productos/productos_confirm_delete.html"
    success_url= reverse_lazy("productos:productos_list")
    
class ProductoDetail(DetailView):
    model = models.Producto
    template_name="productos/productos_detail.html"
    
    

    
    