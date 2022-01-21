from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.urls import reverse

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DNI = models.CharField(max_length=9)
    NumTlf = models.IntegerField(null=True, blank=True)
    Direccion = models.CharField(max_length=50)
    fechanac = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.DNI

class Concesionario(models.Model):
    Ubicacion = models.CharField(max_length=60)
    TlfConce = models.IntegerField()
    Horario = models.CharField(max_length=50)
    def __str__(self):
        return self.Ubicacion

class Coche(models.Model):
    Concesionarioco = models.ForeignKey(Concesionario, on_delete=models.CASCADE)
    Marca = models.CharField(max_length=30)
    Modelo = models.CharField(max_length=30)
    Color = models.CharField(max_length=11)
    Extras = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    upload = models.ImageField(upload_to ='img/')
    descripcion  = models.CharField(max_length=300)
    def __str__(self):
        return self.Modelo

class Carrito(models.Model):
    Usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    Pedido = models.ManyToManyField(Coche)
    def __str__(self):
        return str(self.Usuario)

class Author(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})
# Create your models here.
