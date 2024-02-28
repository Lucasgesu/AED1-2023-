#--------------------------------------- Criando Variaveis ----------------------------------------------
frase = input("Digite uma frase: ")
nova_frase = ""
palavra = ""
#--------------------------------------- Criando Variaveis -----------------------------------------------
#--------------------------------------- Loop ------------------------------------------------------------
for letra in frase:
    if letra == " ":
        if palavra:
            primeira_letra = palavra[0]
            primeira_letra_maiuscula = chr(ord(primeira_letra) - 32)
            palavra = primeira_letra_maiuscula + palavra[1:]
            nova_frase += palavra + " "
            palavra = ""
    else:
        palavra += letra

if palavra:
    primeira_letra = palavra[0]
    primeira_letra_maiuscula = chr(ord(primeira_letra) - 32)
    palavra = primeira_letra_maiuscula + palavra[1:]
    nova_frase += palavra  
#-------------------------------------- Loop --------------------------------------------------------------
#-------------------------------------- Conclusão ---------------------------------------------------------
print("Nova frase:", nova_frase)
#-------------------------------------- Conclusão ---------------------------------------------------------