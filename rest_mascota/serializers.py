from rest_framework import serializers
from appWeb.models import Mascotas


class MascotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascotas
        fields = ['codigo', 'nombre', 'tipoMascota', 'adoptado']
