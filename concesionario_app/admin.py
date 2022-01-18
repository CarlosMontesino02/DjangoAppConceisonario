from django.contrib import admin
from .models import Usuario
from .models import Concesionario
from .models import Coche
from .models import Carrito
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from concesionario_app.models import Usuario

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# Define a new User admin
# Re-register UserAdmin
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Concesionario)
admin.site.register(Coche)
admin.site.register(Carrito)
