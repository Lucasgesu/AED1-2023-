#Faça um programa em python que pergunte ao usuário o seguinte:
# O programa deverá mostrar se a viagem ocorrerá de acordo com as seguintes regras:
#- Deverá custar menos de R$ 30
#- Tem que ter wifi e piscina
#- Se não tiver wifi ou piscina, tem que ter churrasqueira

viagem = int(input("Quanto custa a viagem? "))
if viagem < 30:
    print ("viagem acessivel")
else:
    print ("Viagem cara")
    churras = str(input("Tem churrasqueira?"))
    if churras == "s":
        print ("Viagem acessivel")
    else:
        wifi_piscina = str(input("Tem wifi e pisicina?"))
        if wifi_piscina == "s":
            print ("Viagem acessivel")
        else:
            print ("viagem cara")
