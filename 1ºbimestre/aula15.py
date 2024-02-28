#) Escreva um programa que receba um número inteiro positivo do usuário e verifique se ele é primo.

N = int(input("Quantos termos você quer mostrar?"))
t1 = 0
t2 = 1
cont = 0
while cont < N: 
    print(cont, end=',')
    cont = t1 + t2
    t2 = t1
    t1 = cont
print(N)
 in

