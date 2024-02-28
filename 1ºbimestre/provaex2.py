#Crie um programa em Python que imprima uma sequência de números
#em forma de pirâmide. O programa deve solicitar ao usuário um número inteiro
#positivo e, em seguida, imprimir os números de 1 até o número informado, em linhas
#crescentes e decrescentes, formando uma pirâmide.

N = int(input("Escreva um número: "))
numero_atual = 1

while numero_atual <= N:
    linha = 1
    while linha <= numero_atual:
        print (numero_atual, end="")
        linha = linha + 1
    print ()
    numero_atual = numero_atual + 1
