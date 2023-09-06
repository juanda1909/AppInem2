from django.shortcuts import render, redirect
from .forms import EstudianteRegistroForm  # Importa los formularios necesarios

def index(request):
    return render(request, 'appinem_app/index.html')  # Renderiza la plantilla index.html

def login(request):
    # Lógica para la vista de inicio de sesión para estudiantes
    return render(request, 'appinem_app/login.html')  # Renderiza la plantilla login.html

def login_profesores(request):
    return render(request, 'appinem_app/loginProfesores.html')  # Renderiza la plantilla loginProfesores.html

def registro(request):
    if request.method == 'POST':
        form = EstudianteRegistroForm(request.POST)
        if form.is_valid():
            # Procesa y guarda los datos del estudiante en la base de datos MySQL
            # Ejemplo:
            # estudiante = Estudiante(Tarjeta_identidad=form.cleaned_data['Tarjeta_identidad'],
            #                          Clave=form.cleaned_data['Clave'])
            # estudiante.save()
            return redirect('index')  # Redirige a la página de inicio después del registro
    else:
        form = EstudianteRegistroForm()

    return render(request, 'appinem_app/registro.html', {'form': form})
