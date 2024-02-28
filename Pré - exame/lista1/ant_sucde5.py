"""
Ler 5 (cinco) números inteiros. Exibir o antecessor e o sucessor de cada número
"""

n1 = 1
n2 = 5
n3 = 9
n4 = 13
n5 =  19
ant1 = n1 - 1
ant2 = n2 - 1
ant3 = n3 - 1
ant4 = n4 - 1
ant5 = n5 - 1
suc1 = n1 + 1
suc2 = n2 + 1
suc3 = n3 + 1
suc4 = n4 + 1
suc5 = n5 + 1
antecesores = [ant1, ant2, ant3, ant4, ant5]
sucessores = [suc1, suc2, suc3, suc4, suc5]
print("Os antecessores de:", n1, n2, n3, n4, n5, "são", end=">" )
print(antecesores)
print("Já os sucessores são:", sucessores)

"""
for n in range(5):
    i = int(input("Digite um número: "))
    suc = i + 1
    ant = i - 1
    antecesores.append(ant)
    sucessor.append(suc)
"""