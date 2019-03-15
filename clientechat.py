import socket

IP = "127.0.0.1"
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

def envia_info():
    while True:
        mensaje_cliente = input("Introduzca un mensaje: ")

        if mensaje_cliente.lower() == "salir" :
            enviar_mensaje = str.encode(mensaje_cliente)
            s.send(enviar_mensaje)
            print("Se ha cerrado la conexión.")
            s.close()
            break

        enviar_mensaje = str.encode(mensaje_cliente)
        s.send(enviar_mensaje)

        mensaje_servidor = s.recv(2048).decode("utf-8")
        print("El servidor nos dice: ", mensaje_servidor)

        if  mensaje_servidor.lower() == "salir":
            print("El servidor ha cerrado a conexión.")
            s.close()
            break

try:
    s.connect((IP, PORT))
    print("Conexión establecida con el servidor ")
    envia_info()
except OSError:
    print("El Socket ya está usado")
    s.close()
except KeyboardInterrupt:
print("\n Se ha cerrado la conexión.")
