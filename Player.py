# -*- coding: utf-8 -*-
import random


class Player:
    def __init__(self):
        self.hp = 100
        self.exp = 1
        self.lvl = 1

    def attack(self):
        enemy_hp = 100

        while True:
            print("-"*20)
            print("Twoje hp " + str(self.hp) + "\nHp przeciwnika " + str(enemy_hp))

            while True:
                p_attack = input("Jak chcesz atakować? (Silny/Szybki)\n")

                if p_attack.upper() == "SILNY" and random.randint(0, 100) < 40:
                    tmp = random.randint(40+self.lvl*10, 60+self.lvl*10)
                    enemy_hp -= tmp
                    print("Trafiłeś za " + str(tmp))
                    break

                elif p_attack.upper() == "SZYBKI" and random.randint(0, 100) < 80:
                    tmp = random.randint(20+self.lvl*10, 40+self.lvl*10)
                    enemy_hp -= tmp
                    print("Trafiłeś za " + str(tmp))
                    break

                elif p_attack.upper() != "SZYBKI" and p_attack.upper() != "SILNY":
                    print("Musisz wpisać Silny/Szybki\n")

                else:
                    print("Chybiłeś :(\n")
                    break

            if enemy_hp <= 0:
                tmp = random.randint(30, 60)
                self.exp += tmp
                print("Wygrałeś, dostałeś " + str(tmp) + " exp\n")
                self.update_lvl()
                break

            tmp = random.randint(10, 20)
            self.hp -= tmp
            print("Przeciwnik odbiera Ci " + str(tmp) + " hp\n")

            if self.hp <= 0:
                print("Przegrałeś")
                break

    def update_lvl(self):
        if self.exp >= self.lvl * 100:
            self.exp -= self.lvl * 100
            self.lvl += 1
            print("Nowy poziom!\nTwój poziom: " + str(self.lvl))
