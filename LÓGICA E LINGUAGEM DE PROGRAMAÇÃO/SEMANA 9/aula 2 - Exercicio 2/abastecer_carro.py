# Exercício 2.3
km_por_litro = float(input("Quantos quilômetros o carro percorre por litro? "))
litros_atual = float(input("Quantos litros tem no carro atualmente? "))
distancia = float(input("Qual distância (em km) você deseja percorrer? "))

necessario = distancia / km_por_litro

if necessario > litros_atual:
    abastecer = necessario - litros_atual
    print(f"Você precisa abastecer {abastecer:.2f} litros.")
else:
    print("Você não precisa abastecer.")
