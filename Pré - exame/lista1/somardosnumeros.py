"""
Ler dois números. Somar os números lidos e, após, multiplicar o resultado da soma pelo primeiro número
lido. Apresentar o resultado final.
"""
n1 = int(input("Escrevar o primero número: "))
n2 = int(input("Escreva o segundo número: "))

def soma(n1, n2):
    resp = n1 + n2
    return resp

def mult(resp, n1):
    final = resp * n1
    return final
resp = soma(n1, n2)
final = mult(resp, n1)
print("A resposta final é:",final)
"""
resp = n1 + n2
final = resp * n1
print(final)
"""