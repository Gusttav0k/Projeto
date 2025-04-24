#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

#1)Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual: 

s = float(input("Digite seu salario: "))

if s <= 280:
    aumento = (20 / 100) * s
    salario = s + aumento
    print("Seu aumento é de",aumento)
    print("Seu salario é",salario)
elif s > 280 and s < 700:
    aumento = ( 15/ 100) * s
    salario = s + aumento
    print("Seu aumento é de",aumento)
    print("Seu salario é",salario)
elif s > 700 and s < 1500:
    aumento = ( 10 / 100) * s
    salario = s + aumento
    print("Seu aumento é de",aumento)
    print("Seu salario é",salario)
elif s > 1500:
    aumento = ( 5 / 100) * s
    salario = s + aumento
    print("Seu aumento é de",aumento)
    print("Seu salario é",salario)
