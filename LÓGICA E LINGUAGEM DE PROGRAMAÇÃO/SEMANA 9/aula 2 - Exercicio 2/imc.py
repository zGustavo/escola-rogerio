# Exercício 2.2
peso = float(input("Qual seu peso (kg)? "))
altura = float(input("Qual sua altura (m)? "))
imc = peso / (altura ** 2)
print(f"IMC = {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Peso normal.")
elif 25 <= imc < 29.9:
    print("Sobrepeso.")
else:
    print("Obesidade.")
