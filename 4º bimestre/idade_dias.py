idade = int(input())
anos = int(idade/365)
resto = idade - (anos  * 365)
meses = int(resto/30)
dias = resto - meses * 30
print(anos,"ano(s)")
print(meses,"mes(es)")
print(dias,"dia(s)")