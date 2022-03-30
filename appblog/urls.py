
from django.urls import path

from appblog.views import *

from appblog import views
urlpatterns = [
    
    path("", views.inicio, name='inicio' ),
    path("reseta/", views.reseta, name= 'reseta'),
    path("post/", views.post_blog , name="post"),
    path("formulario_login/",views.formulario_login, name="login_user"),
    path("buscar_reseta/", views.lasresetas, name= 'resetas-cargadas'),
    path("buscar_usuarios/", views.buscar_usuarios, name= 'buscar_usuarios'),
    #path("result_busqueda/" ,views.busqueda),
    path("buscar_post/", views.buscar_post, name= 'post_creados'),
    path("eliminarpost/<elim>/",views.eliminarpost, name="eliminarpost"),

]



