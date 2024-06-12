# tabela de gastos
gasto_medio_bebidas = 80
gasto_medio_comida = 60
gasto_medio_transporte = 15

# coleta de informações
print('Você planeja beber? (S/N)')
resposta_bebida = input().strip().upper()

print('Você planeja comer? (S/N)')
resposta__comida = input().strip().upper()

print('Você planeja utilizar transporte? (S/N)')
resposta_transporte = input().strip().upper()

print("Quantas pessoas sairão com você?")
numero_pessoas = int(input().strip())

# inicializa variavel de gastos total
gasto_medio = 0

# calculando os gastos com base nas respostas
if resposta_bebida == 'S':
  gasto_medio += gasto_medio_bebidas

if resposta__comida == 'S':
  gasto_medio += gasto_medio_comida

if resposta_transporte == 'S':
  gasto_medio += gasto_medio_transporte

# multiplicando o gasto médio pelo total de número de pessoas (incluindo o usuário)
gasto_medio *= (numero_pessoas + 1)

# exibe o gasto médio estimado
print(f"O gasto médio estimado é R${gasto_medio}")