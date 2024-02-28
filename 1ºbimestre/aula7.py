#Crie um programa em Python que leia o rendimento mensal do usuário, qual o
#modelo de imposto (sem correção/com correção das perdas no governo Bolsonaro) e
#retorne o quanto ele deve pagar de imposto.

rendimento = float(input("Qual o rendimento mensal?"))
imposto = int(input("Qual modelo vc escolhe?1(com correção) ou 0(sem correção)"))
# Aliq = Aliquota
#Pad = parcela a dedudizr
if imposto == 1:
    if rendimento >= 6125.99:
        Aliq = 0.275 
        Pad = 1141.71
    else:
        if rendimento >= 4926.15:
            Aliq = 0.225
            Pad = 835.41
        else:
            if rendimento >= 3712.17:
                Aliq = 0.15
                Pad = 465.95
            else:
                if rendimento >= 2500.45:
                    Aliq = 0.075
                    Pad = 187.54
                else:
                    Aliq = 0
                    Pad = 0
else:
    if rendimento >= 4664.68:
        Aliq = 0.275
        Pad = 869.36
    else:
        if rendimento >= 3751.06:
            Aliq = 0.225
            Pad = 636.13
        else:
            if rendimento >= 2826.66:
                Aliq = 0.15
                Pad = 354.80
            else:
                if rendimento >= 1903.99:
                    Aliq = 0.075
                    Pad = 142.80
                else:
                    Aliq = 0
                    Pad = 0
total = (rendimento * Aliq) - Pad
if Pad == 0:
    print ("Você está isento de pagar imposto")
else:
    print ("seu imposto total a pagar:", round(total,2))