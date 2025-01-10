# Příklad 1: Práce s podmínkami a řetězci
# Zadání:
# Napište funkci `process_strings`, která přijme seznam řetězců. 
# Funkce vrátí nový seznam, který obsahuje pouze řetězce delší než 3 znaky, převedené na velká písmena.
# Pokud seznam obsahuje řetězec "STOP", ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_strings(strings):
    # ZDE NAPIŠTE VÁŠ KÓD

    seznam = [] #vytvoření prázdného seznamu pro ukládání výsledků
    for string in strings: #pro všechny řetězce v seznamu
        if string == "STOP": #pokud je řetězec STOP
            break #ukončí se zpracování seznamu
        if len(string) > 3: #pokud je řetězec delší než 3
            seznam.append(string.upper()) #převede na velká písmena

    return seznam #vrácení výsledného seznamu

# Pytest testy pro Příklad 2
def test_process_strings():
    assert process_strings(["abc", "abcd", "STOP", "efgh"]) == ["ABCD"]
    assert process_strings(["hello", "world", "STOP", "python"]) == ["HELLO", "WORLD"]
    assert process_strings(["hi", "ok", "go"]) == []
    assert process_strings(["code", "test", "debug"]) == ["CODE", "TEST", "DEBUG"]