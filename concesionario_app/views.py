from django.shortcuts import render
from django.views.generic import ListView
from concesionario_app.models import Coche, Concesionario, Concesionario, Perfil, Carrito
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from concesionario_app.models import Author
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from concesionario_app.forms import PerfilForm
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, redirect


class cochecreateview(CreateView):
    model = Coche
    fields = ['Concesionarioco','Marca','Modelo','Color','Extras','precio','upload','descripcion']
    success_url = reverse_lazy('coches')

class cocheUpdateView(UpdateView):
    model = Coche
    fields = ['Concesionarioco','Marca','Modelo','Color','Extras','precio','upload','descripcion']

class concesionariocreateview(CreateView):
    model = Concesionario
    fields = ['ubicacion','tlfconce','horario','map']
    success_url = reverse_lazy('concesionarios')

class concesionarioUpdateView(UpdateView):
    model = Concesionario
    fields = ['ubicacion','tlfconce','horario','map']

class registro(CreateView):
    model = Perfil
    fields=['user','DNI','NumTlf','Direccion','fechanac']
    success_url = reverse_lazy('perfiles')

class ofertadecoches(ListView):
    model = Coche

class ofertadecoches_detalles(DetailView):
    model = Coche

class concesionarios(ListView):
    model = Concesionario

class concesionarios_detalles(DetailView):
    model = Concesionario

class carritos(ListView):
    model = Carrito

class carritos_detalles(DetailView):
    model = Carrito

class perfiles(ListView):
    model = Perfil

class perfiles_detalles(DetailView):
    model = Perfil
# Create your views here.

def index (request):
    return render(request, 'concesionario_app/index.html')

#registro
def RegistroUsuario(request):
	if request.method == "POST":
		UForm = UserCreationForm(request.POST)
		PForm = PerfilForm(request.POST)
		if UForm.is_valid() and PForm.is_valid():
			Usuario = UForm.save(commit=False)
			Perfil = PForm.save(commit=False)
			Perfil.user = Usuario
			UForm.save()
			PForm.save()
			username = UForm.cleaned_data['username']
			password = UForm.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')
	else:
		UForm = UserCreationForm
		PForm = PerfilForm

	return render(request, 'registration/registro.html', {'UForm': UForm, 'PForm': PForm})
