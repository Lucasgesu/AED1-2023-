renda = float(input())
imp_ant = 0
if renda <= 2000.00:
    print("Isento")
else:
    if renda <= 3000.00:
        extra = renda - 2000.00
        ir = 8
    elif renda <= 4500.00:
        extra = renda - 3000.01
        imp_ant = 80
        ir = 18
    else:
        extra = renda - 4500.00
        imp_ant = 350.00
        ir = 28

    pagamento = extra * ir / 100
    print(f"R$ {pagamento + imp_ant:.2f}")