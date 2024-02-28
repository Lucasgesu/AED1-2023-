#Uma empresa de transporte oferece diferentes tarifas com base na distância percorrida em quilômetros e no tipo de veículo utilizado. Implemente um
#programa em Python que solicite ao usuário a distância da viagem e o tipo de
#veículo, e calcule o valor total a ser pago. As informações sobre as tarifas estão
#descritas a seguir: Ônibus: R$ 0,50 por Km; Carro: R$ 0,75 por Km; Moto: R$ 0,45
#por Km. Além disso, a empresa oferece os seguintes descontos, dependendo da distância:
#Até 100 km: nenhum desconto.
#De 101 km a 300 km: 10% de desconto.
#Acima de 300 km: 20% de desconto.



onibus= 0.50
Carro = 0.75
moto = 0.45




Dist = float(input("Qual foi a distância da viagem (em km): "))
veiculo = int(input("Qual foi o veículo usado?1(carro) ou 2(moto) ou 3(onibus)"))



if veiculo == 1:
    if Dist == 100:
        print("Não tem desconto")
    else:
        if Dist < 301:
            desconto = 75
        else:
            if Dist >= 302:
                desconto = 37.5



if veiculo == 2:
    if Dist == 100:
        desconto = 0
        print("Não tem desconto")
    else:
            if Dist < 301:
                desconto = 45
            else:
                    if Dist >= 301:
                        desconto = 22.5

if veiculo == 3:
    if Dist == 100:
        print("Não tem desconto")
    else:
            if Dist < 301:
                desconto = 50
            else:
                    if Dist >= 301:
                        desconto = 250




desc = (veiculo + Dist) - desconto

print("O valor a ser pago é de", desc)
