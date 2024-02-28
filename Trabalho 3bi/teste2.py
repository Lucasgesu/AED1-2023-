from graphics import *
import csv
from html import escape

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
pagina_login = GraphWin("Login", 600, 420)  # 600, 500
pagina_login.setBackground("white")  # Defina uma cor de fundo para a janela

# Criar os espaços de "usuário" e "senha"
Text(Point(350, 20), "Realizar Login:").draw(pagina_login)

Text(Point(65, 75), "Usuário:").draw(pagina_login)
entrada_usuario = Entry(Point(200, 75), 20)
entrada_usuario.draw(pagina_login)

Text(Point(65, 120), "Senha:").draw(pagina_login)
entrada_senha = Entry(Point(200, 120), 20)
entrada_senha.draw(pagina_login)

Text(Point(435, 75), "Nome:").draw(pagina_login)
entrada_nome = Entry(Point(565, 75), 20)
entrada_nome.draw(pagina_login)

Text(Point(435, 120), "Usuário:").draw(pagina_login)
entrada_usuario_cadastro = Entry(Point(565, 120), 20)
entrada_usuario_cadastro.draw(pagina_login)

Text(Point(435, 165), "Senha:").draw(pagina_login)
entrada_senha_cadastro = Entry(Point(565, 165), 20)
entrada_senha_cadastro.draw(pagina_login)

# Criar um botão de login
botao_login = Rectangle(Point(150, 200), Point(250, 230))
botao_login.setFill("lightblue")
botao_login.draw(pagina_login)
Text(Point(200, 215), "Login").draw(pagina_login)

# Criar um botão para cadastrar
botao_cadastro = Rectangle(Point(150, 250), Point(250, 280))
botao_cadastro.setFill("lightgreen")
botao_cadastro.draw(pagina_login)
Text(Point(200, 265), "Cadastrar").draw(pagina_login)

# Laço principal
while True:
    ponto_clique = pagina_login.getMouse()

    # Verificar se o botão
