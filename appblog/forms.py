from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class post (forms.Form):
    
    titulo=forms.CharField(max_length=40)
    conten_post=forms.CharField(max_length=5000)
    autor= forms.CharField(max_length=40)


class resetario (forms.Form):
    
    nombre=forms.CharField(max_length=40)
    queso=forms.CharField(max_length=40)
    condimentos=forms.CharField(max_length=20)
    relleno= forms.CharField(max_length=40)
    salsa= forms.CharField(max_length=40)
    carne=forms.CharField(max_length=40)    


class Users (forms.Form):
    
    nombre=forms.CharField(max_length=40)
        

class registrousuario (UserCreationForm): #todo esto tiene que ser tal cual porque sino no lo toma
    email= forms.EmailField()
    password1=forms.CharField( label="contraseña" , widget= forms.PasswordInput)
    password2=forms.CharField( label="repetir contraseña" , widget= forms.PasswordInput)
    class Meta:
        model= User #este models fue importado de django
        fields= ["username" , "email", "password1", "password2"]
        help_text= {k:"" for k in fields}#este campo es opcional para quitar los mensajes
