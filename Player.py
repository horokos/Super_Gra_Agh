# -*- coding: utf-8 -*-
import os
import random
import time
from Items import Weapon
from Items import Armor
import pickle


class Player:
    def __init__(self):
        self.type = 0
        self.exp = 0
        self.lvl = 1
        self.max_hp = 100
        self.hp = self.max_hp
        self.weapon = []
        self.armor = []
        self.available_weapons = []
        self.available_attack_names = []
        self.available_armors = []

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
                    print("%s. %s   (dmg %s-%s, chance %s%%)" % (x + 1, self.weapon[x].attack_name, self.weapon[x].dmg - 10, self.weapon[x].dmg + 10, self.weapon[x].chance))

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

            tmp = int(random.randint(10, 25) * ((self.lvl / 8) + 1))
            self.slow_print(enemy_name + " atakuje Cię!", 0.01)

            dmg_reduction = 0
            for x in self.armor:
                dmg_reduction += x.armor
            self.update_hp(int(tmp*(100 - dmg_reduction)/100))

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
            print("[*] RIP [*]")
            self.slow_print("Koniec gry :(", 0.005)
            self.save_score()
            input("\nWciśnij ENTER, aby kontunuować...")
            exit(0)

        elif value > 0:
            self.slow_print("Tracisz %s hp, pozostało Ci %s/%s hp." % (value, self.hp, self.max_hp), 0.005)
        else:
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            self.slow_print("Zostajesz uleczony o %s hp, masz %s/%s hp." % (abs(value), self.hp, self.max_hp), 0.005)

    def add_armor(self, name, armor):
        self.armor.append(Armor(name, armor))

    def add_random_armor(self):
        if len(self.available_weapons) > 0:
            name = self.available_armors.pop(random.randint(0, len(self.available_armors)-1))
            armor = self.lvl*10
            self.add_armor(name, armor)
            self.slow_print("Znajdujesz %s (armor %s)" % (name, armor), 0.005)

    def add_weapon(self, name, dmg, chance, crit, attack_name):
        self.weapon.append(Weapon(name, dmg, chance, crit, attack_name))

    def add_random_weapon(self):
        if len(self.available_weapons) > 0:
            index = random.randint(0, len(self.available_weapons) - 1)
            name = self.available_weapons.pop(index)
            dmg = random.randint(self.lvl + 2, self.lvl + 6) * 10
            chance = random.randint(40, 90)
            crit = random.randint(self.lvl + 1, self.lvl + 5)
            attack_name = self.available_attack_names.pop(index)
            self.add_weapon(name, dmg, chance, crit, attack_name)
            self.slow_print("Znajdujesz %s (dmg %s-%s, chance %s%%, crit %s%%)" % (name, dmg - 10, dmg + 10, chance, crit), 0.005)

    def load_names(self, file):
        with open(file) as f:
            lines = f.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].replace("*a", "ą")
                lines[i] = lines[i].replace("*A", "Ą")
                lines[i] = lines[i].replace("*c", "ć")
                lines[i] = lines[i].replace("*C", "Ć")
                lines[i] = lines[i].replace("*e", "ę")
                lines[i] = lines[i].replace("*E", "Ę")
                lines[i] = lines[i].replace("*l", "ł")
                lines[i] = lines[i].replace("*L", "Ł")
                lines[i] = lines[i].replace("*n", "ń")
                lines[i] = lines[i].replace("*N", "Ń")
                lines[i] = lines[i].replace("*s", "ś")
                lines[i] = lines[i].replace("*S", "Ś")
                lines[i] = lines[i].replace("*o", "ó")
                lines[i] = lines[i].replace("*O", "Ó")
                lines[i] = lines[i].replace("*z", "ż")
                lines[i] = lines[i].replace("*Z", "Ż")
                lines[i] = lines[i].replace("*x", "ź")
                lines[i] = lines[i].replace("*X", "Ź")
            for i in range(0, len(lines) - 1, 3):
                self.available_weapons.append(lines[i].replace("\n", ""))
                self.available_attack_names.append(lines[i + 1].replace("\n", ""))
                self.available_armors.append(lines[i + 2].replace("\n", ""))

        f.close()

    def show_equipment(self):
        os.system('cls')
        print("-" * 20)
        for x in range(1, len(self.weapon)):
            print("%s. %s   (dmg %s-%s, chance %s%%, crit %s%%)" % (x, self.weapon[x].name, self.weapon[x].dmg - 10, self.weapon[x].dmg + 10, self.weapon[x].chance, self.weapon[x].crit))
        for x in range(0, len(self.armor)):
            print("%s. %s   (dmg reduction %s%%)" % (len(self.weapon) + x, self.armor[x].name, self.armor[x].armor))
        input("\n\nWciśnij ENTER, aby kontunuować...")

    @staticmethod
    def slow_print(string, sec):
        for i in range(len(string)):
            print(string[i], end="", flush=True)
            time.sleep(sec)
        print("\n")

    def save_score(self):
        score = self.exp
        for i in range(self.lvl + 1):
            score += i * 100
        score -= 100

        print("\nZdobyłeś %s punktów!\n" % score)
