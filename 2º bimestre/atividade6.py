"""
Faça um programa em python que diga se uma senha digitada é fraca, média ou forte.
● Senha fraca: não possui caracteres especiais, nem letras maiúsculas.
● Senha média: possui letras minúsculas, números e caracteres especiais, mas não
possui letras maiúsculas.
● Senha forte: possui letras minúsculas/maiúsculas, números e caracteres especiais.
"""
#------------------------------- Criando Variaveis --------------------------------
senha = input("Escreva uma senha: ")
tamanho = len(senha)
minuscula = 0 
maiuscula = 0
numero = 0
especial = 0
cont = 0
#------------------------------- Criando Varíaveis --------------------------------
#------------------------------- Verificação (Senha fraca) ------------------------
while cont < tamanho:
    letra = senha[cont]
    cod = ord(letra)
    if cod >= 97 and cod <= 122:
        minuscula = minuscula + 1
#------------------------------- Verificação (Senha Fraca) ------------------------
#------------------------------- Verificação (Senha Média) ------------------------
    if cod >= 32 and cod <= 47 or cod >= 58 and cod <= 64 or cod >= 91 and cod <= 96 or cod >= 123 and cod <= 126:
        especial = especial + 1
    if cod >= 48 and cod <= 57:
        numero = numero + 1
#------------------------------- Verificação (Senha Média) ------------------------
#------------------------------- Verificação (Senha Forte) ------------------------
    if cod >= 65 and cod <= 90:
        maiuscula = maiuscula + 1
#------------------------------- Verificação (Senha Forte) ------------------------
#------------------------------- Contagem -----------------------------------------
    cont = cont + 1
#------------------------------- Contagem -----------------------------------------
#------------------------------- Verificação Final --------------------------------
if minuscula > 0 and maiuscula > 0 and especial > 0 and numero > 0:
    print("Senha Forte")
elif minuscula > 0 and especial > 0 and numero > 0:
    print ("Senha Média")
elif minuscula > 0 and numero > 0:
    print ("Senha Fraca")
elif tamanho == minuscula or tamanho == maiuscula or tamanho == numero or tamanho == especial:
    print("Senha Invalida") 
#------------------------------- Verificação Final --------------------------------