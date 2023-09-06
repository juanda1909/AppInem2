from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('login/', views.login, name='login'),  # Página de inicio de sesión para estudiantes
    path('login-profesores/', views.login_profesores, name='login-profesores'),  # Página de inicio de sesión para profesores
    path('registro/', views.registro, name='registro'),  # Página de registro
]
