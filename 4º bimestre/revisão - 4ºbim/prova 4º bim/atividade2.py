def divisao (num, sucs):
    if num in sucs:
        return sucs[num]
    elif num == 0:
        sucs[num] = (0)
        return sucs[num]
    elif num == 1:
        sucs[num] = ()
    else:
        divisao(num % sucs)
        result = num % sucs
        print(result)