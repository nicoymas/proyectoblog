
# Create your views here.

from django.shortcuts import  render


#forms

from apppost.formsp import *

from apppost.models import *

#log
from django.contrib.auth.mixins import LoginRequiredMixin


#vistas basadas en clases
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class Postlista( ListView):#model y template_mane siempre deben llamarse asi
    model= Post
    template_name="apppost/class_post.html"

#DetailView: nos permite ver detalles de un solo objeto  
class Post_detalle(LoginRequiredMixin,DetailView):
    model= Post
    template_name= "apppost/class_postdetail.html"  
    
class Crear_Post(LoginRequiredMixin,CreateView):
    model=Post
    success_url="/post/post/routepages/" 
    fields=["titulo","subtitulo","imagen","conten_post","autor"] 

class Update_post(LoginRequiredMixin,UpdateView):
    model=Post
    success_url= "/post/post/routepages/"
    fields=["titulo","subtitulo","imagen","conten_post","autor"]

class Borrar_post(LoginRequiredMixin,DeleteView):
    model=Post
    success_url= "/post/post/routepages/"





def imagen_post(request):
    vista=Imagenpost.objects.filter(post=request.post)
    if len(vista) > 0 :
        imagen=vista [0].imagen.url

    context={"imagen_url":imagen}
    return render(request ,"apppost/class_postdetail.html", context)









