# -*- coding: utf-8 -*-
import random
import time


class Player:
    def __init__(self):
        self.hp = 100
        self.exp = 0
        self.lvl = 1

    def attack(self):
        enemy_hp = 100

        while True:
            time.sleep(0.05)
            print("-"*20)
            self.slow_print("Twoje hp " + str(self.hp) + "\nHp przeciwnika " + str(enemy_hp), 0.005)

            while True:
                self.slow_print("Jak chcesz atakować? (Silny/Szybki)\n", 0.005)
                p_attack = input(">>>")

                if p_attack.upper() == "SILNY" and random.randint(0, 100) < 40:
                    tmp = random.randint(40+self.lvl*10, 60+self.lvl*10)
                    enemy_hp -= tmp
                    self.slow_print("Trafiłeś za " + str(tmp), 0.01)
                    break

                elif p_attack.upper() == "SZYBKI" and random.randint(0, 100) < 80:
                    tmp = random.randint(20+self.lvl*10, 40+self.lvl*10)
                    enemy_hp -= tmp
                    self.slow_print("Trafiłeś za " + str(tmp), 0.01)
                    break

                elif p_attack.upper() != "SZYBKI" and p_attack.upper() != "SILNY":
                    print("Musisz wpisać Silny/Szybki\n")

                else:
                    print("Chybiłeś :(\n")
                    break

            if enemy_hp <= 0:
                tmp = random.randint(30, 60)
                self.slow_print("Wygrałeś, dostałeś " + str(tmp) + " exp\n", 0.01)
                self.update_lvl(tmp)
                break

            tmp = random.randint(10, 20)
            self.update_hp(tmp)

    def update_lvl(self, value):
        time.sleep(0.05)
        levelup = False
        self.exp += value
        self.slow_print("Dostałeś " + str(value) + " exp", 0.005)

        while self.exp >= self.lvl * 100:
            self.exp -= self.lvl * 100
            self.lvl += 1
            levelup = True

        if levelup:
            print("*" * 20)
            self.slow_print("Nowy poziom!\nTwój poziom: " + str(self.lvl) + "\n", 0.005)
            self.hp = 100

        else:
            self.slow_print("Brakuje Ci " + str(self.lvl * 100 - self.exp) + " exp do nowego poziomu", 0.005)

    def update_hp(self, value):
        time.sleep(0.05)
        self.hp -= value
        if self.hp <= 0:
            self.slow_print("Tracisz " + str(value) + " hp", 0.005)
            print("*RIP*")
            self.slow_print("Koniec gry :(\n", 0.005)
            input("Wciśnij dowolny klawisz, aby zakończyć")
            exit(0)
        else:
            self.slow_print("Tracisz " + str(value) + " hp, pozostało Ci " + str(self.hp) + "/100 hp", 0.005)

    @staticmethod
    def slow_print(string, sec):
        for i in range(len(string)):
            print(string[i], end="", flush=True)
            time.sleep(sec)
        print("\n")
