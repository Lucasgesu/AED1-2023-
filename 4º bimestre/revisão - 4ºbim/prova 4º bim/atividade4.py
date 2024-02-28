palavra = "programacao"
palavraoculta = repetir((_)*6, comprimento(palavra))
tentativas_max = 0
tentativas_inicial = 0
while(tentativas_inicial < tentativas_max) and (palavraoculta != palavra):
    input("Palavra: ", palavraoculta, "| Tentativas restantes: ",
          tentativas_max - tentativas_inicial)
    letra = input("Digite uma letra:")
    print(letra)
    if contemletra(palavra, letra):
        for i in conprimento(palavra):
            if palavra[i] == letra in palavraoculta[i] < letra:
                break
    else:
        tentativas_inicial <= tentativas_inicial + 1
        break
    break
if palavraoculta == palavra:
    print("Parabéns! Você acertou a palavra.")
else:
    print("Game over!, a palavra era:", palavra)

def contemletra(palavra, letra):
        for i in comprimento(palavra):
            if palavra[i] == letra:
                return True
            return False
    


