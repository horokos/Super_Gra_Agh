from Struktura import Struktura
from Player import Player
import Code
from Items import Weapon
from Items import Armor


print("Jesteś gotowy na przygodę?\n")
print("Wybierz klasę (1/2/3)")
print("1. Wojownik")
print("2. Mag")
print("3. Łotrzyk")

while True:
    klasa = input(">>>")

    if klasa == "1":
        weapon = Weapon("Noga", 10, 80, 5, "Kopnięcie przeciwnika")
        armor = Armor("Zardzewiała zbroja", 10)
        player = Player(weapon, armor)
        player.add_sword("Miecz pazia", 40, 60, 5, "Cios mieczem pazia")
        break

    elif klasa == "2":
        weapon = Weapon("Ręce", 10, 80, 5, "Proste zaklęcie rażące")
        armor = Armor("Stara szata", 5)
        player = Player(weapon, armor)
        player.add_sword("Dębowa różdżka", 50, 70, 10, "Silne zaklęcie oszałamiające")
        break

    elif klasa == "3":
        weapon = Weapon("Ręka", 10, 90, 3, "Sierpowy")
        armor = Armor("Skurzana tunika", 8)
        player = Player(weapon, armor)
        player.add_sword("Sztylet złodziejaszka", 30, 80, 3, "Cios sztyletem")
        break

    else:
        print("Zła wartość!\n")


stru = Struktura(klasa + ".txt")

Code.generate()

while True:
    stru.p_move(player)


