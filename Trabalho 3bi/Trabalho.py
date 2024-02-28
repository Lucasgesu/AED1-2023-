from graphics import *
import csv

# Função para validar o nome de usuário e senha
def validar_login(usuario, senha):
    with open("usuario.csv", "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            if linha["Usuário"] == usuario and linha["Senha"] == senha:
                return True
    return False

# Criar uma janela de login
janela_login = GraphWin("Login", 400, 250)

# Criar os rótulos e campos de entrada para usuário e senha
Text(Point(200, 15), "Realizar Login:").draw(janela_login)

Text(Point(100, 50), "Usuário:").draw(janela_login)
entrada_usuario = Entry(Point(250, 50), 20)
entrada_usuario.draw(janela_login)

Text(Point(100, 100), "Senha:").draw(janela_login)
entrada_senha = Entry(Point(250, 100), 20)
entrada_senha.draw(janela_login)

# Criar um botão de login
botao_login = Rectangle(Point(150, 150), Point(250, 180))
botao_login.setFill("lightblue")
botao_login.draw(janela_login)
Text(Point(200, 165), "Login").draw(janela_login)

while True:
    ponto_clique = janela_login.getMouse()
    if 150 <= ponto_clique.getX() <= 250 and 150 <= ponto_clique.getY() <= 180:
        usuario = entrada_usuario.getText()
        senha = entrada_senha.getText()
        if validar_login(usuario, senha):
            janela_login.close()
            break
        else:
            texto_erro = Text(Point(200, 130), "Usuário ou Senha Incorretos")
            texto_erro.setTextColor("red")
            texto_erro.draw(janela_login)

# Função para calcular o diagnóstico com base nos exames
def calcular_diagnostico(glicose, ph_urina, pressao_arterial):
    if glicose <= 70 or ph_urina < 5.5 or pressao_arterial > "140x90 mmhg":
        return "O paciente está com Saúde em Risco, o que pode causar Diabetes Mellitus"
    elif glicose <= 100 and 5.5 <= ph_urina <= 6.5 and pressao_arterial >= "90x60 mmhg":
        return "O paciente está com Saúde Estável"
    else:
        return "O paciente está com Saúde Instável, o que pode causar derrames cerebrais, problemas no coração, insuficiência renal ou paralisia nos rins"

# Janela gráfica
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

# Botão "Diagnóstico"
calc_button = Rectangle(Point(250, 350), Point(350, 380))
calc_button.setFill("lightblue")
calc_button.draw(win)
Text(Point(300, 365), "Calcular Diagnóstico").draw(win)         # 300, 365

win.getMouse()  # Esperar um clique do usuário

# Obtém os valores inseridos pelo usuário
nome = nome_entry.getText()
idade = int(idade_entry.getText())
altura = int(altura_entry.getText())
peso = float(peso_entry.getText())
glicose = float(glicose_entry.getText())
ph_urina = float(ph_urina_entry.getText())
pressao_arterial = pressao_arterial_entry.getText()

# Calcular o diagnóstico
diagnostico = calcular_diagnostico(glicose, ph_urina, pressao_arterial)

# Fechar a janela gráfica
win.close()

# Exibir o diagnóstico
print(f"Nome do Paciente: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura} Cm")
print(f"Peso: {peso} Kg")
print(f"Nível de Açúcar no Sangue: {glicose} mg/dl")
print(f"Resultado do Exame de Urina: {ph_urina} PH")
print(f"Pressão Arterial: {pressao_arterial}")
print(f"Diagnóstico: {diagnostico}")