#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
import math 

area = float(input("Digite o tamanho da area a ser pintada: "))

t = (area / 6) * 1.1

latas = math.ceil(t / 18)

p = latas * 80 

g = math.ceil(t / 3.6)

pg = g *25

lm = math.floor(t / 18)

tr = t - (lm * 18)

gm = math.ceil(tr / 3.6)

pm= (lm * 80) + (gm * 25)

print(f"Comprar apenas latas de 18L: {latas} latas, preço: R$ {p:.2f}")
print(f"Comprar apenas galões de 3,6L: {g} galões, preço: R$ {pg:.2f}")
print(f"Misturar latas e galões: {lm} latas e {gm} galões, preço: R$ {pm:.2f}")