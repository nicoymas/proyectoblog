from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post (models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=40)
    subtitulo=models.CharField(max_length=40)
    imagen=models.ImageField(upload_to='post', null=True, blank=True)
    conten_post=RichTextField(blank=True, null=True)
    autor=models.CharField(max_length=40)
    fecha=models.DateTimeField(auto_now_add=True ,null=True)

    def __str__(self):
        return f"{self.titulo} / {self.autor}"


class Imagenpost(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='post', null=True, blank=True)