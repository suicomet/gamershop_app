from django.contrib import admin
from .models import Categoria, Juego, Valoracion, UsuarioForo, Post, Comentario

admin.site.register(Categoria)
admin.site.register(Juego)
admin.site.register(Valoracion)
admin.site.register(UsuarioForo)
admin.site.register(Post)
admin.site.register(Comentario)
