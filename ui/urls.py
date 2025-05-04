from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    CustomLoginView, home, categorias, accion, admin_pag, aventura,
    estrategia, registrar, freeToPlay, terminos, terror, inicio,
    modificar_perfil, recuperar_contrasena, detalle_post, foro, noticias_gamer, JuegoListAPIView, listar_juegos, eliminar_juego, juegos_gratis, editar_juego
, ComentarioListAPIView ,apis_desarrollo)


urlpatterns = [
    path('api/juegos/', JuegoListAPIView.as_view(), name='api_juegos'),
    path('listar-juegos/', listar_juegos, name='listar_juegos'),
    path('juegos/eliminar/<int:juego_id>/', eliminar_juego, name='eliminar_juego'),

    path('juegos/editar/<int:juego_id>/', editar_juego, name='editar_juego'),

    path('noticias/', noticias_gamer, name='noticias_gamer'),
    path('', home, name='index'),
    path('categorias/', categorias, name='categorias'),
    path('accion/', accion, name='accion'),
    path('admin-pag/', admin_pag, name='admin_pag'),
    path('aventura/', aventura, name='aventura'),
    path('estrategia/', estrategia, name='estrategia'),
    path('registrar/', registrar, name='registro'),
    path('free-to-play/', freeToPlay, name='free_to_play'),
    path('terminos/', terminos, name='terminos'),
    path('terror/', terror, name='terror'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('modificar-perfil/', modificar_perfil, name='modificar_perfil'),
    path('recuperar-contrasena/', recuperar_contrasena, name='recuperar_contrasena'),
    path('foro/', foro, name='foro'),
    path('post/<int:post_id>/', detalle_post, name='detalle_post'),

    path('juegos-gratis/', juegos_gratis, name='juegos_gratis'),
    path('api/comentarios/', ComentarioListAPIView.as_view(), name='api_comentarios'),
    path('apis/', apis_desarrollo, name='apis_desarrollo'),
]