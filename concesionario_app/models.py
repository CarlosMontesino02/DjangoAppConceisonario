from django.db import models

class Usuario(models.Model):
    DNI = models.CharField(max_length=9)
    NumTlf = models.IntegerField()
    Direccion = models.CharField(max_length=50)
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
    Stock = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    upload = models.ImageField(upload_to ='uploads/')
    descripcion  = models.CharField(max_length=300)
    def __str__(self):
        return self.Modelo

class Carrito(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Pedido = models.ManyToManyField(Coche)
    def __str__(self):
        return str(self.Usuario)
# Create your models here.
