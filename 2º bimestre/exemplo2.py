palavra = input("Digite a palavra:")
for letra in palavra:
    if letra == "a" or letra == "e" or letra == "i"  or letra == "o" or letra == "u":
        print(letra, "(vogal)")
    else:
        print(letra)
"""
tamanho = len(X) #Função que retorna o tamanho da string
print(X, tamanho)
cont = 0 #indice de string
while cont < tamanho:
    if X[cont] == "a" or X[cont] == "e" or X[cont] == "i" or X[cont] == "o" or X[cont] == "u":
        print(cont,X[cont], "(vogal)")
    else:
        print(cont,X[cont])
    cont = cont + 1
"""