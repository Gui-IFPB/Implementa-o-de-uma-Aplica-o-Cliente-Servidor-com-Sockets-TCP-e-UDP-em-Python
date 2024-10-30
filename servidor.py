import socket
import threading

def tratar_cliente_tcp(conn, addr):
    print(f"Conexão TCP de {addr}")
    data = conn.recv(1024)
    if data:
        resposta = f"TCP: {data.decode()}"
        conn.send(resposta.encode())
        print(f"Respondido: {resposta}")
    conn.close()

def iniciar_servidor_tcp():
    servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_tcp.bind(('0.0.0.0', 5000))
    servidor_tcp.listen()
    print("Servidor TCP escutando na porta 5000")
    
    while True:
        conn, addr = servidor_tcp.accept()
        thread = threading.Thread(target=tratar_cliente_tcp, args=(conn, addr))
        thread.start()

def iniciar_servidor_udp():
    servidor_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor_udp.bind(('0.0.0.0', 5001))
    print("Servidor UDP escutando na porta 5001")

    while True:
        data, addr = servidor_udp.recvfrom(1024)
        print(f"Mensagem UDP de {addr}")
        if data:
            resposta = f"UDP: {data.decode()}"
            servidor_udp.sendto(resposta.encode(), addr)
            print(f"Respondido: {resposta}")

if __name__ == "__main__":
    tcp_thread = threading.Thread(target=iniciar_servidor_tcp)
    udp_thread = threading.Thread(target=iniciar_servidor_udp)
    tcp_thread.start()
    udp_thread.start()
    tcp_thread.join()
    udp_thread.join()
