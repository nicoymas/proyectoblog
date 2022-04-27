
from django.urls import path


from apppost.views import *

from apppost import views


#imagenes
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    #path("update_post/<titulo_id>/", views.editar_post , name="editar"),
    #path("eliminarpost/<elim>/",views.eliminarpost, name="eliminarpost"),
    #path("post/", views.post_blog , name="post"),
    #path("buscar_post/", views.buscar_post, name= 'post_creados'),
    
    #class basadas en vistas crud
    
    
    path("post/routepages/",views.Postlista.as_view(),name='post_lista'),
    path("post/nuevo/",views.Crear_Post.as_view(),name="create"),
    path("post/pages/<pk>",views.Post_detalle.as_view(),name="detalle"),
    path("post/editar/<pk>/",views.Update_post.as_view() ,name="editar"),
    path("post/borrar/<pk>/",views.Borrar_post.as_view(),name="borrar"),

    ]

urlpatterns+= static( settings.MEDIA_URL ,document_root= settings.MEDIA_ROOT)