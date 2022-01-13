"""Concesionario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from concesionario_app.views import carritos, ofertadecoches, index
from concesionario_app.views import concesionarios
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coches/', ofertadecoches.as_view(), name="coches"),
    path('', index),
    path('concesionarios/', concesionarios.as_view(), name="concesionarios"),
    path('carritos/', carritos.as_view(), name="carrito"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
