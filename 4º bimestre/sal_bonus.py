nome = str(input())
sal_fixo = float(input())
vendas_ganhas = float(input())
comisao = (vendas_ganhas * 15)/100
resultado =  sal_fixo + comisao
print(f"TOTAL = R${resultado:.2f}")