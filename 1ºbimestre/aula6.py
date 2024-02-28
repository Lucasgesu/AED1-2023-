#Faça um programa em python que leia o nome de 4 times de futebol que estão em
#uma semifinal. Após, leia os gols das duas partidas: time 1 x time 2 e time 3 x time 4.
#Os times vencedores devem ir para a final. Caso haja empate, deve-se perguntar ao
#usuário qual time se classificou. Por fim, deve-se ler os gols da final e mostrar qual
#time foi campeão (se empatar, perguntar quem foi campeão).

Gols_timeA = int(input("Quantos gols o time A fez: "))
Gols_timeB = int(input("Quantos gols o time B fez: "))
Gols_timeC = int(input("Quantos gols o time C fez: "))
Gols_timeD = int(input("Quantos gols o time D fez: "))

ganhador_semiA = ''
ganhador_semiB = ''

if Gols_timeA > Gols_timeB:
    ganhador_semiA = 'Tempo 1'
elif Gols_timeA == Gols_timeB:
    ganhador_semiA = str(input("Qual tempo venceu na moeda?"))
else:
    ganhador_semiA = 'Tempo 2'

if Gols_timeC > Gols_timeD:
    ganhador_semiB = 'Tempo 3'
elif Gols_timeC == Gols_timeD:
    ganhador_semiB = str(input("Qual tempo venceu na moeda?"))
else:
    ganhador_semiB = 'Tempo 4'

gols_final1 = int(input(f"Quantos gols o time {ganhador_semiA} fez na final: "))
gols_final2 = int(input(f"Quantos gols o time {ganhador_semiB} fez na final: "))

if gols_final1 > gols_final2: 
    print(f"O ganhador foi o time {ganhador_semiA}")
else:
    print(f"O ganhador foi o time{ganhador_semiB}")