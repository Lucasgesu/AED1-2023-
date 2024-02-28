"""
Escreva um programa que recebe uma string do usuário e imprime a string invertida
"""
#--------------------------- Criando variaveis ----------------------------------
frase = str(input("Escreva uma frase:"))
cont = -1
frase_invertida = ""
tamanho = len(frase) - len(frase) - len(frase)
#---------------------------- Criando variaveis ----------------------------------
#---------------------------- Verificação ----------------------------------------
while cont >= tamanho:
    letra = frase[cont]
    cor = ord(letra)
    frase_invertida = frase_invertida + letra
    cont = cont - 1
#---------------------------- Verificação ------------------------------------------
#---------------------------- Conclusão --------------------------------------------
print(frase_invertida)
#---------------------------- Conclusão --------------------------------------------