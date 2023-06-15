
from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path("", views.index, name="index"),
    
    
]

urlpatterns += [
    path("productos/list/", views.ProductoList.as_view(), name = "productos_list"),
    path("productos/create/", staff_member_required(views.ProductoCreate.as_view()), name = "productos_create"),
    path("productos/update/<int:pk>/", staff_member_required(views.ProductoUpdate.as_view()), name = "productos_update"),
    path("productos/delete/<int:pk>/", staff_member_required(views.ProductoDelete.as_view()), name = "productos_delete"),
    path("productos/detail/<int:pk>/", views.ProductoDetail.as_view(), name = "productos_detail"),
]