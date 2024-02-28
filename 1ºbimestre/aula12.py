#Escreva um programa que mostre a seguinte sequência de números para um valor N informado pelo usuário:
N = int(input("Escreva um número: "))
numero_atual = 1

while numero_atual <= N:
    linha = 1
    while linha <= numero_atual:
        print (numero_atual, end="")
        linha = linha + 1
    print ()
    numero_atual = numero_atual + 1
whil