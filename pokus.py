# funkce vrati treti prvek ze seznamu
# def vrat_treti(seznam):
#    if (len(seznam) < 3):
#        print ("Neobsahuje 3 položky")
#    else:
#        return seznam[3]

# funkce spocita prumer z hodnot v seznamu
#def udelej_prumer(seznam):
#    soucet = sum(seznam)
#    pocet = len(seznam)
#
#   prumer = soucet / pocet
#    return prumer

# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(slovnik):
    prumer = sum(student["znamky"]) / len(student["znamky"])
    text = f"Jmeno: {student["jmeno"]}, Prijmeni: {student['prijmeni']}, Vek: {student["vek"]}, Prumerna znamka {prumer}"
    return text


if __name__ == "__main__":
#    seznam = [9,8]
#   vysledek = vrat_treti(seznam)
#    print(vysledek)

#    vysledek2 = udelej_prumer(seznam)
#    print(vysledek2)

    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    print(naformatuj_text(student))