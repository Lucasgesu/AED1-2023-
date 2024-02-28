#----------------------Declarando variaveis --------------------
nome = str(input("Escreva um nome: "))
nome_completo1 = ""
nome_completo2 = ""
nova_letra = ""
#-----------------------Declarando variaveis -------------------
#-----------------------Loop e verificação (DE MINUSCULO PARA MAIUSCULO) --------------------

for x in nome:
    codigo = ord(x)
    if (codigo >=97) and (codigo <=122):
        nova_letra = chr(codigo -32)
        nome_completo1 = nome_completo1 + nova_letra
    else:
        nome_completo1 = nome_completo1 + nome[x]
print(nome_completo1)

#-----------------------Loop e verificação (DE MINUSCULO PARA MAIUSCULO) ---------------------
#-----------------------Segundo loop e verificação (DE MAIUSCULO PARA MINUSCULO) -------------
"""
for y in nome:
    codigo = ord(y)
    if (codigo >= 65) and (codigo <= 90):
        nova_letra = chr (codigo +32)
        nome_completo2 = nome_completo2 + nova_letra
    else:
        nome_completo2 = nome_completo + nome[y]
print(nome_completo2)
"""
#-----------------------Segundo loop e verificação (DE MAIUSCULO PARA MINUSCULO) -------------
#----------------------- Terceiro loop e verificação (nome completo) -------------------------
for 