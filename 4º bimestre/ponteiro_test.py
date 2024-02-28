import sys
texto = ("sys")
print("Ponteiros ----->", sys.getrefcount(texto))# mais um ponteiro apontando para váriavel
outro = texto
print(texto, id(texto))
print(outro, id(outro))
print("-"*40)
print("Ponteiros --->", sys. getrefcount(texto))