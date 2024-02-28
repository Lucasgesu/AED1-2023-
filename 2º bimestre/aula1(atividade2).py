"""
LEIA UMA PALAVRA E TRANSFORME DE MAIUSCULO PARA MINISCULO
"""
#---------------------------------------------------------
# -------------------------- ord = valor do caracter ----------------
# -------------------------- chr = caracter do valor ----------------------------
"""
letra = input("informe a letra:) 
codigo = ord(letra)
nova letra = chr(codigo + 1)
print(nova_letra)
"""
#----------------------Declarando variavel--------------------------------------
palavra = str(input("escreva uma palavra: "))
maiuscula = ""
#----------------------Declarando variavel---------------------------------------
# ---------------------Loop e verificação----------------------------------------
for i in palavra:
    codigo = ord(i)
    if(codigo>=97) and (codigo<=122):
        nova_letra = chr(codigo-32)
        maiuscula = maiuscula + nova_letra
    else:
        maiuscula = maiuscula + palavra[i]
print(maiuscula)
#----------------------Loop e verificação------------------------------------------