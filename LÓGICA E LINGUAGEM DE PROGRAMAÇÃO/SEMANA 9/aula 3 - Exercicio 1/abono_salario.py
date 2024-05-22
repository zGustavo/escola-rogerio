# Exercício 4.2
nome = input("Digite o nome do funcionário: ")
idade = int(input("Digite a idade do funcionário: "))
sexo = input("Digite o sexo do funcionário (M para masculino, F para feminino): ").upper()
salario_fixo = float(input("Digite o salário fixo do funcionário: "))

if sexo == "M":
    if idade >= 30:
        abono = 100
    else:
        abono = 50
elif sexo == "F":
    if idade >= 30:
        abono = 200
    else:
        abono = 80
else:
    print("Sexo inválido.")
    exit()

salario_liquido = salario_fixo + abono
print(f"Nome: {nome}, Salário Líquido: R$ {salario_liquido:.2f}")
