#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas. 

kg = float(input("Digite o valor do peso: "))

if kg > 50:
     a = kg - 50 
     r = round(a ,2)
     print("O excesso de peso e de",r,"Kg")
     t = r * 4
     r2 = round(t, 3)
     print("O total de multa por excesso de carga é:",r2,"R$")
else :
     print("O peso esta de acordo com o regulamento de pesca do estado de São Paulo ")