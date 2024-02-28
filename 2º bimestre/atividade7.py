"""
 Escreva um programa em python que leia um texto e diga se é ou não um palíndromo
(ou seja, se o inverso da string é igual a ela). Não será possível utilizar qualquer função
no python que trabalhe com strings.
Exemplos:
Ama
Mirim
A grama é amarga
"""
#--------------Declarando variaveis -------------------------------------------------------------
palavra = input("Escreva uma palavra: ")
inverso = ""
tamanho = len(palavra) - 1
#--------------Declarando variaveis --------------------------------------------------------------
#--------------Loop-------------------------------------------------------------------------------
while tamanho >= 0:
    inverso = inverso + palavra[tamanho]
    tamanho = tamanho - 1
print(inverso)
#--------------Loop-------------------------------------------------------------------------------
#--------------Verifição--------------------------------------------------------------------------
if palavra == inverso:
    print(inverso, "a palavra é palíndromo")
else:
    print(inverso, "não é palíndromo")
#--------------Verifição--------------------------------------------------------------------------
