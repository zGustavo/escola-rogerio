best_seller = True
lancado_ha_2_anos = False
quantidade_livros = 4
preco_livro = 50
desconto = 0

if best_seller or lancado_ha_2_anos:
  desconto += 20
  if quantidade_livros > 3:
    desconto += 5

preco_final = preco_livro * (1 - desconto / 100) * quantidade_livros

print(f"O preço final após os descontos é de R${preco_final:.2f}.")