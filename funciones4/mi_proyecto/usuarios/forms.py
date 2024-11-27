from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    fecha_nacimiento = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    telefono = forms.CharField(max_length=15, required=True)

    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'email', 'fecha_nacimiento', 'telefono', 'password1', 'password2']

