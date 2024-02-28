def inverte():
    with open("exemplo.txt", "r") as arq:
        palavra = ""
        cont = -1
        frase_invertida = ""
        tamanho = len(palavra) - len(palavra) - len(palavra)
    while cont >= tamanho:
        letra = palavra[cont]
        cor = ord(letra)
        frase_invertida += letra
        cont -= 1
    
    inverte("exemplo.txt")