import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))  # Conecta ao servidor

    while True:
        # Recebe a mensagem do servidor
        data = client_socket.recv(1024).decode()
        if not data:
            break  # Encerra se não houver mais dados

        print(data)  # Exibe a pergunta e as opções

        if "Escolha uma opção" in data:
            # Envia a resposta para o servidor
            answer = input("Sua resposta: ")
            client_socket.send(answer.encode())

    client_socket.close()

if __name__ == "__main__":
    start_client()