nome = "Alice"
idade = 25
e_estudante = True
esta_empregado = False

if idade >= 18 and e_estudante:
    status = "adulto e estudante"
elif idade >= 18 and esta_empregado:
    status = "adulto e empregado"
elif idade < 18:
    status = "menor de idade"
else:
    status = "adulto"

mensagem = f"Olá, {nome}. Você é {status}."
print(mensagem)
