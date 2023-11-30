from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
TALLA=(
    ('s','S'),
    ('m','M'),
    ('l','L'),
    ('x','X'),
    ('xl','XL'),
    ('xxl','XXL')

)
TIPO_ROPA=(
    ('nueva','NUEVA'),
    ('usada','USADA')
)


class Ropa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    rut = models.CharField(max_length=10)
    talla = models.CharField(max_length=3,choices=TALLA,default='s')
    tipo = models.CharField(max_length=5,choices=TIPO_ROPA,default='nueva')
    
    def __str__(self):
        return self.id+" - "+self.nombre

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, default="EN PREPARACION")
    
    def __str__(self):
        return str(self.id)+" "+str(self.fecha)

class Historial(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.ForeignKey(to=Estado, on_delete=models.CASCADE)
    tipo = models.ForeignKey(to=Ropa, on_delete=models.CASCADE) 
    
    
    def __str__(self):
        return str(self.id)+" "+self.producto.codigo



    
