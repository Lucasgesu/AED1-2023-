import sys

sys.setrecursionlimit(20000)
casos = int(input(""))
cont = 0

def josp(meliante, pulo):
    if meliante > 1:
        return((josp(meliante - 1,pulo) + pulo - 1)% meliante) + 1
    else:
        return 1

for i in range(casos):
    meliante, pulo = map(int,input(""). split())
    cont = cont + 1
    lista = list(range(1, meliante + 1))
    print(f'Case {cont}: {josp(meliante, pulo)}')
