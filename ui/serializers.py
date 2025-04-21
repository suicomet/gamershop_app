from rest_framework import serializers
from .models import Juego

class JuegoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()

    class Meta:
        model = Juego
        fields = ['id', 'nombre', 'descripcion', 'precio', 'categoria']

