texto = ["A", "B", "C", "D"]
outro = texto
print(texto, id(texto))
print(outro, id(texto))
print('-'*15)
texto.append("Tchau")
print(texto, id(texto))
print(outro, id(outro))