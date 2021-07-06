"""proyectoWeb URL Configuration

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
import rest_mascota
from rest_mascota.views import lista_mascotas
from django.contrib import admin
from django.contrib.admin.sites import site
from django.urls import path
from django.urls import include

import appWeb.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appWeb.views.home, name="inicio"),
    path('contacto/', appWeb.views.contacto, name='contacto'),
    path('clima/', appWeb.views.clima, name='clima'),
    path('test/', appWeb.views.test, name='test'),
    path('holamundo/', appWeb.views.holamundo, name='holamundo'),
    
    path('listarMascota/',appWeb.views.listar_mascotas, name="listarMascota"),
    path('crearMascota/',appWeb.views.crearMascota, name='crearMascota'),
    path('crearMascotaNav/<str:codigo>/<str:nombre>',appWeb.views.crearMascotaNav, name='crearMascotaNav'),
    path('leermascota/<int:id>',appWeb.views.leer_mascotas, name="leerMascota"),
    path('editarmascota/<int:id>', appWeb.views.editar_mascota, name="editarMascota"),
    path('borrarmascota/<int:id>', appWeb.views.borrar_mascota, name="eliminarMascota"),
    
    #Guardar datos con formulario
    path('nuevaMascota/', appWeb.views.nueva_mascota, name="nuevaMascota"),
    path('guardarMascota/', appWeb.views.guardarMascota, name="guardarMascota"),
    
    #Rutas para formularios
    path('formmascota/', appWeb.views.formMascota, name="formmascota"),
    path('formmascotamod<int:id>/', appWeb.views.formMascotamod, name="formmascotamod"),
    path('formmascotadel/<int:id>/', appWeb.views.formMascotadel, name="formmascotadel"),
    
    path('api/', include('rest_mascota.urls')),

]
