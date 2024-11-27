import sys

class Trida:
    def __init__(self, hodnota):
        self.atribut = hodnota

def funkce(parametr):
    promenna = str(parametr)
    return promenna

if __name__ == "__main__":
    argument = 5
    if argument > 10:
        argument /= 2
    vysledek = funkce(argument)
    print (vysledek)        