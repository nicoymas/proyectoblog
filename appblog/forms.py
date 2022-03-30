from django import forms

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
    #email=forms.EmailField(max_length=40)    