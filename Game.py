from Struktura import Struktura
from Player import Player
import os
import Code


FILE_NAME = ["1.txt", "2.txt", "3.txt", "boss.txt", "weapon.txt"]
for i in FILE_NAME:
    if not os.path.isfile(i):
        input("Brak pliku " + i)
        exit(0)

while True:
    print("Jesteś gotowy na przygodę?\n")
    print("Wybierz klasę (1/2/3)")
    print("1. Wojownik")
    print("2. Mag")
    print("3. Łotrzyk")

    player = Player()

    while True:
        klasa = input(">>>")

        if klasa == "1":
            player.add_weapon("Noga", 11, 90, 5, "Kopnięcie przeciwnika")
            player.add_weapon("Miecz pazia", 40, 60, 5, "Cios mieczem pazia")
            player.add_armor("Zardzewiała zbroja", 15)
            break

        elif klasa == "2":
            player.add_weapon("Ręce", 11, 90, 5, "Proste zaklęcie rażące")
            player.add_weapon("Dębowa różdżka", 50, 70, 10, "Silne zaklęcie oszałamiające")
            player.add_armor("Stara szata", 5)
            break

        elif klasa == "3":
            player.add_weapon("Ręka", 11, 90, 5, "Sierpowy")
            player.add_weapon("Sztylet złodziejaszka", 30, 80, 3, "Cios sztyletem")
            player.add_armor("Skurzana tunika", 10)
            break

        else:
            print("Zła wartość!\n")

    Code.generate(5)
    player.load_names(int(klasa))
    stru = Struktura(klasa + ".txt")

    # wczytywanie obrazka z bossem
    Code.boss_name = ['Deathwing', 'Czarnoksieznik', 'Ksiezniczka'][int(klasa) - 1]
    with open("boss.txt", "r") as f:
        tmp = 0
        for line in f:
            if line[:3] == "x x":
                tmp += 1
            if tmp > int(klasa) * 2:
                break
            if tmp > int(klasa) * 2 - 2:
                Code.boss_pict += line
    f.close()

    while True:
        stru.p_move(player)
        if stru.end:
            break

    while True:
        os.system('cls')
        print("Zagrać ponownie? (t/n)")
        p = input(">>>")

        if p.upper() == "T":
            break

        if p.upper() == "N":
            exit(0)

        else:
            print("Zła wartość!\n")




