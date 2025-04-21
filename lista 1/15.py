#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math

l = float(input("Digite o tamanho em metros quadrados da área a ser pintada:  "))

t  = l / 3

latas = math.ceil (t / 18)

p = latas * 80 
r = round(p, 2)

print("Essa e a quantidade de latas",latas,"e a preço",r,"R$")