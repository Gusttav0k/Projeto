#Faça um Programa que leia três números e mostre-os em ordem decrescente. 

a  = float(input("Qual é o numero: "))
b  = float(input("Qual é o numero: "))
c  = float(input("Qual é o numero: "))

numeros = [a, b, c, ]

ordem = sorted(numeros, reverse=True)

print(ordem)