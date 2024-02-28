palavra_1 = input().strip()
palavra_2 = input().strip()
palavra_3 = input().strip()


if palavra_1 == 'vertebrado':
    if palavra_2 == 'ave':
        if palavra_3 == 'carnivoro':
            animal = 'aguia'
        elif palavra_3 == 'onivoro':
            animal = 'pomba'
    elif palavra_2 == 'mamifero':
        if palavra_3 == 'onivoro':
            animal = 'homem'
        elif palavra_3 == 'herbivoro':
            animal = 'vaca'
elif palavra_1 == 'invertebrado':
    if palavra_2 == 'inseto':
        if palavra_3 == 'hematofago':
            animal = 'pulga'
        elif palavra_3 == 'herbivoro':
            animal = 'lagarta'
    elif palavra_2 == 'anelideo':
        if palavra_3 == 'hematofago':
            animal = 'sanguessuga'
        elif palavra_3 == 'onivoro':
            animal = 'minhoca'
print(animal)