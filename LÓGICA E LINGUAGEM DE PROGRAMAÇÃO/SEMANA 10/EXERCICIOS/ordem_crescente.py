primeiro_numero = float(input("Informe o primeiro número: "))
segundo_numero = float(input("Informe o primeiro número: "))
terceiro_numero = float(input("Informe o primeiro número: "))

#Compara e ordena os números informados
if(primeiro_numero <= segundo_numero and primeiro_numero <= terceiro_numero):
  menor = primeiro_numero
  if (segundo_numero <= terceiro_numero):
    medio = segundo_numero
    maior = terceiro_numero
  else:
    medio = terceiro_numero
    maior = segundo_numero
elif (segundo_numero <= primeiro_numero and segundo_numero <= terceiro_numero):
  menor = segundo_numero
  if (primeiro_numero <= terceiro_numero):
    medio = primeiro_numero
    maior = terceiro_numero
  else:
    medio = terceiro_numero
    maior = primeiro_numero
else:
  menor = terceiro_numero
  if (primeiro_numero <= segundo_numero):
    medio = primeiro_numero
    maior = segundo_numero
  else:
    medio = segundo_numero
    maior = primeiro_numero

# Mostra os números em ordem crescente

print(f"Os números em ordem crescente {menor}, {medio}, {maior}")
