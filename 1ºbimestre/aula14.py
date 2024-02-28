# Escreva um programa que receba um número inteiro positivo do usuário e verifique se ele é primo.
N = int(input("Informe um número: "))
if N <= 0:
    print ("Valor invalido")
else:
    cont = 1
    total = 0
while cont < N:
    if N % cont == 0:
        total += 1
    cont += 1
if total > 1:
    print ("Não é primo")
else:
    print ("é primo")