#lendo o arquivo CSV

arq = open('aula2.csv', 'r') # r = indica leitura

ano = int(input('Informe o ano de interesse:'))
arq.readline() #apenas para que a leitura ignore a 1ª linha do arq(arquivo)

html = "<table border =1>"


for linha in arq:
    lista = linha[:-1].split(';')
    if ano == int(lista[5]):
        html = html + "<tr>" #criando nova linha da tabelha em HTML
        for coluna in lista:
            html = html + "<td>" + coluna + "</td>"  #criando e fechando uma nova coluna na tabela em HTML
        html = html + "</tr>" #fechando a linha da tabela em HTML

html = html + "</table>"

arq.close()
saida = open('saida.html', 'w')
saida.write(html)
saida.close()