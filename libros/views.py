from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Libro
from .forms import LibroForm, LoginForm
from .tasks import enviar_gmail


# Create your views here.

def lista_libros(request):
    """Vista pública para listar todos los libros disponibles"""
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})


@require_http_methods(["GET", "POST"])
def login_view(request):
    """Vista para iniciar sesión como administrador"""
    if request.user.is_authenticated:
        return redirect('dashboard_admin')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                messages.success(request, f'¡Bienvenido {username}!')
                return redirect('dashboard_admin')
            else:
                messages.error(request, 'Usuario o contraseña inválidos, o sin permisos de administrador.')
    else:
        form = LoginForm()
    
    return render(request, 'libros/login.html', {'form': form})


def logout_view(request):
    """Vista para cerrar sesión"""
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('lista_libros')


@login_required(login_url='login')
def dashboard_admin(request):
    """Dashboard del administrador"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página.')
        return redirect('lista_libros')
    
    libros = Libro.objects.all()
    return render(request, 'libros/dashboard_admin.html', {'libros': libros})


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def crear_libro(request):
    """Crear un nuevo libro"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página.')
        return redirect('lista_libros')
    
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado exitosamente.')
            return redirect('dashboard_admin')
    else:
        form = LibroForm()
    
    return render(request, 'libros/crear_libro.html', {'form': form})


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def editar_libro(request, libro_id):
    """Editar un libro existente"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página.')
        return redirect('lista_libros')
    
    libro = get_object_or_404(Libro, id=libro_id)
    
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado exitosamente.')
            return redirect('dashboard_admin')
    else:
        form = LibroForm(instance=libro)
    
    return render(request, 'libros/editar_libro.html', {'form': form, 'libro': libro})


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def eliminar_libro(request, libro_id):
    """Eliminar un libro"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página.')
        return redirect('lista_libros')
    
    libro = get_object_or_404(Libro, id=libro_id)
    
    if request.method == 'POST':
        titulo = libro.titulo
        libro.delete()
        messages.success(request, f'Libro "{titulo}" eliminado exitosamente.')
        return redirect('dashboard_admin')
    
    return render(request, 'libros/eliminar_libro.html', {'libro': libro})



def simular_email(request, libro_id):
    if request.method == 'POST':
        # Enviar la tarea a Celery
        enviar_gmail.delay()
        
        return JsonResponse({
            'status': 'ok',
            'mensaje': '¡Solicitud recibida! Te enviaremos un correo cuando el libro esté disponible.'
        })
    return JsonResponse({'error': 'Método no permitido'}, status=405)


def generar_reporte(request):
    if request.method == 'POST':
        #importamos una tarea asincrona
        from .tasks import generar_reporte as tarea_reporte

        #enviar tarea a la cola de celery
        tarea_reporte.delay()

        #Respondemos inmediatamente al administrador
        return JsonResponse({
            'status': 'ok',
            'mensaje': '¡Solicitud de generación de reporte recibida! Te notificaremos cuando el reporte esté listo.'
        })  
    return JsonResponse({'error': 'Método no permitido'}, status=405)