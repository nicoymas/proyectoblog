
from django.db import models

class Reseta (models.Model):
    
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=40)
    queso=models.CharField(max_length=40)
    condimentos=models.CharField(max_length=20)
    relleno= models.CharField(max_length=40)
    salsa= models.CharField(max_length=40)
    carne=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.nombre}"
    


class Users_login (models.Model):
    
    nombre=models.CharField(max_length=40)
    email=models.EmailField(primary_key=True)
    def __str__(self):
        return f"{self.nombre} / {self.email}"
    


class Post (models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=40)
    conten_post=models.TextField()
    autor=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.titulo} / {self.autor}"

    


