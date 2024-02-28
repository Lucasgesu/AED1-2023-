começo = input().split()
cod = int(começo[0])
quant = int(começo[1])
preco = 0.0

if cod == 1:
    preco = 4.0 * quant
elif cod == 2:
    preco = 4.5 * quant
elif cod == 3:
    preco = 5.0 * quant
elif cod == 4:
    preco = 2.0 * quant
elif cod == 5:
    preco = 1.5 * quant
print('Total: R$ %0.2f' % preco)