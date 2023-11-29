import psutil
import speedtest

#Rendimiento del CPU
cpu_percent = psutil.cpu_percent()

print(f"Porcentaje de uso del CPU: {cpu_percent}%")

#Rendimiento de la memoria
memory = psutil.virtual_memory()
memory_available = memory.available
memory_used = memory.used

print(f"Memoria disponible: {memory_available / 1024 / 1024:.2f} MB")
print(f"Memoria en uso: {memory_used / 1024 / 1024:.2f} MB")

#Rendimiento de la red
speedInternet = speedtest.Speedtest()
download_speed = speedInternet.download()
upload_speed = speedInternet.upload()

print("Velocidad de descarga: {:.2f} Mbps".format(download_speed / 1e6))
print("Velocidad de subida: {:.2f} Mbps".format(upload_speed / 1e6))
