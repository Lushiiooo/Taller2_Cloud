import os
from celery import Celery

# Establece el módulo de configuración de Django por defecto para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')

# Crea la instancia de la aplicación (Celery la buscará automáticamente)
app = Celery('biblioteca')

# Carga la configuración desde los settings de Django usando el prefijo 'CELERY_'
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodescubre las tareas asíncronas en todas las apps instaladas (como tu app 'libros')
app.autodiscover_tasks()