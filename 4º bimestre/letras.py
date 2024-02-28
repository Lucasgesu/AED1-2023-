def calcfrequencia(texto):
    contletras = {}

    for char in texto.lower():

        if char.isalpha():
            contletras[char] = contletras.get(char, 0) + 1

    maxcontagem = max(contletras.values())

    letrasmaisfrequentes = [letra for letra, contagem in contletras.items() if contagem == maxcontagem]

    letrasmaisfrequentes.sort()

    return letrasmaisfrequentes


numeroscasosteste = int(input())

for _ in range(numeroscasosteste):
    linha_texto = input()

    resultado = calcfrequencia(linha_texto)
    print("".join(resultado))