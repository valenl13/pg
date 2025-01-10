# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod #dekorátor, který označuje, že je metoda abstraktní
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, sirka, vyska): #konstruktor pro inicializaci atributů
        self.width = sirka
        self.height = vyska

    def area(self):
        return self.width * self.height #vypočet obsahu obdélníku

class Circle(Shape):
    def __init__(self, polomer): 
        self.polomer = polomer

    def area(self):
        return math.pi * (self.polomer ** 2) #výpočet obsahu kruhu

# ZDE DOPLŇTE VLASTNÍ KÓD

from unittest.mock import patch, MagicMock, mock_open

# Pytest testy pro Příklad 3
def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3

