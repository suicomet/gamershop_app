from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    CustomLoginView, home, categorias, accion, admin_pag, aventura,
    estrategia, registrar, freeToPlay, terminos, terror, inicio,
    modificar_perfil, recuperar_contrasena)


urlpatterns = [
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
]
