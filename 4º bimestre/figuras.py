def diviso_comum (v,r):
    figura_restantes = None
    while figura_restantes != 0:
        figura_restantes = v % r
        v = r
        r = figura_restantes
    return v

import math
trocar_figuras = int(input())
for f in range(trocar_figuras):
    numeros = [int(num) for num in input(). strip(). split(" ")]
    print(math.gcd(numeros[0], numeros[1]))
