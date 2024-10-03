# funkce while
def stars_while():
    print('zacatek')
    i = 0

    while i<5:
        print('*')
        i += 1

    print('konec')

#funkce for
def stars_for():
    print('zacatek')
    i = 0

    for i in [0, 1, 2, 3, 4]:
        print('*', i)
        
    print('konec')



def in_range(min_number, max_number, number):
    if (number > min_number and number < max_number):
        print ('Is in range')
    else:
        print ('Is not in range')

#in_range(100, 1000, 5)


def zobraz_pozdrav(jmeno):
    print('Ahoj', jmeno)

jm = input("Zadej jmeno: ")
zobraz_pozdrav(jm)