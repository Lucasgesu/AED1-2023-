"""
Considere um sistema de gerenciamento de senhas em Python no qual todas as
informações de usuário são armazenadas em um único dicionário da seguinte forma:
"""

dados_usuarios = {
    'joao123': {
        'senha':'senha123',
        'nivel_acesso': 'usuario',
        'data_criacao': '2023 - 01 - 01'
    }}
"""
a)Faça uma função verificar_senha que recebe como parâmetros o dicionário, um nome de
usuário e uma senha de entrada. A função deve retornar True se o nome de usuário existir
no dicionário e a senha fornecida coincidir com a senha armazenada, e False caso contrário.
"""
def verificar_senha(dados_usuarios, logins, senha, nome):
 if dados_usuarios in logins:
  logins[nome, senha] = dados_usuarios[logins[nome,senha]]
 elif:
        logins[nome, senha] == dados_usuarios
        return True
 else:
    return False

"""
b)Crie outra função chamada atualizar_senha que recebe como parâmetros o dicionário de
dados de usuários, um nome de usuário, a senha atual e a nova senha. A função deve
verificar se o nome de usuário existe e se a senha atual coincide com a senha armazenada.
Se ambas as condições forem verdadeiras, a função deve atualizar a senha no dicionário.
Caso contrário, a função não faz alterações.
"""
def atualizar_senha(dados_usuarios, login, senha_atual, nova_senha):
   if dados_usuarios in login:
      dados_usuarios = {
          "prisco456",{
         senha_atual: "aed1",
         nova_senha: ""
      } }
   else:
      return False
