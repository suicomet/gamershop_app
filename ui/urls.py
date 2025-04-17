from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("Categorias.html", views.categorias, name="categorias"),
    path("Accion.html", views.accion, name="accion"),
    path("admin-pag.html", views.admin_pag, name="admin_pag"),
    path("Aventura.html", views.aventura, name="aventura"),
    path("Estrategia.html", views.estrategia, name="estrategia"),
    path("formulario.html", views.registrar, name="registrar"),
    path("FreeToPlay.html", views.freeToPlay, name="freeToPlay"),
    path("login.html", views.login, name="login"),
    path("terminos.html", views.terminos, name="terminos"),
    path("Terror.html", views.terror, name="terror"),
    path("index.html", views.inicio, name="inicio")
]
