import socket

def iniciar_servidor_tcp():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('0.0.0.0', 5000))
    servidor.listen()
    print("Servidor TCP escutando na porta 5000")

    while True:
        conn, addr = servidor.accept()
        print(f"Conexão TCP de {addr}")
        data = conn.recv(1024)
        if data:
            resposta = f"TCP: {data.decode()}"
            conn.send(resposta.encode())
            print(f"Respondido: {resposta}")
        conn.close()

if __name__ == "__main__":
    iniciar_servidor_tcp()
