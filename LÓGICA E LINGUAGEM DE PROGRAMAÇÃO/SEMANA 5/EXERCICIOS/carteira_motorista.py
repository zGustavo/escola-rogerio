idade = int(input("Qual sua idade: "))
exameMedico = input("Você fez exame médico? (S/N): ")

if exameMedico == 's':
  exameMedico = True
else:
  exameMedico = False

violacao = input("Já cometeu alguma infração de transito? (S/N): ")

if violacao == 's':
  violacao = True
elif violacao == 'n':
  violacao = False
else:
  print("Dados incorretos")

if idade >= 18 and exameMedico and not violacao:
  print("Você pode solicitar sua carteira de motorista")
else:
  print("Você não pode solicitar sua carteira de motorista")