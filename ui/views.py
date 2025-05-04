from django.shortcuts import render, redirect
from .forms import JuegoForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from .decorators import allowed_roles, admin_only
from .forms import ModificarPerfilForm
from django.shortcuts import get_object_or_404
from .models import Post, Comentario
import requests
from django.shortcuts import render
from rest_framework import generics
from .models import Juego
from .serializers import JuegoSerializer

# Create your views here.


def home(request):
    return render(request, "index.html")

def categorias(request):
    return render(request, "Categorias.html")

def accion(request):
    return render(request, "Accion.html")

@login_required(login_url='login')
@allowed_roles(roles=['administrador'])
def admin_pag(request):
    return render(request, 'admin-pag.html')

def aventura(request):
    return render(request, "Aventura.html")

def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_juegos')  # Lo crearemos en el paso 4
    else:
        form = JuegoForm()
    return render(request, 'crear_juego.html', {'form': form})

def listar_juegos(request):
    juegos = Juego.objects.all().order_by('nombre')
    return render(request, 'listar_juegos.html', {'juegos': juegos})
@login_required(login_url='login')
@allowed_roles(roles=['Administradores'])
def eliminar_juego(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    juego.delete()
    messages.success(request, f'Juego "{juego.nombre}" eliminado correctamente.')
    return redirect('listar_juegos')
@login_required(login_url='login')
@allowed_roles(roles=['Administradores'])
def editar_juego(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    if request.method == 'POST':
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            messages.success(request, f'Juego "{juego.nombre}" editado correctamente.')
            return redirect('listar_juegos')
    else:
        form = JuegoForm(instance=juego)

    return render(request, 'editar_juego.html', {'form': form, 'juego': juego})
def estrategia(request):
    return render(request, "Estrategia.html")

def noticias_gamer(request):
    api_key = '7614c57452484252a27afa2f273b8d60'
    url = f'https://newsapi.org/v2/everything?q=videogames&language=es&sortBy=publishedAt&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    noticias = data.get('articles', [])
    return render(request, 'noticias.html', {'noticias': noticias})

from django.contrib.auth.models import User
from .forms import RegistroUsuarioForm

def registrar(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            nombre = form.cleaned_data['first_name']
            contra = form.cleaned_data['contra']

            # Crear usuario
            usuario = User.objects.create_user(
                username=username,
                password=contra,
                email=email,
                first_name=nombre
            )



            messages.success(request, 'Usuario registrado con éxito.')
            return redirect('login')
        else:
            messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'formulario.html', {'form': form})


def recuperar_contrasena(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            messages.error(request, "Debes ingresar un correo válido.")
        else:
            # Simulación de envío de correo
            messages.success(request, "Se ha enviado un enlace de recuperación a tu correo.")
    return render(request, 'recuperar_contrasena.html')

def freeToPlay(request):
    return render(request, "FreeToPlay.html")

def login(request):
    return render(request, "login.html")

def terminos(request):
    return render(request, "terminos.html")

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = Comentario.objects.filter(post=post).order_by('-fecha_comentario')

    for c in comentarios:
        print("Comentario de:", c.autor.user.username, "-", c.contenido)

    return render(request, 'detalle_post.html', {
        'post': post,
        'comentarios': comentarios
    })

def juegos_gratis(request):
    url = 'https://www.freetogame.com/api/games?platform=pc'
    response = requests.get(url)
    data = response.json()[:6]  # mostrar solo los primeros 6
    return render(request, 'juegos_gratis.html', {'juegos': data})


def terror(request):
    return render(request, "Terror.html")

def foro(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')
    return render(request, 'foro.html', {'posts': posts})

def inicio(request):
    return render(request, "index.html")

@login_required(login_url='login')
def modificar_perfil(request):
    if request.method == 'POST':
        form = ModificarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado correctamente.')
            return redirect('index')  # o puedes redirigir a 'modificar_perfil' si quieres quedarse ahí
        else:
            messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = ModificarPerfilForm(instance=request.user)

    return render(request, 'modificar_perfil.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return self.success_url

class JuegoListAPIView(generics.ListAPIView):
    queryset = Juego.objects.all().order_by('nombre')
    serializer_class = JuegoSerializer