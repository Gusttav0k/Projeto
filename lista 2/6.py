#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

n1 = float(input("Digite a noto da n1:"))
n2 = float(input("Digite a noto da n2:"))

m = (n1 + n2) / 2
R = round(m, 1)

if R >= 7 and R <= 9.9:
    print("APROVADO!")
elif R == 10:
    print("APROVADO COM DISTINÇÃO!")
else:
    print("REPROVADO!")
     