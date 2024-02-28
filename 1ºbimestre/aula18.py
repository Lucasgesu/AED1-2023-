#Escreva um programa que leia diversos funcionários e seu respectivo salario, ate que o nome de um funcionário seja “fim"
cont = 0
maior_sal = 0
menor_sal = 0
soma_salarios = 0


while True:
    nome = input("digite um nome de funcionário (obs: fim termina): ")

    if nome == "fim" or "FIM" :
        break

    salario = float(input("Informe o salário: "))

    if salario > maior_sal:
        maior_sal = salario
        nome_maior = nome

    if salario < menor_sal:
        menor_sal = salario
        nome_menor = nome

    soma_salarios += salario
    cont += 1

media_salario = soma_salarios   / cont



print("o funcionário com maior salário:", nome_maior, maior_sal, "REAIS")
print ("o funcionário com menor salário:", nome_menor, menor_sal, "REAIS")
print ("a média de salário:", media_salario, "REAIS")





