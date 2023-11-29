import socket
socket_cliente.settimeout(10) # Aumenta el tiempo de espera a 10 segundos

def conectar(ip, puerto):
    # Crear un objeto socket
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar el socket al servidor remoto
    socket_cliente.connect((ip, puerto))

    # Recibir y mostrar mensaje del servidor
    recibido = socket_cliente.recv(1024)
    print(recibido.decode())

    # Cerrar el socket
    socket_cliente.close()

ip = "10.3.21.188" # Reemplaza con la dirección IP del servidor al que deseas conectarte
puerto = 80        # Reemplaza con el puerto en el que está escuchando el servidor

conectar(ip, puerto)