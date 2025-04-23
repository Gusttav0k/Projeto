#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 

a  = float(input("Qual é o valor do primeiro produto: "))
b  = float(input("Qual é o valor do segundo produto: "))
c  = float(input("Qual é o valor do terceiro produto: "))

barato = min (a, b, c, )

print("O produto que voce deve comprar é",barato)
