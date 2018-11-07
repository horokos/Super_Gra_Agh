from Struktura import Struktura
from Player import Player
import Code


print("Jesteś gotowy na przygodę?\n")
print("Wybierz klasę (1/2/3)")
print("1. Wojownik")
print("2. Mag")
print("3. Łotrzyk")

player = Player()

while True:
    klasa = input(">>>")

    if klasa == "1":
        player.add_weapon("Noga", 11, 80, 5, "Kopnięcie przeciwnika")
        player.add_weapon("Miecz pazia", 40, 60, 5, "Cios mieczem pazia")
        player.change_armor("Zardzewiała zbroja", 20)
        break

    elif klasa == "2":
        player.add_weapon("Ręce", 11, 80, 5, "Proste zaklęcie rażące")
        player.add_weapon("Dębowa różdżka", 50, 70, 10, "Silne zaklęcie oszałamiające")
        player.change_armor("Stara szata", 10)
        break

    elif klasa == "3":
        player.add_weapon("Ręka", 11, 90, 3, "Sierpowy")
        player.add_weapon("Sztylet złodziejaszka", 30, 80, 3, "Cios sztyletem")
        player.change_armor("Skurzana tunika", 10)
        break

    else:
        print("Zła wartość!\n")


stru = Struktura(klasa + ".txt")

Code.generate()

while True:
    stru.p_move(player)


