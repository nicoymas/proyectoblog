
from django.urls import path

from apppost.urls import *
from apppost.views import *
from appblog.views import *

from appblog import views
from django.contrib.auth.views import LogoutView

#imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("accounts/login/" , views.login_request , name="login"),
    path("", views.inicio, name='inicio' ),
    
    path("accounts/signup", views.register ,name= "register"),
    path("accounts/logout",LogoutView.as_view (template_name="appblog/logout.html"), name= "logout"),
    path("cargar_imagen/",cargar_imagen, name="cargarimagen"),
    
    path("accounts/profile/", actualizar_usuario ,name="Editarusuario"),
    
    path("about/" , views.sobre_mi , name = "sobremi"),

    
 
     
]
urlpatterns+= static( settings.MEDIA_URL ,document_root= settings.MEDIA_ROOT)






