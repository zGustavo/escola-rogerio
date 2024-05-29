velocidade_permitida = int(input("Qual a velocidade permitida na via: "))
velocidade_motorista = int(input("Quala a velocidade do motorista: "))

if velocidade_motorista > velocidade_permitida:
    if(velocidade_motorista > (velocidade_permitida * 0.5) + velocidade_permitida):
        print("INFRAÇÃO GRAVÍSSIMA! R$ 574,00 + 7 PONTOS + APREENSÃO DA CARTEIRA + SUSPENSÃO DO DIREITOR DE DIRIGIR")
    elif(velocidade_motorista > (velocidade_permitida * 0.2) + velocidade_permitida):
        print("INFRAÇÃO GRAVE! R$ 127,00 + 5 PONTOS")
    else:
        print("INFRAÇÃO MÉDIA! R$ 85,00 + 4 PONTOS")
else:
    print("TUDO CERTO! VOCÊ ESTÁ DENTRO DO LIMITE")
