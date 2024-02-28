#------------------- criando variavel ---------------------------
palavra = input("Escreva uma palavra: ")
inverso = ""
tamanho = len(palavra) - 1 # o -1 serve para pegar o ultimo caracter pois na programacao nao começa em 0
# ---------------------- criando variavel ----------------------

# ------------------------ loop -----------------
while tamanho >= 0:
    inverso = inverso + palavra[tamanho]
    tamanho = tamanho - 1
print(inverso)
# ------------------------ loop ------------------

# ------------------------ verificação ------------------
if palavra == inverso:
    print(inverso, "a palavra é palíndromo")
else:
    print(inverso, "não é palíndromo")
# ------------------------ verificação ------------------
