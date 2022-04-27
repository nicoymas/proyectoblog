
from mensajeria.models import mensajeria
from django.views.generic import ListView

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class mensaje_lista( LoginRequiredMixin,ListView):
    model= mensajeria
    template_name="lista_mensajes.html"



class Crear_mensaje(LoginRequiredMixin,CreateView):
    model=mensajeria
    template_name="crear_mensaje.html"
    success_url="/"
    fields=["emisor","receptor","asunto","cuerpo"] 

class mensaje_detalle(LoginRequiredMixin,DetailView):
    model= mensajeria
    template_name= "detalle_mensaje.html"  

    


