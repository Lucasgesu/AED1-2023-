x = 0
y = 0
tabuada = 100
saida =""
while y <= tabuada:
    saida = saida + str(x*y)
    x = x + 1

    while x <= tabuada:
        saida = saida + ';' + str(x*y)
        x = x + 1
    saida = saida + "\n"
    x = 1
    y = y + 1

arq = open("tabuada.csv", "w")
arq.write(saida)
arq.close()