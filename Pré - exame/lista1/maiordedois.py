"""
algoritmo que apresente o maior de dois números introduzidos por teclado
"""
a = int(input("Digite um número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    print("O maior número é:", a)
elif b > a:
    print("O maior número é:", b)
else:
    print("Os número são iguais")