# Leitura da idade do cliente
print("Qual sua idade?")
idade = int(input())

# Definição do valor base do plano de saúde
valor_base = 100

# Determinação do valor adicional conforme a faixa etária
if idade < 10:
    adicional = 80
elif idade <= 30:
    adicional = 50
elif idade <= 60:
    adicional = 95
else:
    adicional = 130

# Cálculo do valor total a ser pago
valor_total = valor_base + adicional

# Exibição do valor total
print("O valor a ser pago pelo plano de saúde é R$ " + str(valor_total) + ".")
