def dec_to_bin(cislo):
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"

    if isinstance(cislo, str):
        try:
            cislo = int(cislo)
        except ValueError:
            raise ValueError("Vstup musi byt validni cislo: {}".format(cislo))
        
    if not isinstance(cislo, int):
        raise ValueError("Vstup musi byt cele cislo: {}".format(cislo))
    return bin(cislo)[2:]



def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"

if __name__ == "__main__":
    test_bin_to_dec()
    print(dec_to_bin("167"))
    print(dec_to_bin(167))