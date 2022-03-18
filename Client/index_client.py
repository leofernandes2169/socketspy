import threading #processos que rodam paralelamente
import socket

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #usando ipv4 e protocolo TCP
    

    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nNão foi possível se conectar ao servidor')

    username = input('Usuário => ')
    print('\nConectado')

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()



def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg+'\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor')
            print('\nPressione <Enter> para continuar...')
            client.close()
            break

def sendMessages(client, username):
    while True:
        try:
            msg = input('\n')
            client.sendall(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return

main()