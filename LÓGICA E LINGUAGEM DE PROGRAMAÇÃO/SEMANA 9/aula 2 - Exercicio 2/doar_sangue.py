# Exercício 2.4
idade = int(input("Qual sua idade? "))
if idade < 19 or idade > 69:
    print("Infelizmente, você não pode ser doador.")
    exit()

peso = float(input("Qual seu peso? "))
if peso < 50:
    print("Infelizmente, você não pode ser doador.")
    exit()

tatuagem = input("Você fez alguma tatuagem no último ano (S/N)? ").upper()
if tatuagem == "S":
    print("Infelizmente, você não pode ser doador.")
    exit()

alcool = input("Você ingeriu álcool nas últimas 12 horas (S/N)? ").upper()
if alcool == "S":
    print("Infelizmente, você não pode ser doador.")
else:
    print("Parabéns, você pode doar sangue.")
