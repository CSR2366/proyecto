#from django.contrib.auth.views import LoginView, LogoutView
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
#importar include
#from django.urls import include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
] 
#+ staticfiles_urlpatterns()
    
    #path("login/", LoginView.as_view(template_name="home/login.html"), name="login"),
    #path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    #path("register/", views.register, name="register"),
    #path("about/", views.about, name="about"),