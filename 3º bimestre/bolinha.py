import graphics as gf
import random as rd
rd.seed()
#-------------------Criando um objeto GraphWin------------------------
janela = gf.GraphWin('Teste', 400, 400)

centro = gf.Point(50,50)
raio = 20

bolinha = gf.Circle(centro, raio)
bolinha.draw(janela)
anterior = centro
continua = True
while continua:
    coordenada = janela.getMouse()

    if coordenada == anterior:
        continua =  False
        
    else:
        anterior = coordenada
    bolinha = gf.Circle(coordenada, raio)
    bolinha.draw(janela)
    verm = rd.randint(0,255)
    ver = rd.randint(0,255)
    azul = rd.randint(0,255)

    bolinha.setFill(gf.color_rgb(verm, ver, azul))

janela.close()