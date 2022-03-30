
from django.http import HttpResponse
from django.shortcuts import render

from appblog.models import *
from appblog.forms import *



def inicio(request):
    return render(request, "appblog/index.html") 


def reseta (request):
    
    if request.method =="POST":
        
        mireseta= resetario(request.POST)
       
        print(resetario)

        if mireseta.is_valid():
            
            contenido= mireseta.cleaned_data
            
            lareseta= Reseta(nombre=contenido["nombre"] , queso=contenido["queso"], relleno=contenido["relleno"] , salsa=contenido["salsa"] , carne=contenido["carne"])        
            lareseta.save()

            return render(request ,"appblog/reseta.html")    

    else :
        tabla= Reseta.objects.all()
        
        mireseta= resetario()
    
    return render(request,"appblog/reseta.html", {"reseton":mireseta , "tabla": tabla})
    

    

def formulario_login (request):
    lista_user= Users_login.objects.all()

    if request.method == "POST":
        user= Users_login(request.POST["nombre"] , request.POST ["email"])
        user.save()
        return render (request, "appblog/formulario_login.html",{"listado":lista_user})

    
    return render (request, "appblog/formulario_login.html",{"listado":lista_user})  
    


def buscar_usuarios (request): 
    usuario= request.GET.get('user', "")
    error = ""

    if usuario:
        try:  
            nombre = Users_login.objects.get(nombre=usuario)
            return render(request, 'appblog/buscar_usuarios.html', {"nombre": nombre, "id": usuario})

        except Exception as exc:
            print(exc)
            error = "no tenemos nada relacionado a esos datos"
            return render(request, 'appblog/buscar_usuarios.html' , {"error": error})

    return render(request, 'appblog/buscar_usuarios.html' , {"error": error})






def post_blog (request):
    list_post=Post.objects.all()

    if request.method =="POST":
        
        posteos= post(request.POST)
       
        print(posteos)

        if posteos.is_valid():
            
            contenido= posteos.cleaned_data
            
            mipost= Post(titulo=contenido["titulo"], conten_post=contenido["conten_post"], autor=contenido["autor"])
            
            mipost.save()

            return render(request ,"appblog/index.html")    

    else :
        posteos= post()
    
    return render(request,"appblog/post_blog.html", {"formulario":posteos,"lista":list_post})      


def eliminarpost(request,elim):
    try:
        posts=Post.objects.get(titulo=elim)
        posts.delete()
        return render(request,"appblog/post_blog.html")
    
    except Exception as exc:
        return render(request,"appblog/post_blog.html")




def buscar_post (request):
    pass

def lasresetas (request):
    pass


















