# Definindo os preços dos salgadinhos com base no código
preco_coxinha = 0.50
preco_pastel = 0.75
preco_pao_de_queijo = 0.40
preco_enroladinho = 0.80

# Leitura do código do salgado
print("Qual o código do salgado?")
codigo = int(input())

# Leitura da quantidade de salgados
print("Qual a quantidade de salgados?")
quantidade = int(input())

# Cálculo do valor total com base no código do salgado
if codigo == 1:
    total = preco_coxinha * quantidade
    print("Sua conta foi " + str(total) + " reais.")
elif codigo == 2:
    total = preco_pastel * quantidade
    print("Sua conta foi " + str(total) + " reais.")
elif codigo == 3:
    total = preco_pao_de_queijo * quantidade
    print("Sua conta foi " + str(total) + " reais.")
elif codigo == 4:
    total = preco_enroladinho * quantidade
    print("Sua conta foi " + str(total) + " reais.")
else:
    print("Código não reconhecido.")
