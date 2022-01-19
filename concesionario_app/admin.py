from django.contrib import admin
from .models import Perfil
from .models import Concesionario
from .models import Coche
from .models import Carrito
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from concesionario_app.models import Perfil
admin.site.register(Perfil)
admin.site.register(Concesionario)
admin.site.register(Coche)
admin.site.register(Carrito)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfil'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
