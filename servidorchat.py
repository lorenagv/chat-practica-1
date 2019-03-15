import socket

PORT = 8080
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5


def process_client(clientsocket):
    print(clientsocket)

    while True:
        mensaje_cliente = clientsocket.recv(2048).decode("utf-8")

        if mensaje_cliente.lower() == "salir":
            print("saliendo")
            mensaje_servidor = "Se ha cerrado la conexión."
            enviar_mensaje = str.encode(mensaje_servidor)
            clientsocket.send(enviar_mensaje)
            clientsocket.close()
            break

        print("El cliente nos dice: ", mensaje_cliente)

        mensaje_servidor = input("Introduzca una respuesta: ")
        enviar_mensaje = str.encode(mensaje_servidor)
        clientsocket.send(enviar_mensaje)

        if mensaje_servidor.lower() == "salir" :
            print("saliendo")
            clientsocket.close()
            break


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = IP
try:
    serversocket.bind((hostname, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Esperando conexión con %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()

        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
except KeyboardInterrupt:
print("\n Se ha cerrado la conexión.")
