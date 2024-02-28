#--------------------------------- Criando Variaveis ---------------------------------
nome = "AnDRé PrISco DE VARgas"
conectivos = ["da", "de", "do", "dos", "das,", "dos"]
lista = nome.split (" ")
print (lista)
saida = " "
#--------------------------------- Criando variaveis ----------------------------------
#--------------------------------- Loop -----------------------------------------------
for parte in lista[0:-1]:
    if parte.lower() in conectivos:
        saida = saida + parte.capitalize() + " "
    else:
        saida = saida + parte.capitalize() + " "
#-------------------------------- Lopp -------------------------------------------------
#-------------------------------- Conclusão --------------------------------------------
saida = saida + lista[-1].capitalize()
print(saida)
#-------------------------------- Conclusão --------------------------------------------