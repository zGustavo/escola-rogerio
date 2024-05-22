# Exercício 1.2
nota1 = float(input("Qual sua primeira nota? "))
nota2 = float(input("Qual sua segunda nota? "))
media = (nota1 + nota2) / 2
print(f"Sua média foi {media}.")
if media >= 6:
    print("Parabéns você foi aprovado.")
else:
    print("Você não foi aprovado.")
