from django import forms
from django.forms import ModelForm, fields
from .models import Mascotas

class MascotasForm(ModelForm):

    class Meta:
        model = Mascotas
        fields=['codigo','nombre','tipoMascota','adoptado']






