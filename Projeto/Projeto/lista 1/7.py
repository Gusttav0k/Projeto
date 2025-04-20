#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

s = float(input("Quanto vc ganha por hora:"))
h = float(input("Quantas horas vc trabalhou: "))

salario = s * h 
print(f"O total do seu salario do mes é: R${salario:.2f}")