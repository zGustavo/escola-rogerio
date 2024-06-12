# Exibindo as perguntas e coletando as respostas

# Pergunta 1: Raiz quadrada
print("1 - Qual é a raiz quadrada de 64?")
resposta1 = int(input("R. ").strip())  # A resposta deve ser um número inteiro

# Pergunta 2: Potência (elevação ao cubo)
print("2 - Qual é o valor de 4^3 (4 elevado ao cubo)?")
resposta2 = int(input("R. ").strip())

# Pergunta 3: Resto da divisão
print("3 - O que é 15 % 4 (o resto da divisão de 15 por 4)?")
resposta3 = int(input("R. ").strip())

# Pergunta 4: Divisão simples
print("4 - Qual é o resultado de 100 / 4?")
resposta4 = int(input("R. ").strip())

# Pergunta 5: Soma de ângulos internos de um triângulo
print("5 - Qual é a soma dos ângulos internos de um triângulo (em graus)?")
resposta5 = int(input("R. ").strip())

# Variável para contar o número de acertos
acertos = 0

# Verificando cada resposta
if resposta1 == 8:  # Raiz quadrada de 64 é 8
    acertos += 1

if resposta2 == 64:  # 4^3 (4 elevado ao cubo) é 64
    acertos += 1

if resposta3 == 3:  # 15 % 4 (resto da divisão de 15 por 4) é 3
    acertos += 1

if resposta4 == 25:  # 100 / 4 é 25
    acertos += 1

if resposta5 == 180:  # A soma dos ângulos internos de um triângulo é 180 graus
    acertos += 1

# Exibindo o total de acertos
print(f"Você acertou {acertos} questões.")
