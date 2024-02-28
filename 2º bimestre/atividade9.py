"""
Escreva um programa em python que leia uma string, e substitua cada segmento de dois
ou mais espaços em branco por um só caractere de espaço. Não deve ser utilizada
qualquer função no python que trabalhe com strings
"""
#------------------------------- Criando Variaveis ---------------------------------
palavra =str(input("Escreva uma frase:"))
espaço = False
cont = 0
palavra_comp = " "
#------------------------------- Criando Variaveis ---------------------------------
#------------------------------- Loop ----------------------------------------------
for letra in palavra:
    if ord(letra) >= 65 and ord(letra) <= 90 or ord(letra) >= 97 and ord (letra) <= 122:
        cont = 0
        if ord(letra) == 32:
            espaço = True
            cont = cont + 1
        else:
            palavra_comp = palavra_comp + letra
        if espaço == True:
            espaço = False
            if cont == 1:
                palavra_comp + palavra_comp + letra
            else:
                pass
#------------------------------- Loop ----------------------------------------------
#------------------------------- Conclusão -----------------------------------------
print(palavra_comp)
#------------------------------- Conclusão -----------------------------------------