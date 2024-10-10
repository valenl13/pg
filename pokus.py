import sys

def main(parametr):
    otevreny_soubor = open(soubor, "r")
    for radka in otevreny_soubor:
        print(radka)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Zadej nazev souboru")
    soubor = sys.argv[1]
    main(soubor)