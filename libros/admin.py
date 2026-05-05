from django.contrib import admin
from .models import Libro

# Register your models here.

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'cantidad_disponible', 'fecha_creacion')
    search_fields = ('titulo', 'autor')
    list_filter = ('fecha_creacion', 'cantidad_disponible')
