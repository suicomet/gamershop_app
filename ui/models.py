from django.db import models
from django.contrib.auth.models import User  # <-- IMPORTANTE

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Valoracion(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    voto = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    opinion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.juego.nombre} - {self.voto} estrellas"

# models.py

class UsuarioForo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(blank=True)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    autor = models.ForeignKey(UsuarioForo, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(UsuarioForo, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.user.username} - {self.post.titulo}"
