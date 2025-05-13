#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

from math import *

a = float(input("Digite o valor A:"))

if a == 0:
    print("Não é uma equação do segundo grau. Encerrando o programa.")
else:
    b = float(input("Digite o valor B:"))
    c = float(input("Digite o valor C:"))

    delta = b ** 2 - 4 * a * c 
    
    if delta < 0 :
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"A equação possui apenas uma raiz real: x = {x}")
        
    elif delta > 0:
        r = sqrt(delta)

        x1 = (-b + r) / (2 * a)
        x2 = (-b - r) / (2 * a)

        print(f"A equação possui duas raízes reais: x1 = {x1} e x2 = {x2}")





