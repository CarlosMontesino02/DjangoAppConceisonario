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
from concesionario_app.views import carritos, ofertadecoches, index, perfiles, concesionarios
from concesionario_app.views import carritos_detalles, ofertadecoches_detalles, index, perfiles_detalles
from concesionario_app.views import concesionarios_detalles, cochecreateview, registro, cocheUpdateView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from concesionario_app.views import AuthorCreateView, AuthorDeleteView, AuthorUpdateView

urlpatterns = [
    path('perfil/add',registro.as_view(), name="regsitro"),
    path('coches/add',cochecreateview.as_view(), name="coches-add"),
    path('coches/<int:pk>/update', cocheUpdateView.as_view(), name='coche-update'),
    path('admin/', admin.site.urls),
    path('coches/', ofertadecoches.as_view(), name="coches"),
    path('', index),
    path('concesionarios/', concesionarios.as_view(), name="concesionarios"),
    path('carritos/', carritos.as_view(), name="carrito"),
    path('perfiles/', perfiles.as_view(), name="perfiles"),
    path('concesionarios_detalles/', concesionarios_detalles.as_view(), name="concesionarios_detalles"),
    path('carritos_detalles/', carritos_detalles.as_view(), name="carrito_detalles"),
    path('perfiles_detalles/', perfiles_detalles.as_view(), name="perfiles_detalles"),
    #path('coches_detalles/', ofertadecoches_detalles.as_view(), name="coches_detalles"),
    path('coches/<int:pk>/', ofertadecoches_detalles.as_view(), name='coches_detalles'),

    path('author/', perfiles.as_view(), name="author"),
    path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
