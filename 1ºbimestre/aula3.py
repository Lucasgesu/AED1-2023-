#Construa um programa em python que, informadas três medidas a, b e c pelo
#usuário, verifique se elas podem ser lados de um triângulo. Se não puderem ser,
#primeiramente o algoritmo deve informar isso. Se for possível serem lados de
#triângulo, deve dizer qual tipo de triângulo pode ser construído com essas medidas
#(isósceles, escaleno ou equilátero). A condição para formar um triângulo:
#comprimento do maior segmento seja inferior à soma dos comprimentos dos dois
#menores.
Lado1 = float(input("Digite o lado um do triângulo: "))
Lado2 = float(input("Digite o lado dois do triângulo: "))
Lado3 = float(input("Digite o lado três do triângulo: "))

if Lado1 >= (Lado2 + Lado3) or Lado2 >= (Lado1 + Lado3) or Lado3 >= (Lado1 + Lado2):
    print ("Não é um triângulo!")
else:
    if Lado1 == Lado2 and Lado1 == Lado3 and Lado2 == Lado3:
        print ("O triângulo é equilatero!")
    else:
        if Lado1 != Lado2 and Lado1 != Lado3 and Lado3 != Lado2:
            print ("O triângulo é escaleno!")
        else:
            print ("O Triângulo é isósceles")