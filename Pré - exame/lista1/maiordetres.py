"""
Faça um algoritmo que apresente o maior de três números introduzidos por teclado. Obs.: os três números
introduzidos são diferentes entre si).
"""
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número:"))

if a > b and a > c:
    print("O maior número é:", a)
elif b > a and b > c:
    print("O maior número é:", b)
elif c > a or c > b:
    print("O maior número é:", c)
else:
    print("Todos números são iguais")