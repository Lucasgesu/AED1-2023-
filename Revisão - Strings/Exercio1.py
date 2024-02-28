# 1. Escreva um programa que leia uma lista de palavras do usuário e retorne outra lista
# contendo apenas as palavras com mais de 5 caracteres.

#-------------------------Criando Variveis-------------------------------------------------------------
lista_nomes = ['Prisco','Penna', 'Aythanna', 'Andrew', 'Guilherme', 'Bruno', 'Wendel', 'John', 'Lucas']
#-------------------------Criando Variveis-------------------------------------------------------------
#-------------------------Verificação------------------------------------------------------------------
nomes = [nome for nome in lista_nomes
         if len(nome) == 5]
#-------------------------Verificação------------------------------------------------------------------
#-------------------------Conclusão--------------------------------------------------------------------
print(nomes)
#-------------------------Conclusão--------------------------------------------------------------------