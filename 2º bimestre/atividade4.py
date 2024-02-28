"""
Escreva um programa que recebe uma string do usuário e imprime a string com todas as
letras maiúsculas convertidas para minúsculas e vice-versa.
"""
#------------------------------- Criando Variaveis ---------------------------------------------------------
frase = str(input("Escreva uma frase: "))
cont = 0
frase_nova = " "
#------------------------------- Criando Variaveis ---------------------------------------------------------
#------------------------------- Loop ----------------------------------------------------------------------
while cont <= len(frase):
    letra = frase[cont]
    cod = ord(letra)
    if cod == 32:
        frase_nova = frase_nova + letra
    else:
        if cod >= 65 and cod <= 90:
            cod = cod + 32
            letra = chr(cod)
            frase_nova = frase_nova + letra
        else:
            cod = cod - 32
            letra = chr(cod)
            frase_nova = frase_nova + letra
#------------------------------- Loop -----------------------------------------------------------------------
#------------------------------- Verificação e conclusão ----------------------------------------------------
cont = cont + 1
print(frase_nova)
#------------------------------- Verificação e conclusão ----------------------------------------------------