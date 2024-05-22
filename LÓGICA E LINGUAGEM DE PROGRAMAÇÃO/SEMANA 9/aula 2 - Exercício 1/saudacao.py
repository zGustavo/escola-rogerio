# Exercício 1.3
nome = input("Qual seu nome? ")
sexo = input("Qual seu sexo (m para masculino, f para feminino)? ").lower()
if sexo == 'm':
    print(f"Bom dia, senhor {nome}")
elif sexo == 'f':
    print(f"Bom dia, senhora {nome}")
else:
    print("Sexo inválido.")
