"""
Faça um programa em python que leia uma frase e passe para maiúscula a primeira letra
de cada palavra. Você não deve utilizar as funções prontas do python para converter
para maiúscula ou minúscula.
"""
#---------------------------- Criando Variaveis ------------------------------------
frase_inicial = str(input("Escreva uma frase:"))
nova_frase = " "
palavra = " "
#---------------------------- Criando Variaveis ------------------------------------
#--------------------------- Verificação -------------------------------------------
for letra in frase_inicial:
    if letra == " ":
        if palavra:
            primeira_letra = palavra[0]
            primeira_letra_maiscula = chr(ord(primeira_letra) - 32)
            palavra = primeira_letra_maiscula + palavra[1: -1]
            nova_frase = nova_frase + palavra + " "
            palavra = " "
#--------------------------- Verificação -------------------------------------------
#--------------------------- Segunda Verificação -----------------------------------
    else:
        palavra = palavra + letra
        if palavra:
            primeira_letra = palavra[0]
            primeira_letra_maiscula = chr(ord(primeira_letra) - 32)
            palavra = primeira_letra_maiscula + palavra[1:-1]
            nova_frase = nova_frase + palavra 
#------------------------- Segunda Verificação --------------------------------------
#------------------------- Conclusão ------------------------------------------------
print(nova_frase)
#------------------------ Conclusão -------------------------------------------------