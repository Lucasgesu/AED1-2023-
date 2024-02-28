"""
Faça um programa em python que:
● Crie uma senha aleatória de 6 caracteres alfanuméricos (A..Z,0..9);
● Descubra a senha criada (força bruta - tentar todas possibilidades). Obs: para
encontrar a senha, você não pode comparar pedaços da senha, precisa comparar
toda senha (ex: if senha_gerada==senha_tentada: ).
"""
#---------------------- Criando Variaveis --------------------------------------
import random
senha_gerada = " "
cont = 0
moeda = 0
senha1 = " "
senha2 = " "
senha_tentada = " "
#---------------------- Criando Variaveis --------------------------------------
#---------------------- Loop 1 -------------------------------------------------
while len(senha_gerada) <= 3:
    if moeda == 1:
        for letra in senha_gerada:
            letra = str(random.randint(0,9))
            senha1 = senha1 + letra
            if cont <= 3:
                break
    else:
        for letra in senha_gerada:
            letra = chr(random.randint(ord("a"), ord("z")))
            senha1 = senha1 + letra
            if cont <= 3:
                break
    moeda = random.randint(1,2)
    cont = cont + 1
    senha_gerada = senha_gerada + "1"
print ("A senha é: {senha1}")
#---------------------- Loop 1 -------------------------------------------------
#---------------------- Loop 2 -------------------------------------------------
while senha1 != senha2:
    while len(senha_tentada) <= 3:
        if moeda == 1:
            for letra in senha_tentada:
                letra = str(random.randint(0,9))
                senha2 = senha2 + letra
                if cont <= 3:
                    break
        else:
            for letra in senha_tentada:
                letra = chr(random.randint(ord("a"), ord("z")))
                senha2 = senha2 + letra
                if cont <= 3:
                    break
        moeda = random.randint(1,2)
        cont = cont + 1
        senha_tentada = senha_tentada + "1"
    print("Decifrando senha: {senha2}")
#---------------------- Loop 2 -------------------------------------------------
#---------------------- Conclusão ----------------------------------------------
print("Senha Descorberta: {senha1}")
#---------------------- Conclusão ----------------------------------------------