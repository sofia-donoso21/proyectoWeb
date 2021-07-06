from rest_mascota.viewsLogin import login
from django.urls import path
from rest_mascota.views import lista_mascotas, detalle_mascota
from rest_mascota.viewsLogin import login

urlpatterns = [
    path('lista_mascotas/', lista_mascotas, name="lista_mascotaS"), 
    path('detalle_mascota/<str:codigo>/', detalle_mascota, name="detalle_mascota"),
    path('login', login, name="login"),
]
