#-------------------------------------- Criando Variaveis ---------------------------------
texto = "as provas objetivas para os cargos de agente de pesquisa e monitoramento (APM) e supervisor de coleta e qualidade (SCQ) serão realizadas em 17 de setembro, com resultados finais divulgados em 23 de outubro. o nível exigido para ambas as funções é de ensino médio completo e os contratos têm um ano de duração, com possibilidade de renovação por outros dois anos."
termos = []
freq = []
cont = 0
#-------------------------------------- Criando Variaveis ---------------------------------
#-------------------------------------- Transformando e Criando ---------------------------
texto = texto.lower() #Transformando tudo em minusculo
texto = texto.replace(",","")#Troca um caracter por outro
texto = texto.replace(".", "")
lista = texto.split(' ') #Criando a lista crua de texto
print(lista)
print(130 * "-")
#-------------------------------------- Transformando e Criando ---------------------------
#------------------------------------- Loop 1 ---------------------------------------------
for termo in lista:
    if termo not in termos:
        termos.append(termo)
        freq.append(1)
    else:
        indice = termos.index(termo) #em que indce está o termo?
        freq[indice] = freq[indice] + 1
#------------------------------------- Loop 1 ----------------------------------------------
#------------------------------------- Loop 2 ----------------------------------------------
while cont < len(termos):
    print(termos[cont],'-',freq[cont])
    cont = cont + 1
#------------------------------------- Loop 2 ----------------------------------------------
#------------------------------------- Conclusão -------------------------------------------
print(130*"-")
#------------------------------------ Conclusão --------------------------------------------