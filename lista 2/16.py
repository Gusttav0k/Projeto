#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

a = float(input("Iforme um lado do triangulo: "))
b = float(input("Iforme um lado do triangulo: "))
c = float(input("Iforme um lado do triangulo: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("É um triângulo")
    
    if a == b == c:
        print("É um Equilátero")
    elif a == b or b == c or a == c:
        print("O triângulo é Isósceles")
    else:
        print("O triângulo é Escaleno")
else:
    print("Não é um triângulo.")
