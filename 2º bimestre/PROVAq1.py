#Considere um programa em Python que simula um jogo de cartas com um
#baralho completo. O baralho é inicializado com 52 cartas, divididas em 4 naipes
# (Paus, Ouros, Copas e Espadas) e 13 valores (de 2 a 10, Valete, Dama, Rei e Ás). O
# programa deve utilizar listas para armazenar o baralho e sortear duas cartas para
# cada um de 6 jogadores.

# Mostre na tela cada uma das cartas sorteadas para cada jogador. Você não deve permitir que uma carta seja sorteada mais de uma vez.
#-----------------------------------------------------Sortear--------------------------------------------------------------------------
import random
#-----------------------------------------------------Sortear--------------------------------------------------------------------------
#-----------------------------------------------------Criando Jogadores----------------------------------------------------------------
Jogador1 = str(int('Jogador 1 escolheu duas cartas do baralho:'))
jogador2 =str(int('Jogador 2 escolheu duas cartas do baralho: '))
jogador3 = str(int('Jogador 3 escolheu duas cartas do baralho: '))
jogador4 = str(int('Jogador 4 escolheu duas cartas do baralho:'))
jogador5 = str(int('Jogador 5 escolheu duas cartas do baralho: '))
jogador6 = str(int('Jogador 6 escolheu duas cartas do baralho: '))
#-----------------------------------------------------Criando Jogadores----------------------------------------------------------------
#-----------------------------------------------------Criando Variaveis (Cartas)-------------------------------------------------------
cartas = [2,3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Dama', 'Rei', 'Ás']
naipes = [cartas]

print('O naipe de Paus tem:', [cartas], '53 Cartas')
print('O naipe de Ouros tem:', [cartas], '53 Cartas')
print('O naipe de Copas tem:', [cartas], '53 Cartas')
print('O naipe de Espadas tem:', [cartas], '53 Cartas')
#-----------------------------------------------------Criando Variaveis (Cartas)-------------------------------------------------------