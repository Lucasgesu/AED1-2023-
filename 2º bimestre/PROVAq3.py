'''
(B) Escreva um código em Python que substitua todas as menções a usuários na string
comentário por "USUARIO_MENCIONADO".
'''
#------------------------------------------Criando Usúario--------------------------
usuario = 'usuario_mencionado'
comentario = ''
nova_letra = ''
#------------------------------------------Criando Usúario--------------------------
#------------------------------------------Verificação------------------------------
for x in usuario:
     codigo = ord(x)
    if (codigo >=97) and (codigo <=122):
        nova_letra = chr(codigo -32)
        comentario = comentario + nova_letra
    else:
        comentario = comentario + usuario[x]
print(comentario)
#------------------------------------------Verificação------------------------------