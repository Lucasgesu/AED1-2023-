#Faça um programa que, ao receber os valores da largura e do comprimento de uma figura geométrica,
#mostre se esta é um quadrado ou apenas um retângulo. 
#Caso um valor seja menor ou igual a zero, deve-se mostrar um erro.

# float = "Numeros reais"
larg = float(input("Digite o valor da largura: "))
compr = float(input("Digite o valor do comprimento: "))
#"==" - igualdade 
#"=" - atribuição
if larg == 0 or compr == 0:
    print ("alguns desse valores é zero!")
else:
    if larg == compr:
        print ("É quadrado")
    else:
        print ("É um retângulo")
