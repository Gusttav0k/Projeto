#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

#A) Para homens: (72.7*h) - 58 

h = float(input("Digite sua aultura; "))

p1 = (72.7*h) - 58 
r = round(p1,2)

print("O peso ideal masculina é",r)

#B) Para mulheres: (62.1*h) - 44.7 

p2 = (62.1*h) - 44.7 

r2 = round(p2,2)

print("O peso ideal feminino é",r2)