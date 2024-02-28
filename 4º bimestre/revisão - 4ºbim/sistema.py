#-------------Inicializar estoque ------------------------------------------
estoque = {"chocolate": 10, "refri": 7, "morango": 4}
#-------------Inicializar estoque-------------------------------------------
#-------------Adicionar estoque---------------------------------------------

def adicionar_produto(estoque,prod, quant):
    if prod in estoque:
        estoque[prod] = estoque[prod] + quant
    else:
        estoque[prod] == quant
        return estoque

#-------------Adicionar estoque---------------------------------------------
#-------------Venda de produto----------------------------------------------
def vender_produto(estoque,prod,quant):
    if prod in estoque and estoque[prod] >= quant:
        estoque[prod] = estoque[prod] - quant
    else:
        print("você não pode comprar o", prod, "pois está em falta no momento")
#-------------Venda de produto-----------------------------------------------
#-------------Relatório------------------------------------------------------
def relatar_produto(estoque):
    print("No momento o que temos de produto são esses:", estoque)
#-------------Relatório------------------------------------------------------
#-------------Teste final----------------------------------------------------
adicionar_produto(estoque, "chocolate", 5)
vender_produto(estoque, "refri", 4)
print(relatar_produto)
#-------------Teste final----------------------------------------------------
