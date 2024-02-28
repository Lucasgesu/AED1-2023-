"""
Programa uma lista de compras e verificar se o produto está na lista
"""
#-------------------------- Criando variaveis ---------------------------------------------
Compras = []
carrinho = "z"
#-------------------------- Criando variaveis ---------------------------------------------
#-------------------------- Verificação ---------------------------------------------------
while carrinho != " ":
    carrinho = input("Novo item:")
    if carrinho != " ":
        Compras.append(carrinho)
print(Compras)
#-------------------------- Verificação ---------------------------------------------------
#-------------------------- Buscando o item -----------------------------------------------
busca = input("Informe o item a ser buscado")
achei = False
#-------------------------- Buscando o item -----------------------------------------------
#-------------------------- Encontrando o item --------------------------------------------
for item in Compras:
    if item == busca:
        achei = True
#-------------------------- Encontrando o item --------------------------------------------
#-------------------------- Verificação 2 -------------------------------------------------
if achei: 
    print("O item está na lista!")
else:
    print("O item não está na lista!")
#-------------------------- Verificação 2 -------------------------------------------------
