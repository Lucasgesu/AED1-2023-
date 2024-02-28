"""
nome =  "Inicio"
nome2 = nome
nome = nome + "e fim"
print(nome2)
"""
"""
nome = ["Inicio"]
nome2 = nome
nome[0] += " e fim"
print(nome2)
"""
"""
Pois a primeira parte do código junta uma váriavel com uma string solta, e consequentemente
ela não podem se junta pois é um tipo imuntável.
Já na segunda parte a string está dentro de uma lista e "listas" são mutável,
pois o valor do endereço sempre será o mesmo que ficará dentro da mémoria 
"""