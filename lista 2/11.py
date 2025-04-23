#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 

a = str(input("Qual turno voce estuda: ")).lower()

if a == "m":
    print("BOM DIA")
elif a == "v":
    print("BOA TARDE")
elif a == "n":
    print("BOA NOITE")
else:
    print("VALOR INVALIDO")