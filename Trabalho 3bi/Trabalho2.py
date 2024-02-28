from graphics import *
import csv

import graphics

# Função para verificar os dados do usuário
def verificar_login(usuario, senha):
    with open("usuario.csv", "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            if linha["Usuário"] == usuario and linha["Senha"] == senha:
                return True
    return False

# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, usuario, senha):
    with open("novo_usuario.csv", "a", newline="") as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow([nome, usuario, senha])

# Criar uma página de login
pagina_login = GraphWin("Login", 700, 320)    # 600, 500

# Criar os espaços de "usuário" e "senha"
Text(Point(350, 20), "Realizar Login:").draw(pagina_login)      # 200, 15

Text(Point(65, 75), "Usuário:").draw(pagina_login)    # 100, 50
entrada_nome = Entry(Point(200, 75), 20)      # 250, 50, 20
entrada_nome.draw(pagina_login)

Text(Point(65, 120), "Senha:").draw(pagina_login)      # 100, 150
entrada_senha = Entry(Point(200, 120), 20)    # 250, 150, 20
entrada_senha.draw(pagina_login)

Text(Point(435, 75), "Nome:").draw(pagina_login)    # 100, 50
entrada_nome = Entry(Point(565, 75), 20)      # 250, 50, 20
entrada_nome.draw(pagina_login)

Text(Point(435, 120), "Usuário:").draw(pagina_login)      # 100, 100
entrada_usuario = Entry(Point(565, 120), 20)     # 250, 100, 20
entrada_usuario.draw(pagina_login)

Text(Point(435, 165), "Senha:").draw(pagina_login)      # 100, 150
entrada_senha = Entry(Point(565, 165), 20)    # 250, 150, 20
entrada_senha.draw(pagina_login)

# Criar um botão de login
botao_login = Rectangle(Point(180, 230), Point(250, 230))     # 150, 200    250, 230
botao_login.setFill("lightblue")
botao_login.draw(pagina_login)
Text(Point(185, 230), "Login").draw(pagina_login)    # 200, 215

# Criar um botão para cadastrar
botao_cadastro = Rectangle(Point(150, 250), Point(250, 280))   # 150,   250, 280
botao_cadastro.setFill("lightgreen")
botao_cadastro.draw(pagina_login)
Text(Point(560, 230), "Cadastrar").draw(pagina_login)   # 200, 265 

    # Verificar se o botão de login foi clicado
if 150 <= ponto_clique.getX() <= 250 and 200 <= ponto_clique.getY() <= 230:
        usuario = entrada_usuario.getText()
        senha = entrada_senha.getText()
        if verificar_login(usuario, senha):
            pagina_login.close()
            break
        else:
            texto_erro = Text(Point(350, 280), "Usuário ou Senha Incorretos")    # 200, 180
            texto_erro.setTextColor("red")
            texto_erro.draw(pagina_login)

    # Verificar se o botão de cadastro foi clicado
    elif 150 <= ponto_clique.getX() <= 250 and 250 <= ponto_clique.getY() <= 280:
        nome = entrada_nome.getText()
        usuario = entrada_usuario.getText()
        senha = entrada_senha.getText()
        cadastrar_usuario(nome, usuario, senha)
        mensagem_cadastro = Text(Point(350, 280), "Usuário cadastrado com sucesso!")   # 200, 180
        mensagem_cadastro.setTextColor("green")
        mensagem_cadastro.draw(pagina_login)

#while True:
#    coordenada = pagina_login.getMouse()
#
#pagina_login.close()

# Criar um nova página para inserir dados
pagina_inserir = GraphWin("Inserir Dados", 700, 320)

# Criar os espaços para inserir os dados
Text(Point(350, 20, "Inserir Dados:").draw(pagina_inserir))

Text(Point(65, 75), "Pressão Arterial:").draw(pagina_inserir)
entrada_pressao = Entry(Point(200, 75), 20)
entrada_pressao.draw(pagina_inserir)

Text(Point(65, 120), "Lipidrograma").draw(pagina_inserir)
entrada_lipi = Entry(Point(200, 120), 20)
entrada_lipi.draw(pagina_inserir)

Text(Point(65, 165), "Sanguineo"). draw(pagina_inserir)
entrada_sangue = Entry(Point(200, 165), 20)
entrada_sangue.draw(pagina_inserir)

# Botão para inserir
botao_inserir = Rectangle(Point(180, 230), Point(250,230))
botao_inserir.setFill("lightyellow")
botao_inserir.draw(pagina_inserir)
Text(Point(185, 230), "Inserir").draw(pagina_inserir)
while True:
    ponto_clique = pagina_login.getMouse()