#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 

m = int(input("Digite o tamanho do arquivo em MB:"))
v = float(input("Agora fala a velocidade da internet em mbps:"))

t = m * 8
d = t / v
resultado = d / 60

arredondado = round(resultado,2)


print("O tempo de espera para o download e de",arredondado,"minutos")