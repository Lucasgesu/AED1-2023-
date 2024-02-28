"""
LEIA UMA PALAVRA EM QUE USUÁRIO INFORME E VEJA SE INVERSO DESSA PALAVRA É PALÍNDROMO
"""
#--------------Declarando variaveis -------------------------------------------------------------
palavra = input("Escreva uma palavra: ")
inverso = ""
tamanho = len(palavra)
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