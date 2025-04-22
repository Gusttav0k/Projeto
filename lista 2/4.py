#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 

a = str(input("Digite seu sexo 'M' ou 'F':"))

if  a == "M" :
    print("O seu sexo e MASCULINO")
elif a == "F":
    print("O sexo e Feminino")
else:
    print("sexo desconheido ")
       
     