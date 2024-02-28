"""
Faça um programa em python que leia uma frase e a passe para maiúscula. Você não
deve utilizar as funções prontas do python para converter para maiúscula ou minúscula.
"""
#------------------------------- Criando Variaveis -----------------------------------
frase_inicial = str(input("Escreva uma Frase: "))
maiúscula = " "
#------------------------------- Criando Variaveis -----------------------------------
#------------------------------- Loop ------------------------------------------------
for letra in frase_inicial:
    if ord(letra) >= 97 and ord(letra) <= 122:
        maiúscula = maiúscula + chr(ord(letra) - 32)
    else:
        maiúscula = maiúscula + letra
#------------------------------- Loop ------------------------------------------------
#------------------------------- Conclusão -------------------------------------------
print(maiúscula)
#------------------------------- Conclusão -------------------------------------------
