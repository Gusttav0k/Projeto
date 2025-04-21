#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
 
h = float(input("Quanto vc ganha por hora: "))
s = float(input("Quantas horas trabalhada no mês: "))

bruto = h * s

#A)salário bruto. 
r = round(bruto, 2) 
print("Seu salario bruto é",bruto,"R$")

#B)quanto pagou ao INSS.

d1 = 8
inss = bruto - (bruto * d1 / 100) 
p1 = bruto - inss
r2 = round(p1, 2) 
print("O valor pago no inss ",p1,"R$")

#C)quanto pagou ao sindicato.

d2 = 5
sindicato = bruto - (bruto * d2 / 100) 
p2 = bruto - sindicato
r3 = round(p2, 2) 
print("O valor pago no sindicato:",p2,"R$")

#D)escontados 11% para o Imposto de Renda.

d3 = 11
ir = bruto - (bruto * d3 / 100) 
p3 = bruto - ir
r4 = round(p3, 2) 
print("O valor pago no imposto de renda:",r4,"R$")

liquido = bruto - (p1 + p2 + p3)
r5 = round(liquido, 2 )

print("Seu salario liquido é",r5,"R$" )