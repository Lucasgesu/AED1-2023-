def gasto_frutas(produtos, precos, quant):
    valor_total = 0
    for produtos, quant in zip(produtos, quant):
        valor_prod = precos[produtos.index(produtos)]
        valor_total += valor_prod * quant
        return valor_total
def principal():
    n = int(input())
    for _ in range(n):
        produtos = []
        precos = []
        for _ in range(int(input())):
            produtos.append(input()[:50])
            precos.append(float(input()))
        quant = []
        for _ in range(int(input())):
            quant.append(int(input()))
        print("R$ {:.2f}".format(gasto_frutas(produtos, precos, quant)))

    if__name__ = "__main__":
    main()