# -*- coding: utf-8 -*-
import random


class Action:
    def __init__(self):
        self.description = []
        self.description2 = []
        self.exp = []
        self.damage = []
        self.enemy = []
        self.done = []

    def add_action(self, description, description2, exp, damage, enemy):
        self.description.append(description)
        self.description2.append(description2)
        self.exp.append(exp)
        self.damage.append(damage)
        self.enemy.append(enemy)
        self.done.append(False)

    def randomize(self):
        all = list(zip(self.description, self.description2, self.exp, self.damage, self.enemy))
        random.shuffle(all)

        self.description, self.description2, self.exp, self.damage, self.enemy = map(list, zip(*all))

    def print_actions(self):
        print("-"*20)
        print("0. Anuluj")
        for i in range(len(self.description)):
            print(str(i+1) + ". " + self.description[i])

    def do_action(self, player):
        self.print_actions()
        num = -1

        while not (0 <= num < len(self.description) + 1):
            num = input("\nPodaj numer akcji: ")
            try:
                num = int(num)
            except ValueError:
                print("Wpisz cyfrę dzbanie!")
                num = -1

        if num != 0:

            # tablica jest od zera wiec trzeba zmniejszyc
            num -= 1

            if not self.done[num]:
                print("\n...")
                print(self.description2[num] + "\n")
                self.done[num] = True
                self.description[num] = "*Wykonano*"

                if self.exp[num] > 0:
                    print("Dostałeś " + str(self.exp[num]) + " exp")
                    player.update_lvl(self.exp[num])

                if self.damage[num] > 0:
                    player.update_hp(self.damage[num])

                if self.enemy[num] != "None":
                    print(self.enemy[num] + " atakuje Cię!")
                    player.attack()

                print("...\n")

            else:
                print("Akcje " + str(num+1) + " już wykonano\n")

