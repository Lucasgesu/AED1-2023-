codigo1, quant1, valor1 = map(float, input().split())
codigo2, quant2, valor2 = map(float, input().split())
total1 = quant1 * valor1
total2 = quant2 * valor2
total = total1 + total2
print("VALOR A PAGAR: R$ {:.2f}".format(total))
