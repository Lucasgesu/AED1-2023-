'''
Leia uma matriz e mostre na tela de formato para humanos
'''
"""
import numbers as np

def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input('Digite o elemento [' +  str:(i) + ']''[' + str(j) + ']'))
            linha.append(valor)
            matriz.append(linha)
    return matriz


def le_matriz():
    lin = int(input('Digite o numero de linhas da matriz: '))

"""
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(m)

#------------------------Valindando a matriz----------------------------------------------
tam = len(m[0])
for linha in m[1:]:
    if len(linha) != tam:
        print('ERRO! Matriz inválida')
        exit('-1')

for linha in m:
    print('|', end=" ")
    for coluna in linha:
        print(coluna, end=" ")
    print('|')

#--------------------Começando determinante---------------------------------------------

a = m[0][0] * m[1][1] * m[2][2]
b = m[0][1] * m[1][2] * m[2][0]
c = m[0][2] * m[1][0] * m[2][1]
d = m[0][2] * m[1][1] * m[2][0]
e = m[0][0] * m[1][2] * m[2][1]
f = m[0][1] * m[1][0] * m[2][2]

det = a+b+c+d+e+f
print('O determinate é', det)