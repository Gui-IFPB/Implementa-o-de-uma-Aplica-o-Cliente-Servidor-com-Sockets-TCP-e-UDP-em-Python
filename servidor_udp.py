import socket

def iniciar_servidor_udp():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind(('0.0.0.0', 5001))
    print("Servidor UDP escutando na porta 5001")

    while True:
        data, addr = servidor.recvfrom(1024)
        print(f"Mensagem UDP de {addr}")
        if data:
            resposta = f"UDP: {data.decode()}"
            servidor.sendto(resposta.encode(), addr)
            print(f"Respondido: {resposta}")

if __name__ == "__main__":
    iniciar_servidor_udp()
