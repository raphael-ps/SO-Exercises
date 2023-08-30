import socket
import threading
import datetime

def receive_and_send(socket: socket.socket):
    end_while = False
    while not end_while:   
        data = socket.recv(2048)

        msg = data.decode()
        response = ''
        date = datetime.datetime.now()

        if(msg == 'data'):
            response = date.strftime('%d/%m/%Y')
        elif msg == 'hora':
            response = date.strftime('%H:%M:%S')
        elif msg == 'data e hora':
            response = date.strftime('%d/%m/%Y %H:%M:%S')
        elif msg == '/sair':
            response = 'Encerrando conexao'
            end_while = True
            print('conexão encerrada')
        else: 
            response = 'Opção Inválida'
        
        socket.sendall(response.encode())
    socket.close()         

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.0.84.202', 8080)

sock.bind(server_address)
sock.listen(1)
print('Servidor Iniciado e aguardando conexões')

while True: 
    sock_client, address = sock.accept()

    t = threading.Thread(target=receive_and_send, args=(sock_client,))
    t.start()



