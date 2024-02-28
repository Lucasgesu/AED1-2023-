"""
Dado uma Frase, verifique se esta mesta tem todas as letras do Alfabeto
"""
#-------------------------- Criando variaveis ----------------------------
Frase = str(input("Escreva uma frase:"))
letra = 65
Alfabelto = True
#-------------------------- Criando variaveis ----------------------------
#-------------------------- Primeira Verificação ----------------------------------
while letra <= 90:
    if chr(letra) in frase:
        Alfabelto = True
        letra = letra + 1        
    else:
        Alfabelto = False
        letra = 0
#--------------------------- Primeira Verificação ------------------------------------
#--------------------------- Segunda Verificação -------------------------------------
if Alfabelto == True:
    print("Parabéns, tem todo o alfabeto")
else:
    print("Que pena, falta algumas letras")
#--------------------------- Segunda Verificação -------------------------------------