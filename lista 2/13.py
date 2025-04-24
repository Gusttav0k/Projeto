#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. 

v = float(input("Digite o valor da sua hora:"))
h = float(input("Digite a quantidade de horas trabalhadas:"))

sb = v * h

def ir(sb):
    if sb <= 900:
        return 0
    elif sb <= 1500:
        return sb * 0.05
    elif sb <= 2500:
        return sb * 0.10
    else:
        return sb * 0.20
    
r = ir(sb)

s = sb * 0.03

fgts = sb * 0.11

sl = sb - r - s

print("\nSalário Bruto     : R$", round(sb, 2))
print("(-) IR            : R$", round(r, 2))
print("(-) Sindicato     : R$", round(s, 2))
print("FGTS              : R$", round(fgts, 2))
print("Salário Líquido   : R$", round(sl, 2))
