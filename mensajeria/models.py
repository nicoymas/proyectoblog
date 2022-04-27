from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class  mensajeria(models.Model):
    
    emisor=models.CharField(max_length=40)
    receptor=models.CharField(max_length=40)
    asunto=models.CharField(max_length=60)
    cuerpo=RichTextField(blank=True, null=True)
    fecha=models.DateTimeField(auto_now_add=True ,null=True)
    def __str__(self):
        return f"{self.asunto} / {self.emisor} / {self.receptor}"



