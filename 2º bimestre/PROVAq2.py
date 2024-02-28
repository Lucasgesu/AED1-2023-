'''
O Instagram é uma popular plataforma de mídia social que permite aos
usuários compartilhar fotos e vídeos. Considere um cenário em que você está
desenvolvendo uma funcionalidade para analisar os comentários em postagens do
Instagram.
(A) Escreva um código em Python que verifique se uma string comentário contém a
menção a um usuário. Uma menção começa com o símbolo "@" seguido por um
nome de usuário válido (composto apenas por letras minúsculas e números), por
exemplo: "@usuario123".
'''
#----------------------------------Criando Usúario------------------------------
usuario =  str(int(input('Informe seu usúario:')))
#----------------------------------Criando Usúario------------------------------
#----------------------------------Criando Comentário---------------------------
comentario = usuario,"comentou: Nossa, que lugar bacana!"
#----------------------------------Criando Comentário---------------------------
#----------------------------------Verificando Usua--------------------------
for x in comentario:
    codigo = ord(x)
    if (codigo >= 0) and (codigo <= 122):
        print("Parabéns, o usuário", usuario, 'é válido')

#----------------------------------Verificando Usuario--------------------------
