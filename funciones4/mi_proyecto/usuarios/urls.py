from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('perfil/', views.perfil, name='perfil'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('', views.inicio, name='inicio'),
]
