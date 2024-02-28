from graphics import *
import csv
from html import escape
import datetime
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
pagina_login = GraphWin("Login", 700, 320)  # 600, 500
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

    # Verificar se o botão de login foi clicado
    if 150 <= ponto_clique.getX() <= 250 and 200 <= ponto_clique.getY() <= 230:
        usuario = entrada_usuario.getText()
        senha = entrada_senha.getText()
        if verificar_login(usuario, senha):
            pagina_login.close()
            break
        else:
            texto_erro = Text(Point(390, 225), "Usuário ou Senha Incorretos") # 350, 280
            texto_erro.setTextColor("red")
            texto_erro.draw(pagina_login)

    # Verificar se o botão de cadastro foi clicado
    elif 150 <= ponto_clique.getX() <= 250 and 250 <= ponto_clique.getY() <= 280:
        nome = entrada_nome.getText()
        usuario = entrada_usuario_cadastro.getText()
        senha = entrada_senha_cadastro.getText()
        cadastrar_usuario(nome, usuario, senha)
        mensagem_cadastro = Text(Point(390, 280), "Usuário cadastrado com sucesso!") # 350, 280
        mensagem_cadastro.setTextColor("green")
        mensagem_cadastro.draw(pagina_login)

    pagina_login.update()  # Atualize a janela para responder aos eventos

pagina_login.close()  # Feche a janela quando não for mais necessária

# Função para calcular o diagnóstico com base nos exames
def calcular_diagnostico(glicose, ph_urina, pressao_arterial):
    if glicose <= 70 or ph_urina < 5.5 or pressao_arterial > 140:   #Correção nas comparações
        return "O paciente está com Saúde em Risco, o que pode causar Diabetes Mellitus"
    elif glicose <= 100 and 5.5 <= ph_urina <= 6.5 and pressao_arterial >= 90:  # Correção nas comparações
        return "O paciente está com Saúde Estável"
    else:
        return "O paciente está com Saúde Instável, o que pode causar derrames cerebrais, problemas no coração, insuficiência renal ou paralisia nos rins"

# Criar página para inserir os dados médicos
win = GraphWin("Exames Médicos", 600, 420)  # Aumento da largura e altura da tela


# Função para criar perguntas e campos de entrada
def criar_pergunta_entrada(text, y, width):
    Text(Point(150, y), text).draw(win)
    entry = Entry(Point(400,y), width)
    entry.draw(win)
    return entry

# Criação das perguntas e campos de entrada
nome_entry = criar_pergunta_entrada("Nome do Paciente:", 40, 20)
idade_entry = criar_pergunta_entrada("Idade:", 80, 5)
altura_entry = criar_pergunta_entrada("Altura (Cm):", 120, 5)
peso_entry = criar_pergunta_entrada("Peso (Kg):", 160, 5)
glicose_entry = criar_pergunta_entrada("Nível de Açúcar no Sangue (mg/dl):", 200, 5)
ph_urina_entry = criar_pergunta_entrada("Resultado do Exame de Urina (PH):", 240, 5)
pressao_arterial_entry = criar_pergunta_entrada("Pressão Arterial (mmhg):", 280, 10)
colesterol_entry = criar_pergunta_entrada("Nível de Colesterol (mg/dl):", 320, 10)

# Botão "Diagnóstico"
calc_button = Rectangle(Point(250, 350), Point(350, 380))
calc_button.setFill("lightblue")
calc_button.draw(win)
Text(Point(300, 365), "Calcular Diagnóstico").draw(win)         # 300, 365

win.getMouse()  # Esperar um clique do usuário

def adicionar_botao_editar(resultados_win):
    botao_editar = Rectangle(Point(250, 350), Point(350, 380))
    botao_editar.setFill("lightred")
    Text(Point(360, 365), "Editar resultado").draw(resultados_win)
    botao_editar.draw(resultados_win)

    def editar_dados():
        # Fechar a janela de resultados
        resultados_win.close()

# Criar página para exibir os resultados
resultados_win = GraphWin("Ficha Médica do Paciente", 990, 400) # 600, 400
resultados_win.setBackground("white")

# Exibir dados do paciente e diagnóstico
nome_paciente = nome_entry.getText()
idade_paciente = idade_entry.getText()
altura_paciente = altura_entry.getText()
peso_paciente = peso_entry.getText()
glicose = float(glicose_entry.getText())
ph_urina = float(ph_urina_entry.getText())
pressao_arterial = int(pressao_arterial_entry.getText())
colesterol = colesterol_entry.getText()

Text(Point(300, 30), "Dados do Paciente:").draw(resultados_win) # 300, 30
Text(Point(150, 70), f"Nome: {nome_paciente}").draw(resultados_win) # 150, 70
Text(Point(150, 100), f"Idade: {idade_paciente} anos").draw(resultados_win) # 150, 100
Text(Point(150, 130), f"Altura: {altura_paciente} cm").draw(resultados_win) # 150, 130
Text(Point(150, 160), f"Peso: {peso_paciente} kg").draw(resultados_win) # 150, 160
Text(Point(150, 190), f"Nível de Açúcar no Sangue: {glicose} mg/dl").draw(resultados_win) # 150, 190
Text(Point(150, 220), f"Resultado do Exame de Urina (PH): {ph_urina}").draw(resultados_win) # 150, 220
Text(Point(150, 250), f"Pressão Arterial: {pressao_arterial} mmHg").draw(resultados_win) # 150, 250
Text(Point(150, 280), f"Nível de Colesterol: {colesterol} mg/dl").draw(resultados_win) # 150, 280

diagnostico = calcular_diagnostico(glicose, ph_urina, pressao_arterial)

Text(Point(150, 320), "Diagnóstico:").draw(resultados_win) # 300, 320
Text(Point(300, 350), diagnostico).draw(resultados_win) # 300, 350

resultados_win.getMouse()
resultados_win.close()

win.close()  # Fechar a janela principal quando não for mais necessária