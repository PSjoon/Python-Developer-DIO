a = input()
b = input()
c = input()

if (a == 'vertebrado'):

    if (b == 'ave'):

        if (c == 'carnivoro'):
            animal = 'aguia'
        elif (c == 'onivoro'):
            animal = 'pomba'

    elif (b == 'mamifero'):

        if (c == 'herbivoro'):
            animal = 'vaca'
        elif (c == 'onivoro'):
            animal = 'homem'

elif (a == 'invertebrado'):

    if (b == 'inseto'):

        if (c == 'hematofago'):
            animal = 'pulga'
        elif (c == 'herbivoro'):
            animal = 'lagarta'

    elif (b == 'anelideo'):

        if (c == 'hematofago'):
            animal = 'sanguessuga'
        elif (c == 'onivoro'):
            animal = 'minhoca'

print(animal)
