# Escreva um programa que receba duas listas do usuário e retorne uma nova lista
#contendo apenas os elementos comuns entre as duas listas.
#-----------------------------Criando Variaveis--------------------------------
lista1 = [4, 'Lucas', 5, 'John',  12, 'Augusto', 16, "Wendel", 32, 'Pablo' ]
lista2 = [4, 'Fernada', 7, 'Lucas', 9, 'Claudio', 12, 'Guilherme', 15, 'Augusto']
#-----------------------------Criando Variaveis--------------------------------
#------------------------------Verificação-------------------------------------
lista3 = [nome and valor for nome and valor in lista1 and lista2]
#------------------------------Verificação-------------------------------------