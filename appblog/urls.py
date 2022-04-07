
from django.urls import path
from django.contrib.auth.views import LogoutView

from appblog.views import *

from appblog import views



urlpatterns = [
    
    #path("", views.inicio, name='inicio' ),
    #path("login" ,views.login_user , name="login"),
    #path("logout" ,LogoutView.as_view (template_name="appblog/logout.html"), name="logout"),
    #path("register" ,views.register, name="register"),
    #
    #
    #path("reseta/", views.reseta, name= 'reseta'),
    #path("post/", views.post_blog , name="post"),
    #path("formulario_login/",views.formulario_login, name="login_user"),
    #path("buscar_reseta/", views.lasresetas, name= 'resetas-cargadas'),
    #path("buscar_usuarios/", views.buscar_usuarios, name= 'buscar_usuarios'),
    #path("buscar_post/", views.buscar_post, name= 'post_creados'),
    #path("eliminarpost/<elim>/",views.eliminarpost, name="eliminarpost"),
    
    path("", views.inicio, name='inicio' ),
    
    
    #Todo POST
    path("update_post/<titulo_id>/", views.editar_post , name="editar"),
    path("eliminarpost/<elim>/",views.eliminarpost, name="eliminarpost"),
    path("post/", views.post_blog , name="post"),
    path("buscar_post/", views.buscar_post, name= 'post_creados'),
    
    
    #Resetas
    path("reseta/", views.reseta, name= 'reseta'),
    path("buscar_reseta/", views.lasresetas, name= 'resetas-cargadas'),
   
    #Usuarios
    path("formulario_login/",views.formulario_login, name="login_user"),
    path("buscar_usuarios/", views.buscar_usuarios, name= 'buscar_usuarios'),
    
    
    path("login" ,views.login_user , name="login"),

    #urls basadas en clases
    path("usuario/lista/",views.Userlista.as_view(),name='usuario_lista'),
    
    
    path("editar/<pk>/",views.Update_user.as_view(),name="editar"),
    path("borrar/<pk>/",views.Borrar_user.as_view(),name="borrar"),
    path("<pk>/",views.Usuario_detalle.as_view(),name="detalle"),
    path("nuevo/",views.Crear_usuario.as_view(),name="create"),
]



