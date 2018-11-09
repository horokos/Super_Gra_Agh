# -*- coding: utf-8 -*-
import os
import random
import time
from Items import Weapon
from Items import Armor
import pickle


class Player:
    def __init__(self):
        self.exp = 0
        self.lvl = 1
        self.max_hp = 100
        self.hp = self.max_hp
        self.weapon = []
        self.armor = None

    def attack(self, enemy_name, senemy_hp):
        enemy_hp = senemy_hp

        while True:
            time.sleep(0.05)
            p = -1
            while not (0 <= p < len(self.weapon)):
                os.system('cls')
                print("-" * 20)
                self.slow_print("Hp Gracza: " + str(self.hp) + "\nHp przeciwnika: " + str(enemy_hp), 0.005)

                for x in range(0, len(self.weapon)):
                    print("%s. %s   (dmg %s-%s)" % (x + 1, self.weapon[x].attack_name, self.weapon[x].dmg - 10, self.weapon[x].dmg + 10))

                print("\nPodaj numer ataku")
                p = input(">>>")

                try:
                    p = int(p)
                    p -= 1
                except ValueError:
                    p = -1

            print("...")
            if random.randint(0, 100) < self.weapon[p].chance:
                if random.randint(1, 100) > self.weapon[p].crit:
                    tmp = self.weapon[p].dmg + random.randint(-10, 10)
                else:
                    print("Obrażenia krytyczne!")
                    tmp = (self.weapon[p].dmg + random.randint(-10, 10))*2
                enemy_hp -= tmp
                self.slow_print("Trafiłeś za " + str(tmp), 0.01)

            else:
                print("\nChybiłeś :(")

            if enemy_hp <= 0:
                tmp = random.randint(30, 60)
                self.slow_print("Wygrałeś!", 0.01)
                self.update_lvl(tmp)
                break

            tmp = random.randint(10, 25)
            self.slow_print(enemy_name + " atakuje Cię!", 0.01)
            self.update_hp(int(tmp*(100 - self.armor.armor)/100))

            input("\n\nWciśnij ENTER, aby kontynuować...")

    def update_lvl(self, value):
        time.sleep(0.05)
        levelup = False
        old_max_hp = self.max_hp

        self.exp += value
        self.slow_print("Dostałeś " + str(value) + " exp", 0.005)

        while self.exp >= self.lvl * 100:
            self.exp -= self.lvl * 100
            self.lvl += 1
            self.max_hp += 10
            levelup = True

        if levelup:
            print("*" * 20)
            self.slow_print("Nowy poziom!\nTwój poziom: " + str(self.lvl) + "\nJesteś w pełni wyleczony."
                            "\nTwój maksymalny poziom hp został zwiększony o " +
                            str(self.max_hp - old_max_hp) + "\n", 0.005)
            self.hp = self.max_hp
        else:
            self.slow_print("Brakuje Ci " + str(self.lvl * 100 - self.exp) + " exp do nowego poziomu", 0.005)

    def update_hp(self, value):
        time.sleep(0.05)
        self.hp -= value
        if self.hp <= 0:
            self.slow_print("Tracisz " + str(value) + " hp", 0.005)
            print("*RIP*")
            self.slow_print("Koniec gry :(\n", 0.005)
            self.save_score()
            input("Wciśnij ENTER, aby kontunuować...")
            exit(0)

        elif value > 0:
            self.slow_print("Tracisz %s hp, pozostało Ci %s/%s hp." % (str(value), str(self.hp), str(self.max_hp)), 0.005)
        else:
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            self.slow_print("Zostajesz uleczony o %s hp, masz %s/%s hp." % (str(abs(value)), str(self.hp), str(self.max_hp)), 0.005)

    def change_armor(self, name, armor):
        self.armor = Armor(name, armor)

    def add_weapon(self, name, dmg, chance, crit, attack_name):
        self.weapon.append(Weapon(name, dmg, chance, crit, attack_name))

    @staticmethod
    def slow_print(string, sec):
        for i in range(len(string)):
            print(string[i], end="", flush=True)
            time.sleep(sec)
        print("\n")

    def save_score(self):
        pass
