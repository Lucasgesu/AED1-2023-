"""
Faça um programa em python que leia uma frase e a passe para maiúscula. Você não
deve utilizar as funções prontas do python para converter para maiúscula ou minúscula
"""
#------------------------Criando variaveis -----------------------
frase = str(input("Escreva uma frase:"))
cont = 0
frase_atualizada = ""
#-------------------------Criando variaveis -------------------------
#------------------------- Loop e verificação -----------------------
while cont <len(frase):
    letra = frase[cont]
    cod = ord(letra)
    if cod >= 65 and cod <= 90 or cod == 32:
        frase_atualizada = frase_atualizada + letra
    else:
        cod = cod - 32
        letra = chr(cod)
        frase_atualizada = frase_atualizada + letra
#------------------------ Lopp e verificação -------------------------
#------------------------ Conclusão ----------------------------------
cont = cont + 1
print(frase_atualizada)
#------------------------ Conclusão -----------------------------------