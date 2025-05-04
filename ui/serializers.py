from rest_framework import serializers
from .models import Juego
from .models import Comentario

class JuegoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()

    class Meta:
        model = Juego
        fields = ['id', 'nombre', 'descripcion', 'precio', 'categoria']

class ComentarioSerializer(serializers.ModelSerializer):
    autor_username = serializers.CharField(source='autor.user.username', read_only=True)
    post_titulo = serializers.CharField(source='post.titulo', read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'autor_username', 'post_titulo', 'contenido', 'fecha_comentario']