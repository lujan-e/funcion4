from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from .models import UsuarioPersonalizado
from django.contrib.auth import logout

# Vista para registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Te has registrado correctamente.")
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

# Vista para inicio de sesión
def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.error(request, "Credenciales incorrectas")
    else:
        form = AuthenticationForm()
    
    return render(request, 'usuarios/inicio_sesion.html', {'form': form})

# Vista para perfil del usuario
@login_required
def perfil(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            messages.success(request, "Contraseña cambiada exitosamente.")
            return redirect('perfil')
    else:
        password_form = PasswordChangeForm(user=request.user)
    
    return render(request, 'usuarios/perfil.html', {'password_form': password_form})

# Vista para cerrar sesión
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

# Vista para la página principal (inicio)
def inicio(request):
    return render(request, 'usuarios/inicio.html')


