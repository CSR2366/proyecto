#from django.contrib.auth.views import LoginView, LogoutView
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
#importar include
#from django.urls import include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("productos/", views.productos, name="productos"),
    path("envios/", views.envios, name="envios"),
    
] 
#+ staticfiles_urlpatterns()
    
    #path("login/", LoginView.as_view(template_name="home/login.html"), name="login"),
    #path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    #path("register/", views.register, name="register"),
    #