
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login ,logout , authenticate
from django.contrib.auth.forms import AuthenticationForm
from appblog.models import *
from appblog.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def login_user(request):
    if request.method == "POST":
        formulario=AuthenticationForm(request, data= request.POST) #cargando datos al formulario
        if formulario.is_valid():#verificacion de data
            data=formulario.cleaned_data
            nombre_user=data.get("username") #este no puede ser cualquier nombre, ya viene con el formulario django
            contraseña= data.get("password")

            usuario= authenticate( username=nombre_user, password=contraseña) #para ver si esos datos estan en la BD
            
            if usuario is not None: #si realmente existe el usuario...
                
                login(request, usuario) #se llama a la funcion login con el usuario
                contexto={"user":usuario}
                return render(request , "appblog/index.html", contexto)
            else: #en el caso de que no funcione  no exista
                contex= {"errors":["el usuario no existe"]}
                return render (request, "appblog/index.html", contex)
        else:
            contex= {"errors":["revise los datos indicados"]}
            return render (request, "appblog/index.html", contex)

    else:
        form= AuthenticationForm()
        return render(request, "appblog/login.html",{"form":form})


def register(request):
    if request.method == "POST":
        form = registrousuario(request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            form.save()
            context={"page": usuario}
            return render(request, "appblog/index.html", context)

        else:
            context={"page": "anonimo" ,"error": ["no paso validaciones"]}
            return render(request ,"appblog/index.html", context)
    else:
        form = registrousuario()
        return render (request , "appblog/register.html" ,{"form": form})


def inicio(request):
    return render(request, "appblog/index.html") 


@ login_required
def reseta (request):
    
    if request.method =="POST":
        
        mireseta= resetario(request.POST)
       
        print(resetario)

        if mireseta.is_valid():
            
            contenido= mireseta.cleaned_data
            
            lareseta= Reseta(nombre=contenido["nombre"] , queso=contenido["queso"],condimentos=contenido["condimentos"], relleno=contenido["relleno"] , salsa=contenido["salsa"] , carne=contenido["carne"])        
            lareseta.save()
            tabla= Reseta.objects.all()
        
            mireseta= resetario()
 
            return render(request ,"appblog/reseta.html",{"reseton":mireseta , "tabla": tabla})    

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
    

@ login_required()
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

@ login_required
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

@ login_required()
def eliminarpost(request,elim):
    try:
        posts=Post.objects.get(titulo=elim)
        posts.delete()
        return render(request,"appblog/post_blog.html")
    
    except Exception as exc:
        return render(request,"appblog/post_blog.html")



@ login_required()
def buscar_post (request):
    pass


@ login_required()
def lasresetas (request):
    pass


















