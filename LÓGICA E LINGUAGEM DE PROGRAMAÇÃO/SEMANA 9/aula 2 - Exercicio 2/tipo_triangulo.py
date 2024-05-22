# Exercício 2.1
lado1 = int(input("Informe o primeiro lado do triângulo: "))
lado2 = int(input("Informe o segundo lado do triângulo: "))
lado3 = int(input("Informe o terceiro lado do triângulo: "))

if lado1 == lado2 == lado3:
    print("Trata-se de um triângulo equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Trata-se de um triângulo isósceles.")
else:
    print("Trata-se de um triângulo escaleno.")
