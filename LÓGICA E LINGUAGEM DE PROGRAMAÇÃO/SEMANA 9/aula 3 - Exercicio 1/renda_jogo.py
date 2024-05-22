# Exercício 4.1
publico_total = int(input("Informe o público do jogo: "))

popular = publico_total * 0.10 * 5
geral = publico_total * 0.50 * 10
arquibancada = publico_total * 0.30 * 20
cadeiras = publico_total * 0.10 * 30

renda_total = popular + geral + arquibancada + cadeiras
print(f"O valor da renda total é R$ {renda_total:.2f}")
