"""
Faça um programa em python que leia uma frase e passe para maiúscula a primeira letra
de cada palavra. Você não deve utilizar as funções prontas do python para converter
para maiúscula ou minúscula.
"""
#--------------------------- Criando variaveis -----------------------------------
frase = input("Escreva uma frase: ")
nova_frase = " "
palavra = " "
#--------------------------- Criando variaveis -----------------------------------
#--------------------------- Verificação -----------------------------------------
for letra in frase:
    if letra == " ":
        if palavra:
            primeira_letra = palavra[0]
            primeira_letra_maiuscula = chr(ord(primeira_letra)- 32)
            palavra = primeira_letra_maiuscula + palavra[1:]
            nova_frase += palavra + " "
            palavra = " "
    else:
        palavra += letra
#-------------------------- Verificação --------------------------------------------
#-------------------------- Segunda verificação ------------------------------------
if palavra:
    primeira_letra = palavra[0]
    primeira_letra_maiuscula = chr(ord(primeira_letra)- 32)
    palavra = primeira_letra_maiuscula + palavra[1:]
    nova_frase += palavra
#-------------------------- Segunda verificação ------------------------------------
#-------------------------- Conclusão ----------------------------------------------
print(nova_frase)
#-------------------------- Conclusão ----------------------------------------------