# 0 1 2 3 4 5 6
#  A U G U S T O
X = input("Digite a palavra")
tamanho = len(X) #Função que retorna o tamanho da string
print(X, tamanho)
cont = 0 #indice de string
while cont < tamanho:
    if X[cont] == "a" or X[cont] == "e" or X[cont] == "i" or X[cont] == "o" or X[cont] == "u":
        print(cont,X[cont], "(vogal)")
    else:
        print(cont,X[cont])
    cont = cont + 1
