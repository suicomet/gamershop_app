from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from .decorators import allowed_roles, admin_only
from .forms import ModificarPerfilForm
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

def estrategia(request):
    return render(request, "Estrategia.html")


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

def terror(request):
    return render(request, "Terror.html")

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