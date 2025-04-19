from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView

# Create your views here.


def home(request):
    return render(request, "index.html")

def categorias(request):
    return render(request, "Categorias.html")

def accion(request):
    return render(request, "Accion.html")

def admin_pag(request):
    return render(request, "admin-pag.html")

def aventura(request):
    return render(request, "Aventura.html")

def estrategia(request):
    return render(request, "Estrategia.html")

def registrar(request):
    return render(request, "formulario.html")

def freeToPlay(request):
    return render(request, "FreeToPlay.html")

def login(request):
    return render(request, "login.html")

def terminos(request):
    return render(request, "terminos.html")

def terror(request):
    return render(request, "Terror.html")

def inicio(request):
    return render(request, "index.html")

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return self.success_url