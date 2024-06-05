# Leitura dos números inteiros
print("Qual o primeiro número?")
numero1 = int(input())
print("Qual o segundo número?")
numero2 = int(input())

# Leitura da operação desejada
print("Qual a operação?")
operacao = input()

# Execução da operação desejada
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    # Verificação para evitar divisão por zero
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
elif operacao == "^":
    resultado = numero1 ** numero2
else:
    resultado = "Erro: Operação inválida."

# Exibição do resultado
print("O resultado da operação é: " + str(resultado))
