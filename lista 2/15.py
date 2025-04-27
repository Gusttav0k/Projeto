#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

m = (n1 + n2) / 2

print(f"\nNota 1: {n1}")
print(f"Nota 2: {n2}")
print(f"Média: {m}")

if m >= 9.0 and m <= 10.0:
    print("Conceito: A (APROVADO)")
elif m >= 7.5 and m < 9.0:
    print("Conceito: B (APROVADO)")
elif m >= 6.0 and m < 7.5:
    print("Conceito: C (APROVADO)")
elif m >= 4.0 and m < 6.0:
    print("Conceito: D (REPROVADO)")
elif m >= 0 and m < 4.0:
    print("Conceito: E (REPROVADO)")
else:
    print("Notas inválidas!")


    
    