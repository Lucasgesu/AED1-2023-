"""
Escreva um programa que recebe uma frase do usuário e conta o número de palavras na frase
"""
#-------------------------- Criando Variaveis -------------------------------------------
frase = str(input("Digite uma frase:"))
cont = 0
quant = 1
#-------------------------- Criando Variaveis -------------------------------------------
#-------------------------- Loop --------------------------------------------------------
while cont < len(frase):
    cod = ord(frase[cont])
    if cod == 32:
        quant = quant + 1
    cont = cont + 1
#-------------------------- Loop --------------------------------------------------------
#-------------------------- Conclusão ---------------------------------------------------
print("Existem", quant, "Palavras")
#-------------------------- Conclusão ---------------------------------------------------