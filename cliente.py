import socket

def cliente():
    protocolo = input("Escolha o protocolo (TCP/UDP): ").upper()
    mensagem = input("Digite a mensagem a ser enviada: ")

    if protocolo == "TCP":
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect(('localhost', 5000))
        cliente_socket.send(mensagem.encode())
        resposta = cliente_socket.recv(1024).decode()
        print(f"Resposta do servidor: {resposta}")
        cliente_socket.close()

    elif protocolo == "UDP":
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cliente_socket.sendto(mensagem.encode(), ('localhost', 5001))
        resposta, _ = cliente_socket.recvfrom(1024)
        print(f"Resposta do servidor: {resposta.decode()}")
        cliente_socket.close()

if __name__ == "__main__":
    cliente()
