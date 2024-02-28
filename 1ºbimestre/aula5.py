#Faça um programa em python que leia 3 números e os mostre em ordem crescent
A = float(input("Digite um número:"))
B = float(input("Digite um número: "))
C = float(input("Digite um número:"))
if 
if A <= B and A <= C:
    
    menor = A
    if B <= C:
        meio = B
        maior = C
    else:
        meio = C
        maior = B
if B <= A and B <= C:
    menor = B
    if A <= C:
        meio = A
        maior = C
    else:
        meio = C
        maior = A
else:
    menor = C
    if A <= B:
        meio = A
        maior = B
    else:
        meio = B
        maior = A

print ("Os números em ordem crescente são:", menor, meio, maior)