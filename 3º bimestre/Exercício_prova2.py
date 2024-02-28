import random
print("Bem-vindo ao Jogo de Dados!")
alvo = input(str("Digite o valor do alvo(2-12):"))
lancar_dados = int[1,2,3,4,5,6]
lancar_dados2 = int[1,2,3,4,5,6]
random.randint(lancar_dados, lancar_dados2)
result = lancar_dados + lancar_dados2
#--------------------- Verificação -------------------------------------
print("Lançando os dados...")
print("Os números nos dados somam", result)

while alvo:
    if alvo >= result:
        print("Você ganhou a aposta! A soma dos dados é maior ou igual a", result)
    else:
        print("Você perdeu a aposta! A soma dos dados é menor que", result)