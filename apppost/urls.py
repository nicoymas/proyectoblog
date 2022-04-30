
from django.urls import path


from apppost.views import *

from apppost import views


#imagenes
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    
    
    
    path("pages/",views.Postlista.as_view(),name='post_lista'),
    path("nuevo/",views.Crear_Post.as_view(),name="create"),
    path("pages/<pk>",views.Post_detalle.as_view(),name="detalle"),
    path("editar/<pk>/",views.Update_post.as_view() ,name="editar"),
    path("borrar/<pk>/",views.Borrar_post.as_view(),name="borrar"),

    ]

urlpatterns+= static( settings.MEDIA_URL ,document_root= settings.MEDIA_ROOT)