tentativa_teste = int(input())
for teste in range(0, tentativa_teste):
    entrada = input().split()
    pa = int(entrada[0])
    pb = int(entrada[1])
    cpa = float(entrada[2])/100
    cpb = float(entrada[3])/100
    tempo = 0

    while True:
        pa += int(pa * cpa)
        pb += int(pb * cpb)
        tempo += 1

        if pa > pb or tempo > 100:
            break
    if tempo <= 100:
        print(tempo, "anos.")
    else:
        print("Mais de 1 seculo.")