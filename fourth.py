# Simplifying the `je_tah_mozny` function to make it as concise as possible
def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    start = figurka['pozice']
    typ = figurka['typ']
    dr, dc = cilova_pozice[0] - start[0], cilova_pozice[1] - start[1]

    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8) or cilova_pozice in obsazene_pozice:
        return False  # Target is off the board or occupied

    if typ == 'pěšec':
        return (dr, dc) in {(1, 0), (2, 0)} if start[0] == 2 else (dr, dc) == (1, 0)

    elif typ == 'jezdec':
        return (abs(dr), abs(dc)) in {(2, 1), (1, 2)}

    elif typ == 'věž':
        return (dr == 0 or dc == 0) and all((start[0] + i * (dr and (dr // abs(dr))),
                                             start[1] + i * (dc and (dc // abs(dc)))) not in obsazene_pozice
                                            for i in range(1, max(abs(dr), abs(dc))))

    elif typ == 'střelec':
        return abs(dr) == abs(dc) and all((start[0] + i * (dr // abs(dr)),
                                           start[1] + i * (dc // abs(dc))) not in obsazene_pozice
                                          for i in range(1, abs(dr)))

    elif typ == 'dáma':
        return (dr == 0 or dc == 0 or abs(dr) == abs(dc)) and all((start[0] + i * (dr and (dr // abs(dr))),
                                                                   start[1] + i * (dc and (dc // abs(dc))))
                                                                  not in obsazene_pozice
                                                                  for i in range(1, max(abs(dr), abs(dc))))

    elif typ == 'král':
        return max(abs(dr), abs(dc)) == 1

    return False

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
