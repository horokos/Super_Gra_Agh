# -*- coding: utf-8 -*-
import os
import Load
import Code


class Struktura:
    def __init__(self, filename):
        self.id_room = 1
        Load.FILE_NAME = filename
        Load.load()

    def p_move(self, player):
        # pierwsza wyswietlanie ma byc wolne
        sec = 0.001
        while True:
            os.system('cls')
            Load.room.introduce(self.id_room - 1, sec)

            if self.id_room < 8:
                print("-"*20 + "\n\nGdzie się ruszasz? (1/2/3)\n")
                print("1. " + Load.room.rooms_doors[self.id_room * 2 + - 1])
                print("2. " + Load.room.rooms_doors[self.id_room * 2])

                if self.id_room > 1:
                    print("3. Zawróć")
                    if not all(Load.action[self.id_room - 2].done):
                        print("\nLub...\n4. Wykonaj akcje\n")

                move = input(">>>")

                if move == "1":
                    self.id_room *= 2
                    break

                if move == "2":
                    self.id_room = self.id_room * 2 + 1
                    break

                if self.id_room > 1:
                    if move == "3":
                            self.id_room = int(self.id_room / 2)
                            break

                    if move == "4" and not all(Load.action[self.id_room - 2].done):
                        Load.action[self.id_room - 2].do_action(player, Load.room, self.id_room - 1)
                        break

            else:
                print("-" * 20 + "\nGdzie się ruszasz? (1/2)\n")
                print("1. Wejdź do portalu")
                print("2. Zawróć")
                if not all(Load.action[self.id_room - 2].done):
                    print("\nLub...\n3. Wykonaj akcje\n")

                move = input(">>>")

                if move == "1":
                    Code.guess(player)
                    exit(0)
                    break

                if move == "2":
                    self.id_room = int(self.id_room / 2)
                    break

                if move == "3" and not all(Load.action[self.id_room - 2].done):
                    Load.action[self.id_room - 2].do_action(player, Load.room, self.id_room - 1)
                    break

            # kolejne wyswitlanie ma byc szybkie
            sec = 0

    os.system('cls')
