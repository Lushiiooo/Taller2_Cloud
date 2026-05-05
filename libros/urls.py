from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('crear/', views.crear_libro, name='crear_libro'),
    path('editar/<int:libro_id>/', views.editar_libro, name='editar_libro'),
    path('eliminar/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),
]
