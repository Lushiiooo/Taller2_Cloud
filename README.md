# 📚 Biblioteca Virtual - Django

Una aplicación web de biblioteca virtual desarrollada con Django puro, con una interfaz hermosa usando CSS y HTML.

## 🎯 Características

### Para Usuarios Públicos
- ✅ Ver lista de libros disponibles
- ✅ Ver detalles de cada libro (título, autor, descripción, cantidad disponible)
- ✅ Botón "Avisame cuando esté disponible" para libros sin stock (estético por ahora)
- ✅ Interfaz responsive y bonita

### Para Administradores
- ✅ **Crear libros**: Agregar nuevos libros a la biblioteca
- ✅ **Leer/Listar libros**: Ver todos los libros en un dashboard
- ✅ **Editar libros**: Modificar información de libros existentes
- ✅ **Eliminar libros**: Remover libros de la biblioteca con confirmación
- ✅ Panel de administración con estadísticas
- ✅ Tabla de gestión de libros

## 🚀 Instalación y Uso

### Requisitos
- Python 3.8+
- pip

### Pasos para ejecutar

1. **Navega a la carpeta del proyecto**
   ```bash
   cd Taller
   ```

2. **Activa el entorno virtual** (Windows)
   ```bash
   venv\Scripts\activate
   ```

3. **Inicia el servidor Django**
   ```bash
   python manage.py runserver
   ```

4. **Abre tu navegador** e ingresa a:
   ```
   http://127.0.0.1:8000/
   ```

## 🔐 Credenciales de Administrador

- **Usuario**: `admin`
- **Contraseña**: `12345`

## 📖 URLs de la Aplicación

| URL | Descripción |
|-----|-------------|
| `/` | Página principal - Lista de libros públicos |
| `/login/` | Página de inicio de sesión |
| `/logout/` | Cerrar sesión |
| `/dashboard/` | Panel de administrador |
| `/crear/` | Crear nuevo libro |
| `/editar/<id>/` | Editar un libro existente |
| `/eliminar/<id>/` | Eliminar un libro |
| `/admin/` | Panel de administración de Django |

## 🎨 Diseño y Estilos

- **Colores principales**: Gradiente púrpura-azul (#667eea a #764ba2)
- **Tema responsive**: Se adapta a dispositivos móviles y de escritorio
- **Animaciones suaves**: Transiciones y efectos hover
- **Iconos emoji**: Para mejor visualización y claridad

## 📊 Modelo de Datos

### Modelo: Libro
- `titulo` (CharField): Título del libro
- `autor` (CharField): Nombre del autor
- `descripcion` (TextField): Descripción del libro
- `cantidad_disponible` (IntegerField): Número de copias disponibles
- `fecha_creacion` (DateTimeField): Fecha de creación
- `fecha_actualizacion` (DateTimeField): Fecha de última actualización

## 🔄 Funcionalidades CRUD

### Create (Crear)
- Accede a `/crear/` como administrador
- Completa el formulario con los datos del libro
- Haz clic en "Guardar Libro"

### Read (Leer)
- Accede a `/` para ver libros como usuario público
- Accede a `/dashboard/` como administrador para ver todos los libros

### Update (Editar)
- En el dashboard, haz clic en "Editar" para modificar un libro
- Realiza los cambios necesarios
- Haz clic en "Guardar Cambios"

### Delete (Eliminar)
- En el dashboard, haz clic en "Eliminar"
- Confirma la eliminación
- El libro se eliminará de la base de datos

## 🛡️ Seguridad

- ✅ Validación de formularios
- ✅ Protección CSRF
- ✅ Solo administradores pueden acceder a funciones CRUD
- ✅ Redirección automática de usuarios no autenticados
- ✅ Confirmación requerida para eliminar

## 💾 Base de Datos

La aplicación utiliza SQLite por defecto. Los datos se almacenan en `db.sqlite3`.

Para crear migraciones:
```bash
python manage.py makemigrations
```

Para aplicar migraciones:
```bash
python manage.py migrate
```

## 📱 Libros de Prueba

La base de datos viene precargada con 5 libros de prueba:
1. El Quijote - Miguel de Cervantes (3 copias)
2. Cien años de soledad - Gabriel García Márquez (2 copias)
3. 1984 - George Orwell (1 copia)
4. Orgullo y prejuicio - Jane Austen (0 copias - No disponible)
5. El Código Da Vinci - Dan Brown (2 copias)

## 🔮 Características Futuras

- [ ] Sistema de notificaciones para libros disponibles
- [ ] Historial de cambios
- [ ] Búsqueda y filtrado de libros
- [ ] Sistema de préstamos
- [ ] Comentarios y calificaciones
- [ ] Subida de portadas de libros
- [ ] API REST para integración con otras plataformas

## 📝 Notas

- El botón "Avisame cuando esté disponible" es actualmente estético y será implementado en futuras versiones
- El servidor de desarrollo está diseñado solo para desarrollo, no para producción
- Para producción, usa un servidor WSGI como Gunicorn o uWSGI

## ✨ Autor

Proyecto desarrollado como un sistema de gestión de biblioteca virtual en Django.

---

¡Disfruta de tu Biblioteca Virtual! 📚✨
