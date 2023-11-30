from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Ropa


class Registro(UserCreationForm):
    nombre = forms.CharField(max_length=20, help_text="Ingrese su nombre")
    apellido = forms.CharField(max_length=20, help_text="Ingrese su apellido")
    email = forms.EmailField(max_length=64, help_text="Ingrese su correo electronico")
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','nombre', 'apellido', 'email', 'password1', 'password2')

class Ropa(ModelForm):
    nombre = forms.TextInput()
    email = forms.EmailField()
    rut = forms.TextInput()
    talla = forms.RadioSelect()
    tipo = forms.RadioSelect()
    class Meta:
        model = Ropa
        fields = ('nombre','email','rut','talla','tipo')
