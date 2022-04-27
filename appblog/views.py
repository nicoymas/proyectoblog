

from django.shortcuts import redirect, render
from django.contrib.auth import login ,logout , authenticate

#forms
from django.contrib.auth.forms import AuthenticationForm
from appblog.forms import *

from appblog.models import *

#log

from django.contrib.auth.decorators import login_required



def sobre_mi(request):
    return render(request ,"appblog/sobremi.html")

def login_request(request):
    if request.method == "POST":
        formulario=AuthenticationForm(request, data= request.POST) 
        if formulario.is_valid():
            data=formulario.cleaned_data
            nombre_user=data.get('username') 
            contraseña= data.get('password')

            usuario= authenticate( username=nombre_user, password=contraseña) 
            
            if usuario is not None: 
                
                login(request, usuario) 
                 
                contexto={"user":usuario}
                
                return redirect("inicio")
            else: 
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
        form= registrousuario(request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            print(usuario)
            form.save()
            
            return render(request, "appblog/index.html")
            
        else:
            context={"errors": ["no paso validaciones"]}
            return render(request ,"appblog/index.html", context)
    else:
        form = registrousuario()
        return render (request , "appblog/register.html" ,{"form": form})

 
def inicio(request):
    
    if request.user.username:
        avatar = Avatar.objects.filter(usuario=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        else:
            imagen = None
            
           
    else:
        imagen = None
    dict_ctx = {"title": "Inicio", "page": "Inicio", "imagen_url": imagen}
    return render(request, "appblog/index.html", dict_ctx)
    
    

@ login_required()
def cargar_imagen(request):

    if request.method == "POST":
        formulario= AvatarFormulario(request.POST,request.FILES)

        if formulario.is_valid():
            usuario1= request.user
            avatar= Avatar.objects.filter(usuario=usuario1)

            if len(avatar) > 0:
                avatar= avatar[0]
                avatar.imagen= formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(usuario=usuario1, imagen=formulario.cleaned_data["imagen"])
                avatar.save()
            
        return redirect("inicio")
    else:

        formulario = AvatarFormulario()
        return render(request, "appblog/cargar_imagen.html", {"form": formulario})



    

@login_required()
def actualizar_usuario(request):
    return render(request, "appblog/editar_usuario.html")





@login_required()
def actualizar_usuario(request):
    
    usuario= request.user

    if request.method == "POST":
        formulario= UsuarioEditForm(request.POST) 

        if formulario.is_valid():
            
            data= formulario.cleaned_data

            usuario.email= data["email"]
            usuario.password1= data["password1"]
            usuario.password2= data["password2"]
            usuario.first_name= data["first_name"]
            usuario.last_name= data["last_name"]
           

            usuario.save()

            return redirect("inicio")
        
        else:
            formulario= UsuarioEditForm(initial={"email": usuario.email, "first_name": usuario.first_name ,"last_name": usuario.last_name})  
            return render(request,  "appblog/editar_usuario.html", {"form": formulario, "errors": ["Datos o formato invalidos"]})

    else:
        formulario= UsuarioEditForm(initial={"email": usuario.email, "first_name": usuario.first_name ,"last_name": usuario.last_name})  
        return render(request,  "appblog/editar_usuario.html", {"form": formulario})






