from django import forms
from concesionario_app.models import Perfil

class PerfilForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('DNI', 'NumTlf', 'Direccion', 'fechanac')
