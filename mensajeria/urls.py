from django.urls import path


from mensajeria.views import *

from mensajeria import views

urlpatterns = [
    path('',views.Crear_mensaje.as_view(), name='mensajeria'),
    path('lista/',views.mensaje_lista.as_view() , name='mensaje_lista'),
    path('detalles/<pk>',views.mensaje_detalle.as_view() , name='mensaje_detalles'),




]