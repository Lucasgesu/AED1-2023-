with open("usúario.txt", "r") as arq:
    login = arq.readlines()
saida = []
for usúario in login:
    saida.append(login[:-1])
login = saida
print(login)

usúarios ={}
for usúario in login:
    if login in usúarios:
        usúarios[login] = usúarios[login] + 1
    else:
        usúarios[login] = 1
print(usúarios.items())