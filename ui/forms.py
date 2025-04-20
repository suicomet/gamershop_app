from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class ModificarPerfilForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Fecha de nacimiento',
        required=False
    )
    direccion = forms.CharField(
        label='Dirección',
        required=False
    )

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']
        labels = {
            'first_name': 'Nombre completo',
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico'
        }
        help_texts = {
            'username': None
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

    def clean_username(self):
        username = self.cleaned_data['username']
        user_id = self.instance.id
        if User.objects.exclude(id=user_id).filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso.")
        return username


class RegistroUsuarioForm(forms.ModelForm):
    contra = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    recontra = forms.CharField(widget=forms.PasswordInput, label='Reingrese su contraseña')
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha de nacimiento')
    direccion = forms.CharField(required=False, label='Dirección')

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']
        labels = {
            'first_name': 'Nombre completo',
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico'
        }
        help_texts = {
            'username': 'Requerido. Letras, números y @/./+/-/_ solamente.',
        }

    def clean_first_name(self):
        nombre = self.cleaned_data['first_name']
        if any(char.isdigit() for char in nombre):
            raise ValidationError("El nombre no debe contener números.")
        if len(nombre) < 3:
            raise ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 4:
            raise ValidationError("El nombre de usuario debe tener al menos 4 caracteres.")
        if User.objects.filter(username=username).exists():
            raise ValidationError("El nombre de usuario ya está en uso.")
        return username

    def clean_contra(self):
        contra = self.cleaned_data['contra']
        if len(contra) < 6:
            raise ValidationError("La contraseña debe tener al menos 6 caracteres.")
        if not re.search(r'[A-Za-z]', contra):
            raise ValidationError("La contraseña debe contener al menos una letra.")
        if not re.search(r'\d', contra):
            raise ValidationError("La contraseña debe contener al menos un número.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contra):
            raise ValidationError("La contraseña debe contener al menos un carácter especial.")
        return contra

    def clean(self):
        cleaned_data = super().clean()
        contra = cleaned_data.get("contra")
        recontra = cleaned_data.get("recontra")

        if contra and recontra and contra != recontra:
            raise ValidationError("Las contraseñas no coinciden.")
