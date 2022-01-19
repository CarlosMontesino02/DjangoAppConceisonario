from django.shortcuts import render
from django.views.generic import ListView
from concesionario_app.models import Coche, Concesionario, Concesionario, Perfil, Carrito

class ofertadecoches(ListView):
    model = Coche

class concesionarios(ListView):
    model = Concesionario

class carritos(ListView):
    model = Carrito

class perfiles(ListView):
    model = Perfil
# Create your views here.

def index (request):
    return render(request, 'concesionario_app/index.html')
