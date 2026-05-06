from celery import shared_task
import time

@shared_task
def enviar_gmail():
    print("Enviando correo electrónico...")
    time.sleep(10)
    print("Correo electrónico enviado.")
    return "Correo electrónico enviado exitosamente."

@shared_task
def generar_reporte():
    print("Generando reporte...")
    time.sleep(10)
    print("Reporte generado.")
    return "Reporte generado exitosamente."