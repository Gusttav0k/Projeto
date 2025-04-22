#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

a = str(input("Digite uma letra: ")).lower()

l = ["a","e","i","o","u"]

if a in l:
    print("É uma vogal")
else:
    print("E uma cosoante ")