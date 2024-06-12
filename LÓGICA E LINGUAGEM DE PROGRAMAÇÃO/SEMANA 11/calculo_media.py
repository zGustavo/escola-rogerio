# Solicitar as três notas ao usuário
nota1 = float(input("Informe a primeira nota: ").strip())
nota2 = float(input("Informe a segunda nota: ").strip())
nota3 = float(input("Informe a terceira nota: ").strip())

# Calcular a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibir a média
print(f"Sua média foi {media:.1f}.")

# Verificar o status do aluno com base na média
if media < 4:
    print("Você foi reprovado.")
elif media >= 7:
    print("Você foi aprovado.")
else:
    # Média está entre 4 e 7, calcular a nota necessária na final
    nota_final = (5 - (media * 0.6)) / 0.4
    print(f"Você foi para a final. Você precisa de {nota_final:.1f} na final.")
