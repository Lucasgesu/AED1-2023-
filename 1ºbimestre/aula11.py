#Escreva um programa que mostre a tabuada (0 a 10) de um número fornecido pelo usuário
x = int(input("informe um número:"))
cont = 0
while cont <= 10:
    resp = cont * x
    print(x,  cont, '*=', resp)
    cont = cont + 1
    