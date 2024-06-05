# Leitura do nome do mês
print("Digite um mês:")
mes = input()

# Normalizando a entrada para letras minúsculas
mes = mes.lower()

# Verificação e impressão do número de dias
if mes == "janeiro":
    print(mes + " tem 31 dias.")
elif mes == "fevereiro":
    print(mes + " tem 28 ou 29 dias.")
elif mes == "março":
    print(mes + " tem 31 dias.")
elif mes == "abril":
    print(mes + " tem 30 dias.")
elif mes == "maio":
    print(mes + " tem 31 dias.")
elif mes == "junho":
    print(mes + " tem 30 dias.")
elif mes == "julho":
    print(mes + " tem 31 dias.")
elif mes == "agosto":
    print(mes + " tem 31 dias.")
elif mes == "setembro":
    print(mes + " tem 30 dias.")
elif mes == "outubro":
    print(mes + " tem 31 dias.")
elif mes == "novembro":
    print(mes + " tem 30 dias.")
elif mes == "dezembro":
    print(mes + " tem 31 dias.")
else:
    print("Mês inválido.")
