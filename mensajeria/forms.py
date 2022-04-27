from django import forms

class Mensajes(forms.Form):
    emisor=forms.CharField(max_length=40)
    receptor=forms.CharField(max_length=40)
    asunto=forms.CharField(max_length=60)
    cuerpo=forms.CharField(max_length=5000)
    fecha=forms.DateField()

    def __str__(self):
        return f"{self.asunto} / {self.emisor} / {self.receptor}"

        
