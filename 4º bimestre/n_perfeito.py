N = int(input())

for i in range(N):
    x = int(input())
    divisao = []

    for y in range(1,x):

        if x % y == 0:
            divisao.append(y)

    if sum(divisao) == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")