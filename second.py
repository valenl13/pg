def cislo_text(cislo):
    cislo = int(cislo)  # Převod vstupu na celé číslo
    if cislo < 0 or cislo > 100:
        return "Číslo musí být v rozmezí 0 až 100."

    jednotky = ["nula", "jedna", "dvě", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desítky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    nepravidelne = ["", "jeden", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]

    if cislo < 10:
        return jednotky[cislo]
    elif 10 <= cislo < 20:
        if cislo == 10:
            return "deset"
        elif cislo == 11:
            return "jedenáct"
        elif cislo == 12:
            return "dvanáct"
        elif cislo == 13:
            return "třináct"
        elif cislo == 14:
            return "čtrnáct"
        elif cislo == 15:
            return "patnáct"
        elif cislo == 16:
            return "šestnáct"
        elif cislo == 17:
            return "sedmnáct"
        elif cislo == 18:
            return "osmnáct"
        elif cislo == 19:
            return "devatenáct"
    else:
        desitka = desítky[cislo // 10]
        jednicka = cislo % 10
        if jednicka == 0:
            return desitka
        else:
            return f"{desitka} {nepravidelne[jednicka]}"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
