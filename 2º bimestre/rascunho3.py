"""
Dado uma Frase, verifique se esta mesta tem todas as letras do Alfabeto
"""
#------------------------- Criando variaveis ---------------------------
Texto = input("Informe um texto: ")
alf = "abcdefghijklmnopqrstuvywz"
total = 0
#------------------------- Criando variaveis ----------------------------
#------------------------- Primeira verifição ---------------------------
for letra in alf:
    if (letra in Texto) or (chr(ord(letra)- 32)in Texto):
        total = total + 1
print(total)
#------------------------- Primeira verifição -----------------------------
#------------------------- Segunda verifição ------------------------------
if total == 26:
    print ("É um programa!")
else:
    print ("Não é um programa!")
#------------------------- Segunda verifição -------------------------------