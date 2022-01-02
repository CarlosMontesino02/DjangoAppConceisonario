from django.shortcuts import render
from django.views.generic import ListView
from concesionario_app.models import Coche, Concesionario, Concesionario, Usuario, Carrito

class ofertadecoches(ListView):
    model = Coche

class concesionarios(ListView):
    model = Concesionario

# Create your views here.
