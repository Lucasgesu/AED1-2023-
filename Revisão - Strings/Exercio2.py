#Escreva um programa que receba uma lista de números e retorne uma nova lista
#contendo apenas os números pares.
#----------------------------------Criando Variaveis-------------------------
lista_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_pares = []
#----------------------------------Criando Variaveis-------------------------
#----------------------------------Verificação-------------------------------
for valor in lista_num:
    if valor %2 == 0: # % = resto da divisão
        num_pares.append(valor) #Append = adiciona valor ao uma nova lista
#----------------------------------Verificação-------------------------------
print(num_pares)