from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Users (forms.Form):
    
    nombre=forms.CharField(max_length=40)
    email=forms.EmailField(max_length=40)
        


class registrousuario (UserCreationForm):
    email= forms.EmailField()
    password1=forms.CharField( label="contraseña" , widget= forms.PasswordInput)
    password2=forms.CharField( label="repetir contraseña" , widget= forms.PasswordInput)
  
    class Meta:
        
        model= User 
        fields = ['username', 'email', 'password1', 'password2']
       
        help_text= { k: "" for k in fields}

       
class UsuarioEditForm(UserCreationForm):

    email = forms.EmailField(label="Editar email")
    password1 = forms.CharField(label="Contrasenia 1", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contrasenia 2", widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=500,label="Nombre")
    last_name = forms.CharField(label="Apellido")
    

    class Meta:
        model = User
        fields = ["first_name", "last_name","email", "password1", "password2"]
        help_text = { k: "" for k in fields}


class AvatarFormulario(forms.Form):

    imagen = forms.ImageField()       




    