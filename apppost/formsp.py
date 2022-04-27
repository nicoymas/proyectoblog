from django import forms
from ckeditor.fields import RichTextField

from apppost.models import Post


class post (forms.Form):
    
    titulo=forms.CharField(max_length=40)
    subtitulo=forms.CharField(max_length=40)
    imagen = forms.ImageField()
    conten_post =RichTextField() 
    autor=forms.CharField(max_length=40)

    class Meta:
        model = Post
        fields = ["titulo","subtitulo","imagen", "conten_post", "autor"]
        help_text = { k: "" for k in fields}
    

