import socket

# Lista de perguntas com alternativas e respostas corretas
questions = [
    {"question": "Quem pintou a Mona Lisa?", "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"], "answer": 1},
    {"question": "Em que ano o homem pisou na Lua pela primeira vez?", "options": ["1965", "1969", "1972", "1980"], "answer": 1},
    {"question": "Quem foi o primeiro presidente do Brasil?", "options": ["Juscelino Kubitschek", "Getúlio Vargas", "Deodoro da Fonseca", "Dom Pedro II"], "answer": 2}
]

# Função para lidar com o cliente conectado
def handle_client(conn):
    score = 0
    for i, q in enumerate(questions):
        # Monta a mensagem com a pergunta e as opções
        message = f"{q['question']}\n"
        for idx, option in enumerate(q["options"]):
            message += f"{idx+1}. {option}\n"
        message += "Escolha uma opção (1, 2, 3, 4): "

        # Envia a pergunta para o cliente
        conn.send(message.encode())

        # Recebe a resposta do cliente e verifica se está correta
        response = conn.recv(1024).decode().strip()
        if response.isdigit():
            response = int(response) - 1
            if response == q["answer"]:
                score += 1

    # Envia o resultado final ao cliente
    conn.send(f"Você acertou {score} de {len(questions)} perguntas.\n".encode())
    conn.close()

# Criação do socket do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12345))  
server.listen(5)  
print("Servidor esperando conexões...")

# Loop para aceitar conexões de clientes
while True:
    conn, addr = server.accept()
    print(f"Conexão recebida de {addr}")
    handle_client(conn)