import socket

connection_socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.0.84.202', 8080)

connection_socker.connect(server_address)

end_loop = False
while not end_loop:
    msg = str(input("Informe a mensagem a ser enviada: "))

    connection_socker.sendall(msg.encode())

    response = connection_socker.recv(2048)
    print('-='*50)
    print('From Server:\n\t', response.decode())
    print('=-'*50)

    if (msg == '/sair'):
        end_loop = True
        connection_socker.close()