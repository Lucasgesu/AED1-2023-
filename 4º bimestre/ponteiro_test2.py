def incrementa(x):
    print(x, id(x))
    x += 1
    print(x, id(x))

x = 7
print(x, id(x))
incrementa(x)
print(x, id(x))