#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 

a = float(input("Digite sua altura: "))

p = (72.7 * a) - 58

r = round(p,2)

print("Seu peso ideal é",r)