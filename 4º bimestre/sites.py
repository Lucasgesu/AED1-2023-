with open("site.txt", "r") as arq:
    sites = arq.readlines()
saida = []
for site in sites:
    saida.append(site[:-1])
sites = saida
print(sites)

dic = {}  #aqui  vai o dicionari0 com os dados condensados
#print(dic)
for site in sites:
    if site in dic:
        dic[site] += 1
    else:
        dic[site] = 1
        #print(dic)
#print(dic.items())
saida = "site.fr"
