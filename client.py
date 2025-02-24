import socket

# Criação do socket do cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12345))  # Conecta-se ao servidor

# Loop para receber perguntas e enviar respostas
while True:
    data = client.recv(1024).decode()
    if not data:
        break
    print(data, end="")

    # Se for uma pergunta com opções, espera uma resposta do usuário
    if data[0].isdigit():  # Se começar com um número, espera uma resposta
        response = input("Digite o número da resposta: ")
        client.send(response.encode())  # Envia a resposta para o servidor

client.close()  # Fecha a conexão após o término do quiz
