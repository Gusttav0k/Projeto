#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

print(f"A data é {dia}/{mes}/{ano}")

if mes < 1 or mes > 12:
    print("Mês inválido!")
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia > 0 and dia <= 31:
        print("Data válida")
    else:
        print("Dia inválido")
elif mes in [4, 6, 9, 11]:
    if dia > 0 and dia <= 30:
        print("Data válida")
    else:
        print("Dia inválido")
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if dia > 0 and dia <= 29:
            print("Data válida (ano bissexto)")
        else:
            print("Dia inválido para fevereiro em ano bissexto")
    else:
        if dia > 0 and dia <= 28:
            print("Data válida")
        else:
            print("Dia inválido para fevereiro")

        