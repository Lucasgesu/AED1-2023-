import graphics as gf
import random as rd
rd.seed()

janela = gf.GraphWin('Teste', 400, 400)

centro = gf.Point(50,50)
raio = 20
bolinha = gf.Circle(centro, raio)
bolinha.draw(janela)
passo_y = 10
passo_x = 10
verm = 255
ver = 255
blue = 255

linha_x = 400
linha_y1 = 100
linha_y2 = 500

linha = gf.Line(gf.Point(400, 100), gf.Point(400,500))

while True:
    tecla = janela.checkKey()
    if tecla != "":
        print(tecla)
    bol_x = bolinha.getCenter().getX()
    bol_y = bolinha.getCenter().getY()

    if tecla == "Up":
        if (bol_y - raio) == linha_y2 and (bol_x + raio)
        bolinha.move(0,-passo_y)
    elif tecla == "Down":
        bolinha.move(0, passo_y)
    elif tecla == "Left":
        bolinha.move(-passo_x, 0)
    elif tecla == "Right":
        bolinha.move(passo_x, 0)
    elif tecla == "s":
        verm = rd.randint(0,255)
        ver = rd.randint(0,255)
        azul = rd.randint(0,255)


        bolinha.setFill(gf.color_rgb(verm, ver, azul))


coordenada = janela.getMouse()
janela.close()
