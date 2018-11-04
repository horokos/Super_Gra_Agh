from Struktura import Struktura
from Player import Player
import Code


print("Jesteś gotowy na przygodę?\n")
print("Wybierz klasę (1/2/3)")
print("1. Wojownik")
print("2. Mag")
print("3. Łotrzyk")

while True:
    klasa = input(">>>")

    if klasa in ["1", "2", "3"]:
        break

    else:
        print("Zła wartość")

player = Player()
stru = Struktura(klasa + ".txt")

Code.generate()

while True:
    stru.p_move(player)

