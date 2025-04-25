#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

n1 = float(input("Digite a nota:"))
n2 = float(input("Digite a nota:"))

m = (n1 + n2) / 2


if m > 9 and m <= 10:
     print("A (APROVADO)")
elif m > 7.5 and m <= 9:
    print("B (APROVADO)")
elif m > 6 and m <= 7.5:
    print("C (APROVADO)")
elif m > 4 and m <=6:
    print("D (REPROVADO)")
elif m > 0 and m <= 4:
    print("E (RPROVADO)")
    


    
    