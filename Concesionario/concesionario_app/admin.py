from django.contrib import admin
from .models import Usuario
from .models import Concesionario
from .models import Coche
from .models import Carrito
admin.site.register(Usuario)
admin.site.register(Concesionario)
admin.site.register(Coche)
admin.site.register(Carrito)
# Register your models here.
