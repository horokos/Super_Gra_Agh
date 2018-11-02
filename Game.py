from Struktura import Struktura
from Player import Player

player = Player()
stru = Struktura()

print("Jesteś gotowy na przygodę?\n")
print("Wybierz klasę (1/2/3)")
print("1. Wojownik")
print("2. Mag")
print("3. Łotrzyk")

klasa = input(">>>")

while True:
    stru.p_move(player)

