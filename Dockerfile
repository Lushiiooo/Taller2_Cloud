# Usar una imagen oficial de Python ligera
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Variables de entorno para optimizar Python en contenedores
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copiar el archivo de dependencias e instalar
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código del proyecto al contenedor
COPY . /app/