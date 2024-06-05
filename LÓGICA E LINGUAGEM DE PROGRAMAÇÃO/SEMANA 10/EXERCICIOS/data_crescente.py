# leitura da primeira data
dia1 = int(input('Informe o dia da primeira data: '))
mes1 = int(input('Informe o mês da primeira data: '))
ano1 = int(input('Informe o ano da primeira data: '))

# Leitura da segunda data
dia2 = int(input('Informe o dia da segunda data: '))
mes2 = int(input('Informe o mês da segunda data: '))
ano2 = int(input('Informe o ano da segunda data: '))

# Comparação das datas
if ano1 < ano2:
    print(str(dia1) + "/" + str(mes1) + "/" + str(ano1) + ", " + str(dia2) + "/" + str(mes2) + "/" + str(ano2))
elif ano1 > ano2:
    print(str(dia2) + "/" + str(mes2) + "/" + str(ano2) + ", " + str(dia1) + "/" + str(mes1) + "/" + str(ano1))
else:  # anos são iguais
    if mes1 < mes2:
        print(str(dia1) + "/" + str(mes1) + "/" + str(ano1) + ", " + str(dia2) + "/" + str(mes2) + "/" + str(ano2))
    elif mes1 > mes2:
        print(str(dia2) + "/" + str(mes2) + "/" + str(ano2) + ", " + str(dia1) + "/" + str(mes1) + "/" + str(ano1))
    else:  # meses são iguais
        if dia1 < dia2:
            print(str(dia1) + "/" + str(mes1) + "/" + str(ano1) + ", " + str(dia2) + "/" + str(mes2) + "/" + str(ano2))
        else:
            print(str(dia2) + "/" + str(mes2) + "/" + str(ano2) + ", " + str(dia1) + "/" + str(mes1) + "/" + str(ano1))
