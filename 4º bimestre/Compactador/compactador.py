with open("texto.txt", 'r') as arquivo:
    tex = arquivo.read()

tex = tex.replace('\n', '')
print(tex)
lista = tex.split(" ")
dic = {}
